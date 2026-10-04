import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
from mod import parse_ratio
print(f"ratio(1:2)={parse_ratio('1:2'):.2f}")
