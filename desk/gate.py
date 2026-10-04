"""Gate: a decision function the PreToolUse hook calls. Stdlib only.

Gates are missing tools, not reminders. The deny list wins over the registry.
decide() returns (allow, reason). Reason is printed to stderr by the hook (exit 2 blocks).
"""
import json
import os
import re
import shlex

DENY_VERBS = {
    "order", "send", "pay", "payment", "purchase", "buy", "checkout", "hire", "sign",
    "diagnose", "exploit", "payload", "bypass", "decrypt", "reply", "forward",
    "trade", "broker",
}
DENY_PAIRS = [("hardware", "start")]
DENY_COMMANDS = {"sendmail", "mail", "mailx", "mutt", "msmtp", "ssmtp", "swaks"}
WRAPPERS = {"sudo", "env", "nohup", "time", "xargs", "command", "exec", "nice"}
FILE_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit"}
TRACE_PATH = "trace/trace.jsonl"


def tokens(name):
    """Split a tool name into lowercase word tokens: camelCase, '_', '-', '__' all split."""
    spaced = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", name)
    return [t for t in re.split(r"[^A-Za-z0-9]+", spaced.lower()) if t]


def verb_hit(name):
    toks = tokens(name)
    hit = sorted(set(toks) & DENY_VERBS)
    for a, b in DENY_PAIRS:
        if a in toks and b in toks:
            hit.append(f"{a}-{b}")
    return hit


CODE_RUNNERS = {"python", "python3", "bash", "sh", "zsh", "dash", "node", "perl", "ruby", "eval", "source"}
_HEREDOC = re.compile(r"(?m)^(?P<head>[^\n]*?)<<-?\s*(?P<q>['\"]?)(?P<tag>\w+)(?P=q)(?P<rest>[^\n]*)\n(?P<body>.*?)\n[ \t]*(?P=tag)[ \t]*(?=\n|$)", re.S)


def _strip_heredocs(cmd):
    """Drop heredoc bodies that are data (cat, tee, echo...). A body fed to an interpreter is code: keep it."""
    def repl(m):
        words = re.findall(r"[\w./-]+", m.group("head"))
        if any(os.path.basename(w) in CODE_RUNNERS for w in words):
            return m.group(0)
        return m.group("head") + " " + m.group("rest")
    return _HEREDOC.sub(repl, cmd)


def _argv0s(cmd):
    out = []
    for seg in re.split(r"&&|\|\||[;|\n]", _strip_heredocs(cmd)):
        try:
            words = shlex.split(seg, posix=True)
        except ValueError:
            words = seg.split()
        while words and (re.match(r"^\w+=", words[0]) or words[0] in WRAPPERS):
            words = words[1:]
        if words:
            out.append(os.path.basename(words[0]))
    return out


_TRACE_WRITE = [
    r"(^|[;&|\s])(rm|mv|truncate|shred|unlink|dd|chattr|cp|ln|rsync|install)(\s|$)",
    r"sed\s+(-[a-zA-Z]*i|--in-place)",
    r"perl\s+-[a-zA-Z]*i",
    r"(^|[^>])>\s*\S*trace/",
    r"tee\s+(?!-a)\S*trace/",
    r"open\([^)]*trace[^)]*,\s*['\"][^'\"]*[wx+]",
]


def _touches_trace_destructively(cmd):
    cmd = _strip_heredocs(cmd)
    if "trace/" not in cmd:
        return False
    return any(re.search(p, cmd) for p in _TRACE_WRITE)


def decide(tool_name, tool_input, reg):
    tool_input = tool_input or {}
    # 1. file tools may not write the trace
    if tool_name in FILE_TOOLS:
        path = tool_input.get("file_path") or tool_input.get("notebook_path") or ""
        norm = os.path.normpath(path).replace(os.sep, "/")
        if norm.endswith(TRACE_PATH):
            return False, f"DENY {tool_name}: trace is append-only; the agent has no write or delete on its own record"
        return True, "file tool"
    # 2. shell
    if tool_name == "Bash":
        cmd = tool_input.get("command", "")
        deny_cmds = set(reg.get("deny_commands", [])) | DENY_COMMANDS
        for a0 in _argv0s(cmd):
            if a0 in deny_cmds:
                return False, f"DENY Bash: '{a0}' is a send-class command; prepare the details and stop"
        if _touches_trace_destructively(cmd):
            return False, "DENY Bash: trace/ is append-only; read it (cat, tail, grep, wc) or run verify-trace"
        return True, "shell"
    # 3. MCP tools: deny verbs win, then the registry, then the unregistered policy
    if tool_name.startswith("mcp__"):
        hit = verb_hit(tool_name)
        if hit:
            return False, f"DENY {tool_name}: gate verb {hit}; the irreversible tool is absent by design"
        entry = next((t for t in reg.get("tools", []) if t.get("name") == tool_name), None)
        if entry is None:
            if reg.get("unregistered_mcp", "deny") == "deny":
                return False, f"DENY {tool_name}: not in registry/tools.json; connecting is a human accept, scope read first"
            return True, "unregistered (allow-traced)"
        if entry.get("scope") == "act" and not entry.get("human_added"):
            return False, f"DENY {tool_name}: scope act requires a human add (human_added is false)"
        return True, f"registry scope {entry.get('scope')}"
    # 4. built-ins
    if tool_name in set(reg.get("builtin_deny", [])):
        return False, f"DENY {tool_name}: builtin_deny"
    return True, "builtin"


def load_registry(root):
    with open(os.path.join(root, "registry", "tools.json")) as f:
        return json.load(f)
