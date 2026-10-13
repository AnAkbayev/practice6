from pathlib import Path
import os
import shutil

workspace = Path("utility_demo")
workspace.mkdir(exist_ok=True)
sample = workspace / "sample.txt"
sample.write_text("Utilities example\n", encoding="utf-8")

print("Current directory:", os.getcwd())
print("Directory contents:", os.listdir(workspace))
print("Path exists:", sample.exists())
print("File size:", sample.stat().st_size, "bytes")

backup = workspace / "sample_backup.txt"
shutil.copy2(sample, backup)
print("Backup created:", backup.exists())

# Safe directory removal example: only remove an empty directory.
empty_dir = workspace / "empty_directory"
empty_dir.mkdir(exist_ok=True)
empty_dir.rmdir()
print("Removed empty directory:", not empty_dir.exists())
