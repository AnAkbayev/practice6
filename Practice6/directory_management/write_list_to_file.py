from pathlib import Path

items = ["apple", "banana", "cherry", "orange"]
output = Path("fruits.txt")

with output.open("w", encoding="utf-8") as file:
    file.writelines(item + "\n" for item in items)

print(f"Wrote {len(items)} items to {output}")
print(output.read_text(encoding="utf-8"))
