import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    # Test 1: identical nodes with default url
    def test_eq_same_properties(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    # Test 2: different text content
    def test_not_equal_different_text(self):
        node1 = TextNode("Text A", TextType.BOLD)
        node2 = TextNode("Text B", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    # Test 3: different text_type
    def test_not_equal_different_type(self):
        node1 = TextNode("Some text", TextType.BOLD)
        node2 = TextNode("Some text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    # Test 4: different url
    def test_not_equal_different_url(self):
        node1 = TextNode("Link text", TextType.LINK, "https://example.com")
        node2 = TextNode("Link text", TextType.LINK, "https://another.com")
        self.assertNotEqual(node1, node2)

    # Test 5: one has url, other doesn't
    def test_not_equal_url_vs_none(self):
        node1 = TextNode("Link text", TextType.LINK, "https://example.com")
        node2 = TextNode("Link text", TextType.LINK)
        self.assertNotEqual(node1, node2)

    # Test 6: __repr__ produces expected string
    def test_repr(self):
        node = TextNode("Hello", TextType.BOLD, None)
        expected = "TextNode('Hello', 'bold', None)"
        self.assertEqual(repr(node), expected)


if __name__ == "__main__":
    unittest.main()
