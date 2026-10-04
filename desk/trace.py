"""Append-only, hash-chained trace. Stdlib only.

Record k carries prev = sha256(bytes of record k-1, no newline). Editing, deleting, or reordering any
record that has a successor breaks the chain. Limits, stated plainly: the final record can be edited
and the tail can be truncated without a chain break; real append-only needs the filesystem (chattr +a)
or a remote write-once sink. The agent has no write path to this file (see gate.py).
"""
import fcntl
import hashlib
import json
import os

ZERO = "0" * 64


def path(root):
    return os.path.join(root, "trace", "trace.jsonl")


def _last_line(f):
    f.seek(0, os.SEEK_END)
    size = f.tell()
    if size == 0:
        return None
    back = min(size, 65536)
    f.seek(size - back)
    data = f.read(back).rstrip(b"\n")
    last = data.split(b"\n")[-1]
    return last or None


def append(root, rec):
    p = path(root)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "a+b") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        try:
            last = _last_line(f)
            if last is None:
                prev, seq = ZERO, 0
            else:
                prev = hashlib.sha256(last).hexdigest()
                try:
                    seq = int(json.loads(last)["seq"]) + 1
                except Exception:
                    seq = -1  # corrupted tail; verify() will report it
            out = dict(rec, seq=seq, prev=prev)
            f.write((json.dumps(out, sort_keys=True, separators=(",", ":")) + "\n").encode())
            f.flush()
            os.fsync(f.fileno())
        finally:
            fcntl.flock(f, fcntl.LOCK_UN)
    return out


def verify(root):
    p = path(root)
    if not os.path.exists(p):
        return True, "no trace file (0 records)"
    prev, n = ZERO, 0
    with open(p, "rb") as f:
        for i, raw in enumerate(f, 1):
            line = raw.rstrip(b"\n")
            if not line:
                return False, f"line {i}: blank line"
            try:
                rec = json.loads(line)
            except Exception:
                return False, f"line {i}: not JSON"
            if rec.get("prev") != prev:
                return False, f"line {i}: chain break (prev does not match record {n - 1})"
            if rec.get("seq") != n:
                return False, f"line {i}: seq {rec.get('seq')} != {n}"
            prev = hashlib.sha256(line).hexdigest()
            n += 1
    return True, f"{n} records, chain intact"
