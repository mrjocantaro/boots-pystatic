import unittest

def markdown_to_blocks(markdown: str) -> list[str]:
    # Split by double newlines to separate blocks
    raw_blocks = markdown.split("\n\n")
    # Strip whitespace and ignore empty blocks
    blocks = [block.strip() for block in raw_blocks if block.strip()]
    return blocks


class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_empty_blocks_removed(self):
        md = "\n\nFirst block\n\n\nSecond block\n\n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["First block", "Second block"])

    def test_single_block(self):
        md = "Just one block of text with no double newlines"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Just one block of text with no double newlines"])

if __name__ == "__main__":
    unittest.main()
