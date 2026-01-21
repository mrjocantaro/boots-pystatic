from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_textnodes(text: str):
    # Start with a single Text node
    nodes = [TextNode(text, TextType.TEXT)]
    
    # Split by inline code first (backticks)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    # Split by bold (**)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    # Split by italic (_)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    # Split out images
    nodes = split_nodes_image(nodes)
    # Split out links
    nodes = split_nodes_link(nodes)

    return nodes
