from pathlib import Path

def inspect_path(path_string: str) -> None:
    path = Path(path_string)
    if path.exists():
        print("Path exists.")
        print("Filename:", path.name)
        print("Directory portion:", path.parent)
    else:
        print("Path does not exist.")

if __name__ == "__main__":
    entered = input("Enter a path: ").strip()
    if entered:
        inspect_path(entered)
