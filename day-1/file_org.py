import os
import shutil

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Music": [".mp3", ".wav", ".flac"]
}

def  get_category(file_name):
    extension = os.path.splitext(file_name)[1].lower()
    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category
            print (category)
        
    return "Other"
