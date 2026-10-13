from pathlib import Path
import shutil

root = Path("move_demo")
source_dir = root / "source"
destination_dir = root / "destination"
source_dir.mkdir(parents=True, exist_ok=True)
destination_dir.mkdir(parents=True, exist_ok=True)

source_file = source_dir / "example.txt"
source_file.write_text("File to move or copy.\n", encoding="utf-8")

# Copy the file to the destination directory.
copied_file = destination_dir / source_file.name
shutil.copy2(source_file, copied_file)
print(f"Copied to: {copied_file}")

# Move another file example (shutil.move returns the destination path).
move_source = source_dir / "move_me.txt"
move_source.write_text("This file will be moved.\n", encoding="utf-8")
moved_to = shutil.move(str(move_source), str(destination_dir / move_source.name))
print(f"Moved to: {moved_to}")
