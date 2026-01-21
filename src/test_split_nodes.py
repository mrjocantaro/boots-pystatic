import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code_split(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_bold_split(self):
        node = TextNode("Some **bold text** here", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        expected = [
            TextNode("Some ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(" here", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_italic_split(self):
        node = TextNode("This is _italic_ text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_no_delimiter(self):
        node = TextNode("Just normal text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [node])

    def test_non_text_node_passed(self):
        node = TextNode("Bold text", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [node])

    def test_unmatched_delimiter_raises(self):
        node = TextNode("This is `broken code", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_multiple_nodes(self):
        nodes = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("**bold** world", TextType.TEXT)
        ]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        expected = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" world", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)


if __name__ == "__main__":
    unittest.main()
