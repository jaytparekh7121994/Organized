import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf', '.rtf', '.txt', '.docx', '.ppt', '.pptx'],
    "AUDIO": ['.m4a', '.m4b', '.mp3'],
    "IMAGES": ['.jpeg', '.jpg', '.png'],
    "VIDEOS": ['.mp4', '.mov', '.avi'],
    "ZIP": ['.zip', '.tgz', '.gz', '.rar'],
    "EXE": ['.exe'],
    "EXCEL SHEET": ['.xlsx', '.xls']
}


def pickDirectory(value):
    """ Picks a directory from SUBDIRECTORIES based on Suffix or file
    extension"""
    for category, extension_list in SUBDIRECTORIES.items():
        for extension in extension_list:
            if value == extension:
                return category
    return 'MISC'


def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filepath = Path(item)
        print(filepath)
        filetype = filepath.suffix.lower()
        directory = pickDirectory(filetype)
        directoryPath = Path(directory)
        if directoryPath.is_dir() is not True:
            directoryPath.mkdir()
        filepath.rename(directoryPath.joinpath(filepath))


organizeDirectory()
