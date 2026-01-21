# src/markdown_utils.py
def extract_title(markdown: str) -> str:
    """Extract the first h1 (#) header from markdown text."""
    for line in markdown.splitlines():
        line = line.strip()
        if line.startswith("# ") and not line.startswith("##"):
            # Remove leading # and whitespace
            return line[1:].strip()
    raise ValueError("No H1 header found in markdown")
