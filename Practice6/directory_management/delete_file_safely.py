from pathlib import Path
import os

def delete_file_safely(path_string: str) -> bool:
    path = Path(path_string)

    if not path.exists():
        print("The path does not exist.")
        return False
    if not path.is_file():
        print("The path is not a regular file; refusing to delete it.")
        return False
    if not os.access(path, os.W_OK):
        print("The file is not writable; deletion may fail.")
        return False

    confirmation = input(f"Delete '{path}'? Type YES to confirm: ")
    if confirmation != "YES":
        print("Deletion cancelled.")
        return False

    try:
        path.unlink()
        print("File deleted.")
        return True
    except OSError as error:
        print("Deletion failed:", error)
        return False

if __name__ == "__main__":
    target = input("File path to delete: ").strip()
    if target:
        delete_file_safely(target)
