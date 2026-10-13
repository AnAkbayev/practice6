# Practice 6 — Python File Handling and Built-in Functions

This repository contains runnable examples for file handling, directory management, and Python built-in functions.

## Structure

```text
Practice6/
├── file_handling/
│   ├── read_files.py
│   ├── write_files.py
│   ├── copy_delete_files.py
│   └── file_modes.py
├── directory_management/
│   ├── create_list_dirs.py
│   ├── move_files.py
│   ├── path_access.py
│   ├── list_path_contents.py
│   ├── path_exists_parts.py
│   ├── count_lines.py
│   ├── write_list_to_file.py
│   ├── generate_alphabet_files.py
│   ├── copy_file_contents.py
│   └── delete_file_safely.py
├── builtin_functions/
│   ├── map_filter_reduce.py
│   ├── enumerate_zip_examples.py
│   ├── basic_builtins.py
│   └── os_shutil_pathlib_examples.py
└── README.md
```

## Requirements

- Python 3.9 or newer recommended.
- No third-party packages are required.

## How to run

Run each script from a terminal, for example:

```bash
python file_handling/read_files.py
python builtin_functions/map_filter_reduce.py
```

Some scripts create sample files and folders in the current working directory. Run them in a practice folder. `path_access.py`, `list_path_contents.py`, `path_exists_parts.py`, `count_lines.py`, and `delete_file_safely.py` ask for a path or filename. The delete script requires typing `YES` before removing a file.

## Topics covered

- File modes `r`, `w`, `a`, and `x`
- `read()`, `readline()`, `readlines()`, `write()`, and `writelines()`
- `with` context managers
- `os`, `shutil`, and `pathlib`
- Directory creation, listing, and safe removal
- Checking path existence and access
- Counting file lines, writing lists, copying files, and generating A.txt–Z.txt
- `len()`, `sum()`, `min()`, `max()`, `map()`, `filter()`, `reduce()`, `enumerate()`, `zip()`, `sorted()`, `type()`, and type conversions

## GitHub upload

From the directory that contains `Practice6/`:

```bash
git init
git add Practice6
git commit -m "Add Practice6 - file handling and built-in functions examples"
git branch -M main
git remote add origin YOUR_REPOSITORY_URL
git push -u origin main
```

If the repository is already initialized and connected to GitHub, use the commit and push commands from your assignment instructions.
