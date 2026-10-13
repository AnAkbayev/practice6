from pathlib import Path
import os

root = Path("practice_data")
nested = root / "documents" / "reports"
nested.mkdir(parents=True, exist_ok=True)
(nested / "report.txt").write_text("Sample report\n", encoding="utf-8")
(root / "notes.txt").write_text("Some notes\n", encoding="utf-8")

print("Current working directory:", os.getcwd())
print("Items in practice_data:", os.listdir(root))

print("\nDirectories only:")
for item in root.iterdir():
    if item.is_dir():
        print(item)

print("\nFiles only (directly inside practice_data):")
for item in root.iterdir():
    if item.is_file():
        print(item)

print("\nAll files and directories recursively:")
for item in root.rglob("*"):
    print("Directory:" if item.is_dir() else "File:", item)

print("\nFiles with .txt extension:")
for item in root.rglob("*.txt"):
    print(item)
