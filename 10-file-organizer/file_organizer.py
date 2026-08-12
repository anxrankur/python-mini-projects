import os
import shutil

folder = input("Enter folder path to organize: ")

if not os.path.isdir(folder):
    print("Folder not found!")
else:
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
        "Documents": [".pdf", ".doc", ".docx", ".txt"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov"],
        "Audio": [".mp3", ".wav", ".aac"],
        "Archives": [".zip", ".rar", ".7z"]
    }

    for category in categories:
        os.makedirs(os.path.join(folder, category), exist_ok=True)

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        if not os.path.isfile(file_path):
            continue

        extension = os.path.splitext(filename)[1].lower()
        moved = False

        for category, extensions in categories.items():
            if extension in extensions:
                destination = os.path.join(folder, category, filename)
                shutil.move(file_path, destination)
                print(f"Moved: {filename} → {category}")
                moved = True
                break

        if not moved:
            print(f"Skipped: {filename}")

    print("\n✅ Files organized successfully!")
