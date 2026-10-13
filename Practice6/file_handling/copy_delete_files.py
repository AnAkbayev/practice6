from pathlib import Path
import shutil

source = Path("source.txt")
backup = Path("source_backup.txt")
copy_path = Path("source_copy.txt")

source.write_text("Example content for copying and backup.\n", encoding="utf-8")

# Copy a file and create a backup.
shutil.copy2(source, copy_path)
shutil.copy2(source, backup)
print(f"Copied {source} to {copy_path} and backed it up to {backup}")

# Safe deletion: check that the target exists and is a file.
if copy_path.exists() and copy_path.is_file():
    copy_path.unlink()
    print(f"Deleted {copy_path}")
else:
    print(f"Not deleting: {copy_path} does not exist or is not a file.")
