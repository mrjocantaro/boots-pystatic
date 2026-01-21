import unittest
from src.extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_simple_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_title_with_whitespace(self):
        self.assertEqual(extract_title("#   Hello World   "), "Hello World")

    def test_title_not_first_line(self):
        md = """
Some text
# Actual Title
More text
"""
        self.assertEqual(extract_title(md), "Actual Title")

    def test_ignores_h2(self):
        md = "## Not This\n# This One"
        self.assertEqual(extract_title(md), "This One")

    def test_no_h1_raises(self):
        with self.assertRaises(Exception):
            extract_title("## No title here")


if __name__ == "__main__":
    unittest.main()
