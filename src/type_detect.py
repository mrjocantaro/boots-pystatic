# src/type_detect.py
from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    lines = block.splitlines()
    
    if not lines:
        return BlockType.PARAGRAPH

    if re.match(r"^#{1,6} ", lines[0]):
        return BlockType.HEADING

    if lines[0].startswith("```") and lines[-1].startswith("```") and len(lines) >= 2:
        return BlockType.CODE

    if all(line.startswith(">") for line in block.splitlines()):
        return BlockType.QUOTE

    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    is_ordered = True
    for i, line in enumerate(lines, start=1):
        if not re.match(rf"^{i}\. ", line):
            is_ordered = False
            break
    if is_ordered:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
