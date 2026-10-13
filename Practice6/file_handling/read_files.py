from pathlib import Path

# Create a sample file if it doesn't exist yet.
sample_file = Path("sample.txt")
if not sample_file.exists():
    sample_file.write_text("First line\nSecond line\nThird line\n", encoding="utf-8")

# read()
with sample_file.open("r", encoding="utf-8") as file:
    print("read():")
    print(file.read())

# readline()
with sample_file.open("r", encoding="utf-8") as file:
    print("readline():", file.readline().rstrip())

# readlines()
with sample_file.open("r", encoding="utf-8") as file:
    print("readlines():", file.readlines())
