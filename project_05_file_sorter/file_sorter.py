from pathlib import Path

categories = {
    "Images": [".jpg", ".jpeg", ".bmp", ".png"],
    "Videos": [".gif", ".mp4", ".avi"],
    "Documents": [".pdf", ".txt", ".pptx", ".csv",
                  ".xls", ".odp", ".pages", ".xlsx",
                  ".docx"],
    "Music": [".mp3", ".wav", ".flac"]
}

# Create dictionnary extension -> category
d = {ext: category for category, exts in categories.items() for ext in exts}

dir_to_sort = Path.home() / "Downloads"

# Get the files in a list
files = [f for f in dir_to_sort.iterdir() if f.is_file()]

# Sorting the files
for f in files:
    output_dir = dir_to_sort / d.get(f.suffix.lower(), "Others")
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name)
