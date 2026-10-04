import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
from mod import parse_ratio
text = f"ratio(1:2)={parse_ratio('1:2'):.2f}"
print('<!doctype html><meta charset=utf-8><body style="margin:0;font:20px monospace;background:#fff;color:#000"><pre>' + text + '</pre></body>')
