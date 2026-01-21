import sys
from generate import generate_pages_recursive
from copy_static import copy_dir_recursive

def main():
    # Basepath configurable desde línea de comandos, por defecto "/"
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    # Copiamos archivos estáticos a docs/
    copy_dir_recursive("static", "docs")

    # Generamos todas las páginas markdown en docs/
    generate_pages_recursive("content", "docs", basepath)

if __name__ == "__main__":
    main()
