from pathlib import Path
from config import DOWNLOADS_FOLDER
from utils import FOLDERS

def organize():
  print(DOWNLOADS_FOLDER)

  for file in DOWNLOADS_FOLDER.iterdir():

    if file.is_dir() and file.suffix != ".app":
      continue

    extension = file.suffix.lower()

    folder = FOLDERS.get(extension)

    #print(f"{file.suffix} -> {folder}")
    if folder:
      destination = DOWNLOADS_FOLDER / folder
      destination.mkdir(exist_ok=True)
      file.rename(destination / file.name)

