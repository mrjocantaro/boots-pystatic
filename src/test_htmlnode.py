import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_single(self):
        node = HTMLNode(tag="a", props={"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')

    def test_props_to_html_multiple(self):
        node = HTMLNode(tag="a", props={"href": "https://example.com", "target": "_blank"})
        # Order of dict iteration in Python >=3.7 preserves insertion order
        self.assertEqual(node.props_to_html(), ' href="https://example.com" target="_blank"')

    def test_props_to_html_none(self):
        node = HTMLNode(tag="p")
        self.assertEqual(node.props_to_html(), "")

    def test_repr_contains_all_fields(self):
        child = HTMLNode(tag="span", value="Hello")
        node = HTMLNode(tag="div", children=[child], props={"class": "container"})
        expected_repr = (
            "HTMLNode(tag='div', value=None, children=[HTMLNode(tag='span', value='Hello', "
            "children=None, props=None)], props={'class': 'container'})"
        )
        self.assertEqual(repr(node), expected_repr)

import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    # ... previous HTMLNode tests ...

    # LeafNode tests
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leaf_value_required(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None).to_html()

    def test_leaf_repr(self):
        node = LeafNode("span", "Test", {"class": "highlight"})
        expected_repr = "LeafNode(tag='span', value='Test', props={'class': 'highlight'})"
        self.assertEqual(repr(node), expected_repr)
import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    # LeafNode tests ...
    # (assume previous LeafNode tests are here)

    # ParentNode tests
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>"
        )

    def test_to_html_multiple_children(self):
        children = [
            LeafNode("b", "Bold"),
            LeafNode(None, "Normal"),
            LeafNode("i", "Italic")
        ]
        parent_node = ParentNode("p", children)
        self.assertEqual(
            parent_node.to_html(),
            "<p><b>Bold</b>Normal<i>Italic</i></p>"
        )

    def test_to_html_with_props(self):
        children = [LeafNode("span", "text")]
        parent_node = ParentNode("a", children, {"href": "https://example.com"})
        self.assertEqual(
            parent_node.to_html(),
            '<a href="https://example.com"><span>text</span></a>'
        )

    def test_repr(self):
        child = LeafNode("span", "child")
        node = ParentNode("div", [child], {"id": "main"})
        expected_repr = f"ParentNode(tag='div', children={[child]!r}, props={{'id': 'main'}})"
        self.assertEqual(repr(node), expected_repr)

    def test_missing_tag_raises(self):
        child = LeafNode("span", "child")
        with self.assertRaises(ValueError):
            ParentNode(None, [child]).to_html()

    def test_missing_children_raises(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None)


if __name__ == "__main__":
    unittest.main()
