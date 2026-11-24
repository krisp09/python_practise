import os
import shutil

file_name ="1.jpg"
extension = os.path.splitext(file_name)[1].lower()

print(extension)


files=["1.jpg", "2.png", "3.pdf", "4.mp3", "5.docx", "6.avi", "7.txt", "8.flac", "9.mov", "10.xlsx"]

for file in files:
    extension = os.path.splitext(file)[1].lower()
    if extension in [".jpg", ".jpeg", ".png", ".gif", ".bmp"]:
        print(f"{file} is an Image file.")
    elif extension in [".pdf", ".docx", ".txt", ".xlsx"]:
        print(f"{file} is a Document file.")
    elif extension in [".mp4", ".avi", ".mov", ".mkv"]:
        print(f"{file} is a Video file.")
    elif extension in [".mp3", ".wav", ".flac"]:
        print(f"{file} is a Music file.")
    else:
        print(f"{file} is of Other type.")