from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import text_node_to_html_node, text_to_textnodes
from markdown_blocks import markdown_to_blocks
from type_detect import block_to_block_type, BlockType


def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            inline_nodes = [
                text_node_to_html_node(node)
                for node in text_to_textnodes(block)
            ]
            children.append(ParentNode("p", inline_nodes))

        elif block_type == BlockType.HEADING:
            # contar cantidad de #
            level = 0
            for char in block:
                if char == "#":
                    level += 1
                else:
                    break

            level = min(level, 6)
            heading_text = block[level:].strip()

            inline_nodes = [
                text_node_to_html_node(node)
                for node in text_to_textnodes(heading_text)
            ]
            children.append(ParentNode(f"h{level}", inline_nodes))

        elif block_type == BlockType.CODE:
            lines = block.splitlines()
            code_text = "\n".join(lines[1:-1]) + "\n"
            code_node = LeafNode("code", code_text)
            children.append(ParentNode("pre", [code_node]))

        elif block_type == BlockType.QUOTE:
            lines = []
            for line in block.splitlines():
                if not line.startswith(">"):
                    raise ValueError("Invalid quote block")
                lines.append(line.lstrip("> ").rstrip())

            quote_text = "\n".join(lines)

            inline_nodes = [
                text_node_to_html_node(node)
                for node in text_to_textnodes(quote_text)
            ]

            quote_node = ParentNode("blockquote", inline_nodes)
            children.append(quote_node)

        elif block_type == BlockType.UNORDERED_LIST:
            items = []
            for line in block.splitlines():
                text = line[2:] if line.startswith("- ") else line
                inline_nodes = [
                    text_node_to_html_node(node)
                    for node in text_to_textnodes(text)
                ]
                items.append(ParentNode("li", inline_nodes))
            children.append(ParentNode("ul", items))

        elif block_type == BlockType.ORDERED_LIST:
            items = []
            for line in block.splitlines():
                parts = line.split(". ", 1)
                text = parts[1] if len(parts) > 1 else parts[0]
                inline_nodes = [
                    text_node_to_html_node(node)
                    for node in text_to_textnodes(text)
                ]
                items.append(ParentNode("li", inline_nodes))
            children.append(ParentNode("ol", items))

        else:
            raise ValueError(f"Unsupported block type: {block_type}")

    return ParentNode("div", children)
