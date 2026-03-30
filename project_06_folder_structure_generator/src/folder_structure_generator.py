from pathlib import Path

SOURCE_FILE = Path(__file__).resolve()
SOURCE_DIR = SOURCE_FILE.parent.parent
DATA_DIR = SOURCE_DIR / "data"

d = {"movies": ["Lord of Rings",
                "Harry Potter",
                "Moon",
                "Forrest Gump"],
     "employees": ["Paul",
                   "Pierre",
                   "Marie"],
     "programming": ["variables",
                     "files",
                     "loops"]}

for key, values in d.items():
    key_dir = DATA_DIR / key
    key_dir.mkdir(parents=True, exist_ok=True)
    for value in values:
        val_dir = key_dir / value
        val_dir.mkdir(parents=True, exist_ok=True)
