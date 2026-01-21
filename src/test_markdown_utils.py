# src/test_markdown_utils.py
import unittest
from markdown_utils import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_simple_h1(self):
        self.assertEqual(extract_title("# Hello"), "Hello")
    
    def test_h1_with_spaces(self):
        self.assertEqual(extract_title("#   My Page  "), "My Page")
    
    def test_multiple_headers(self):
        md = "# First\n## Second\n# Third"
        self.assertEqual(extract_title(md), "First")
    
    def test_no_h1(self):
        md = "## Not H1\nSome text"
        with self.assertRaises(ValueError):
            extract_title(md)

if __name__ == "__main__":
    unittest.main()
