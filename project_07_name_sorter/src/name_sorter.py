from pathlib import Path

CURRENT_FILE = Path(__file__).resolve()
PARENT_DIR = CURRENT_FILE.parent.parent
file = PARENT_DIR / "data" / "names.txt"

# Read the content of the file and split it into lines
with open(file, "r") as f:
    lines = f.read().splitlines()

# Split each line into names and clean them by stripping unwanted characters
names = []
for line in lines:
    names.extend(line.split())
cleaned_names = [name.strip("., ") for name in names]

# Sort the cleaned names and write them back to the file
with open(file, "w") as f:
    f.write("\n".join(sorted(cleaned_names)))
