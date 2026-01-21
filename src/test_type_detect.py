# src/test_type_detect.py
import unittest
from type_detect import BlockType, block_to_block_type

class TestBlockTypeDetection(unittest.TestCase):
    def test_paragraph(self):
        self.assertEqual(
            block_to_block_type("This is a normal paragraph."),
            BlockType.PARAGRAPH,
        )

    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### Heading 3"), BlockType.HEADING)

    def test_code_block(self):
        code = "```\nprint('Hello')\n```"
        self.assertEqual(block_to_block_type(code), BlockType.CODE)

    def test_quote(self):
        quote = "> First line\n> Second line"
        self.assertEqual(block_to_block_type(quote), BlockType.QUOTE)

    def test_unordered_list(self):
        ul = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(ul), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        ol = "1. First\n2. Second\n3. Third"
        self.assertEqual(block_to_block_type(ol), BlockType.ORDERED_LIST)

if __name__ == "__main__":
    unittest.main()
