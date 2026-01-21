import shutil
from pathlib import Path
import markdown

def generate_pages_recursive(content_dir, template_dir, dest_dir, basepath):
    content_dir = Path(content_dir)
    template_dir = Path(template_dir)
    dest_dir = Path(dest_dir)

    template_path = template_dir / "template.html"  # tu template principal

    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")

    dest_dir.mkdir(parents=True, exist_ok=True)

    for md_path in content_dir.rglob("*.md"):
        relative_path = md_path.relative_to(content_dir)
        output_path = dest_dir / relative_path.with_suffix(".html")
        output_path.parent.mkdir(parents=True, exist_ok=True)

        generate_page(md_path, template_path, output_path, basepath)


def generate_page(from_path, template_path, dest_path, basepath):
    markdown_content = from_path.read_text(encoding="utf-8")
    html_content = markdown.markdown(markdown_content)
    title = extract_title(markdown_content)

    template = template_path.read_text(encoding="utf-8")

    html = template.replace("{{ Title }}", title)
    html = html.replace("{{ Content }}", html_content)

    # Ajustar todos los recursos al basepath
    html = html.replace('href="/', f'href="{basepath}')
    html = html.replace('src="/', f'src="{basepath}')

    dest_path.write_text(html, encoding="utf-8")


def extract_title(markdown_text):
    for line in markdown_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "Untitled"
