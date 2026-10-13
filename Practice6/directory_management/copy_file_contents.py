from pathlib import Path
import shutil

source = Path("source_text.txt")
destination = Path("destination_text.txt")

# Make a sample source file so the example can run immediately.
source.write_text("Line one\nLine two\nLine three\n", encoding="utf-8")

with source.open("r", encoding="utf-8") as source_file:
    with destination.open("w", encoding="utf-8") as destination_file:
        shutil.copyfileobj(source_file, destination_file)

print("Copied contents:")
print(destination.read_text(encoding="utf-8"))
