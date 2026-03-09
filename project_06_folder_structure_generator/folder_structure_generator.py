from pathlib import Path

SOURCE_FILE = Path(__file__).resolve()
SOURCE_DIR = SOURCE_FILE.parent

d = {"Films": ["Lord of Rings",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employees": ["Paul",
                   "Pierre",
                   "Marie"],
     "Programming": ["variables",
                     "files",
                     "loops"]}

for key, values in d.items():
    key_dir = SOURCE_DIR / key
    key_dir.mkdir(exist_ok=True)
    for value in values:
        val_dir = key_dir / value
        val_dir.mkdir(parents=True, exist_ok=True)
