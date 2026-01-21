import re
from textnode import TextNode, TextType
from htmlnode import LeafNode


def text_node_to_html_node(text_node: TextNode):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)

    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)

    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)

    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)

    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})

    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

    raise ValueError("Invalid TextType")


def text_to_textnodes(text: str):
    nodes = [TextNode(text, TextType.TEXT)]

    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes


def split_nodes_delimiter(nodes, delimiter, text_type):
    result = []
    for node in nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue

        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError(f"Unmatched delimiter {delimiter}")

        for i, part in enumerate(parts):
            if part == "":
                continue
            if i % 2 == 0:
                result.append(TextNode(part, TextType.TEXT))
            else:
                result.append(TextNode(part, text_type))
    return result


def split_nodes_link(nodes):
    result = []
    for node in nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue

        text = node.text
        while True:
            match = re.search(r"\[([^\]]+)\]\(([^)]+)\)", text)
            if not match:
                result.append(TextNode(text, TextType.TEXT))
                break

            if match.start() > 0:
                result.append(TextNode(text[:match.start()], TextType.TEXT))

            result.append(TextNode(match.group(1), TextType.LINK, match.group(2)))
            text = text[match.end():]

    return result


def split_nodes_image(nodes):
    result = []
    for node in nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue

        text = node.text
        while True:
            match = re.search(r"!\[([^\]]*)\]\(([^)]+)\)", text)
            if not match:
                result.append(TextNode(text, TextType.TEXT))
                break

            if match.start() > 0:
                result.append(TextNode(text[:match.start()], TextType.TEXT))

            result.append(TextNode(match.group(1), TextType.IMAGE, match.group(2)))
            text = text[match.end():]

    return result
