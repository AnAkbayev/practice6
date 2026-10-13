from pathlib import Path

path = Path("modes_demo.txt")

# "w": create or overwrite
with path.open("w", encoding="utf-8") as file:
    file.write("Created with mode w.\n")

# "a": append
with path.open("a", encoding="utf-8") as file:
    file.write("Added with mode a.\n")

# "r": read
with path.open("r", encoding="utf-8") as file:
    print(file.read())

# "x": create only if the file does not already exist
exclusive_path = Path("exclusive_demo.txt")
try:
    with exclusive_path.open("x", encoding="utf-8") as file:
        file.write("Created with mode x.\n")
    print(f"Created {exclusive_path}")
except FileExistsError:
    print(f"{exclusive_path} already exists; mode x will not overwrite it.")
