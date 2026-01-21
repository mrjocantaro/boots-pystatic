import re
from textnode import TextNode, TextType

def split_nodes_image(old_nodes):
    """
    Split TextType.TEXT nodes by markdown images ![alt](url)
    Return a new list of TextNode objects.
    """
    new_nodes = []

    img_pattern = r'!\[([^\]]+)\]\(([^)]+)\)'

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = []
        last_index = 0

        for match in re.finditer(img_pattern, node.text):
            start, end = match.span()
            # Text before the image
            if start > last_index:
                parts.append(TextNode(node.text[last_index:start], TextType.TEXT))
            # The image itself
            alt_text, url = match.groups()
            parts.append(TextNode(alt_text, TextType.IMAGE, url))
            last_index = end

        # Remaining text after last match
        if last_index < len(node.text):
            parts.append(TextNode(node.text[last_index:], TextType.TEXT))

        new_nodes.extend(parts)

    return new_nodes


def split_nodes_link(old_nodes):
    """
    Split TextType.TEXT nodes by markdown links [text](url)
    Return a new list of TextNode objects.
    """
    new_nodes = []

    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = []
        last_index = 0

        for match in re.finditer(link_pattern, node.text):
            start, end = match.span()
            # Text before the link
            if start > last_index:
                parts.append(TextNode(node.text[last_index:start], TextType.TEXT))
            # The link itself
            anchor_text, url = match.groups()
            parts.append(TextNode(anchor_text, TextType.LINK, url))
            last_index = end

        # Remaining text after last match
        if last_index < len(node.text):
            parts.append(TextNode(node.text[last_index:], TextType.TEXT))

        new_nodes.extend(parts)

    return new_nodes
