import os
import shutil
from pathlib import Path
import markdown

def generate_pages_recursive(content_dir, dest_dir, basepath="/"):
    """
    Recorre recursivamente todos los archivos markdown en content_dir
    y genera páginas HTML en dest_dir, respetando la estructura de carpetas.
    """
    content_dir = Path(content_dir)
    dest_dir = Path(dest_dir)

    # Borramos y recreamos el directorio de destino
    if dest_dir.exists():
        shutil.rmtree(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)

    # Template mínimo para todas las páginas
    template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ Title }}</title>
    <link href="{basepath}index.css" rel="stylesheet" />
</head>
<body>
<article>{{ Content }}</article>
</body>
</html>
"""

    # Recorremos todos los markdown
    for md_path in content_dir.rglob("*.md"):
        relative_path = md_path.relative_to(content_dir)
        output_path = dest_dir / relative_path.with_suffix(".html")
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Generamos página
        generate_page(md_path, template, output_path, basepath)


def generate_page(from_path, template, dest_path, basepath="/"):
    """
    Convierte un archivo markdown a HTML usando el template y lo escribe en dest_path.
    """
    markdown_content = from_path.read_text(encoding="utf-8")
    html_content = markdown.markdown(markdown_content)
    title = extract_title(markdown_content)

    html = template.replace("{{ Title }}", title)
    html = html.replace("{{ Content }}", html_content)

    # Ajustamos paths para assets
    html = html.replace('href="{basepath}', f'href="{basepath}')
    html = html.replace('src="{basepath}', f'src="{basepath}')

    dest_path.write_text(html, encoding="utf-8")


def extract_title(markdown_text):
    """
    Extrae el primer H1 del markdown. Si no existe, devuelve "Untitled".
    """
    for line in markdown_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "Untitled"
