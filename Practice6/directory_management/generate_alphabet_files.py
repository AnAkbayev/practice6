from pathlib import Path
import string

output_dir = Path("alphabet_files")
output_dir.mkdir(exist_ok=True)

for letter in string.ascii_uppercase:
    file_path = output_dir / f"{letter}.txt"
    file_path.write_text(f"This is {letter}.txt\n", encoding="utf-8")

print(f"Generated {len(string.ascii_uppercase)} files in {output_dir.resolve()}")
