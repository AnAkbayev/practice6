from pathlib import Path
import os

def list_path(path_string: str = ".") -> None:
    path = Path(path_string)
    if not path.exists():
        print(f"Path does not exist: {path}")
        return
    if not path.is_dir():
        print(f"Not a directory: {path}")
        return

    print("Directories:")
    for name in os.listdir(path):
        candidate = path / name
        if candidate.is_dir():
            print(candidate)

    print("\nFiles:")
    for name in os.listdir(path):
        candidate = path / name
        if candidate.is_file():
            print(candidate)

    print("\nAll entries recursively:")
    for candidate in path.rglob("*"):
        print(candidate)

if __name__ == "__main__":
    entered = input("Directory path (default: current directory): ").strip()
    list_path(entered or ".")
