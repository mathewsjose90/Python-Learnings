import os
from pathlib import Path
SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

def pickdirectory(value):
    for dir_name in SUBDIRECTORIES:
        if value in SUBDIRECTORIES[dir_name]:
            return dir_name
    return 'MISC'

print(pickdirectory('.pdf'))
os.chdir('Ex_Files_Python_Automation/Exercise Files/OrganizeMe/')
print(os.getcwd())

def organizedir():
    for item in os.scandir():
        if item.is_dir():
            continue
        filepath=Path(item)
        file_type=filepath.suffix.lower()
        dest_dir=pickdirectory(file_type)
        dest_dir_path=Path(dest_dir)
        if not dest_dir_path.is_dir():
            dest_dir_path.mkdir()
        filepath.rename(dest_dir_path.joinpath(filepath))

organizedir()