from pathlib import Path

output_file = Path("output.txt")

# "w" creates the file or overwrites its contents.
with output_file.open("w", encoding="utf-8") as file:
    file.write("Python file handling practice\n")
    file.write("This file was created using write().\n")

# "a" appends without replacing existing content.
with output_file.open("a", encoding="utf-8") as file:
    file.write("This line was appended.\n")

print(output_file.read_text(encoding="utf-8"))
