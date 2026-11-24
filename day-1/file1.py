import os
import shutil

categories = {
    "Image": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Document": [".pdf", ".docx", ".txt", ".xlsx"],
    "Video": [".mp4", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".flac"]
}

def get_category(file_name):
    extension = os.path.splitext(file_name)[1].lower()
    for category, extensions in categories.items():
        if extension in extensions:
            return category
            print(f"{file_name} is a {category} file.")
    return "Other"


if __name__ == "__main__":
    
    get_category("1.jpg")  # Output: "Image"