import sys
from pathlib import Path
from generate import generate_pages_recursive
from copy_static import copy_dir_recursive

def main():
    # Basepath configurable desde argumento CLI
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    # Directorios
    content_dir = Path("content")
    static_dir = Path("static")
    dest_dir = Path("docs")  # Para GitHub Pages

    # Copiar recursos estáticos
    copy_dir_recursive(static_dir, dest_dir)

    # Generar todas las páginas
    generate_pages_recursive(content_dir, static_dir, dest_dir, basepath)

    print(f"Site generated into {dest_dir} with basepath '{basepath}'")

if __name__ == "__main__":
    main()
