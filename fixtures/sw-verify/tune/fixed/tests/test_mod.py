import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from mod import parse_ratio

class T(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(parse_ratio('3:4'), 0.75)
    def test_zero_numerator(self):
        self.assertEqual(parse_ratio('0:5'), 0.0)

if __name__ == '__main__':
    unittest.main()
