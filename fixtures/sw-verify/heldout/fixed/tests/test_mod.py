import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from mod import slugify

class T(unittest.TestCase):
    def test_punctuation_edges(self):
        self.assertEqual(slugify('Hello, World!'), 'hello-world')
    def test_padded_spaces(self):
        self.assertEqual(slugify('  A  B '), 'a-b')

if __name__ == '__main__':
    unittest.main()
