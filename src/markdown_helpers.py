import re
import unittest

def extract_markdown_images(text: str):
    """
    Extract markdown images from text.
    Returns a list of tuples: (alt_text, url)
    """
    pattern = r'!\[([^\]]+)\]\(([^)]+)\)'
    return re.findall(pattern, text)

def extract_markdown_links(text: str):
    """
    Extract markdown links from text.
    Returns a list of tuples: (anchor_text, url)
    """
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    return re.findall(pattern, text)


# Example tests
class TestMarkdownExtraction(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        expected = [("image", "https://i.imgur.com/zjjcJKZ.png")]
        self.assertListEqual(extract_markdown_images(text), expected)

    def test_extract_multiple_images(self):
        text = "![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        self.assertListEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_links(self):
        text = "Link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev")
        ]
        self.assertListEqual(extract_markdown_links(text), expected)

    def test_no_matches(self):
        text = "No markdown here!"
        self.assertListEqual(extract_markdown_images(text), [])
        self.assertListEqual(extract_markdown_links(text), [])

if __name__ == "__main__":
    unittest.main()
