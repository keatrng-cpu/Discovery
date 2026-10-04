import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
from mod import slugify
text = slugify('Hello, World!')
print('<!doctype html><meta charset=utf-8><body style="margin:0;font:20px monospace;background:#fff;color:#000"><pre>' + text + '</pre></body>')
