from pathlib import Path
import os

def check_path(path_string: str) -> None:
    path = Path(path_string)
    print("Path:", path)
    print("Exists:", path.exists())
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

    if path.exists():
        print("Name:", path.name)
        print("Parent directory:", path.parent)

if __name__ == "__main__":
    entered = input("Enter a path to check (default: current directory): ").strip()
    check_path(entered or ".")
