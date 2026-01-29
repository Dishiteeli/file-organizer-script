import os
import shutil

audio = [".mp3", ".wma", ".aac"]
video = [".mp4", ".wmv", ".avi"]
docs = [".docx", ".pdf", ".xlsx", ".xls"]
software = [".exe", ".apk"]
zips = [".zip", ".rar"]

path = r"C:\Users\punda\Videos"

folders = {
    "audio": audio,
    "video": video,
    "docs": docs,
    "software": software,
    "zips": zips,
    "unknown": []
}

# Create folders safely
for folder in folders:
    os.makedirs(os.path.join(path, folder), exist_ok=True)

for file in os.listdir(path):
    full_path = os.path.join(path, file)

    # Skip folders
    if os.path.isdir(full_path):
        continue

    ext = os.path.splitext(file)[1].lower()

    moved = False
    for folder, extensions in folders.items():
        if ext in extensions:
            shutil.move(full_path, os.path.join(path, folder, file))
            moved = True
            break

    if not moved:
        shutil.move(full_path, os.path.join(path, "unknown", file))
