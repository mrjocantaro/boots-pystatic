from textnode import TextNode, TextType
from typing import List


def split_nodes_delimiter(
    old_nodes: List[TextNode],
    delimiter: str,
    text_type: TextType,
) -> List[TextNode]:
    """
    Split text nodes on a given delimiter and convert the delimited
    portions into nodes of the specified text_type.
    """
    new_nodes: List[TextNode] = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            # Keep non-text nodes as-is
            new_nodes.append(node)
            continue

        text = node.text
        parts = text.split(delimiter)

        if len(parts) == 1:
            # No delimiter found, keep the node as-is
            new_nodes.append(node)
            continue

        if len(parts) % 2 == 0:
            # Even number of parts -> unmatched delimiter
            raise ValueError(
                f"Unmatched delimiter '{delimiter}' in text: {text}"
            )

        # Odd number of parts -> delimiters match
        for i, part in enumerate(parts):
            if part == "":
                continue  # skip empty strings
            if i % 2 == 0:
                # Outside delimiter -> TEXT
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                # Inside delimiter -> specified type
                new_nodes.append(TextNode(part, text_type))

    return new_nodes
