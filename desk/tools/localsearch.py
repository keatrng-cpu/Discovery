#!/usr/bin/env python3
"""Offline corpus search that logs every query. The held-out harness for retrieval directives.

usage: localsearch.py <corpus_dir> "<query>"   (set DESK_SEARCH_LOG=<file> to choose the log)
Prints JSON lines {doc, line, text, score}. Production retrieval is mcp__FireCrawl__firecrawl_search;
this stands in where a check must be deterministic and offline.
"""
import json
import os
import re
import sys

STOP = set("the a an of to in and or for on at by with was were is are be been it its as that this from per".split())


def toks(s):
    return {t for t in re.findall(r"[a-z0-9]+", s.lower()) if t not in STOP}


def main():
    if len(sys.argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    corpus, query = sys.argv[1], sys.argv[2]
    q = toks(query)
    hits = []
    for name in sorted(os.listdir(corpus)):
        p = os.path.join(corpus, name)
        if not os.path.isfile(p):
            continue
        for i, line in enumerate(open(p, encoding="utf-8").read().splitlines(), 1):
            sc = len(q & toks(line))
            if sc:
                hits.append({"doc": name, "line": i, "text": line, "score": sc})
    hits.sort(key=lambda h: (-h["score"], h["doc"], h["line"]))
    log = os.environ.get("DESK_SEARCH_LOG", "artifacts/search.log")
    os.makedirs(os.path.dirname(log) or ".", exist_ok=True)
    with open(log, "a") as f:
        f.write(json.dumps({"query": query, "n_hits": len(hits)}) + "\n")
    for h in hits[:5]:
        print(json.dumps(h))
    return 0


if __name__ == "__main__":
    sys.exit(main())
