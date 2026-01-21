import os
import shutil

def copy_dir_recursive(src: str, dst: str) -> None:
    """
    Recursively copy the contents of `src` directory into `dst`.
    Deletes `dst` first if it exists.
    """
    # Delete destination directory if it exists
    if os.path.exists(dst):
        print(f"Removing existing directory: {dst}")
        shutil.rmtree(dst)

    # Create the destination directory
    os.makedirs(dst, exist_ok=True)

    # Iterate over all items in the source directory
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isfile(src_path):
            # Copy the file
            print(f"Copying file: {src_path} -> {dst_path}")
            shutil.copy2(src_path, dst_path)
        elif os.path.isdir(src_path):
            # Recursively copy the subdirectory
            print(f"Entering directory: {src_path}")
            copy_dir_recursive(src_path, dst_path)
