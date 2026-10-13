from pathlib import Path

def count_lines(filename: str) -> int:
    path = Path(filename)
    with path.open("r", encoding="utf-8") as file:
        return sum(1 for _ in file)

if __name__ == "__main__":
    filename = input("Text file path: ").strip()
    try:
        print("Number of lines:", count_lines(filename))
    except FileNotFoundError:
        print("File not found.")
    except OSError as error:
        print("Could not read file:", error)
