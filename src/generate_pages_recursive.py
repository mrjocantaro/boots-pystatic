from generate_page import generate_page
import os

def generate_pages_recursive(content_dir, template_path, dest_dir, basepath):
    for item in os.listdir(content_dir):
        item_path = os.path.join(content_dir, item)
        if os.path.isfile(item_path):
            if item.endswith(".md"):
                generate_page(item_path, template_path, dest_dir, basepath)
        else:
            new_dest = os.path.join(dest_dir, item)
            os.makedirs(new_dest, exist_ok=True)
            generate_pages_recursive(item_path, template_path, new_dest, basepath)
