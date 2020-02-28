import os
import shutil
import tkinter as tk
from tkinter import filedialog


def main():
    root = tk.Tk()
    root.withdraw()
    root.directory = filedialog.askdirectory()

    create_directories(root.directory)
    sort_files(root.directory)

    root.mainloop()


def sort_files(directory):
    for root, dirs, files in os.walk(directory):
        dirs.clear()

        for file in files:
            file_path = os.path.join(root, file)
            _, file_ext = os.path.splitext(file)
            file_ext = file_ext.lower()

            if file_ext == ".exe" or file_ext == ".msi":
                destination = os.path.join(os.path.join(directory, "Applications"), file)
                if not os.path.exists(destination):
                    shutil.move(file_path, destination)

            elif file_ext == ".mp3" or file_ext == ".wav" or file_ext == ".m4a":
                destination = os.path.join(os.path.join(directory, "Audio"), file)
                if not os.path.exists(destination):
                    shutil.move(file_path, destination)

            elif file_ext == ".jpg" or file_ext == ".png" or file_ext == ".gif" or file_ext == ".heic":
                destination = os.path.join(os.path.join(directory, "Images"), file)
                if not os.path.exists(destination):
                    shutil.move(file_path, destination)

            elif file_ext == ".docx":
                destination = os.path.join(os.path.join(directory, "Documents"), file)
                if not os.path.exists(destination):
                    shutil.move(file_path, destination)

            elif file_ext == ".pdf":
                destination = os.path.join(os.path.join(directory, "PDFs"), file)
                if not os.path.exists(destination):
                    shutil.move(file_path, destination)

            elif file_ext == ".zip":
                destination = os.path.join(os.path.join(directory, "Images"), file)
                if not os.path.exists(destination):
                    shutil.move(file_path, destination)

            else:
                destination = os.path.join(os.path.join(directory, "Miscellaneous"), file)
                if not os.path.exists(destination):
                    shutil.move(file_path, destination)


def create_directories(root):
    create_directory_helper(root, "Applications")
    create_directory_helper(root, "Audio")
    create_directory_helper(root, "Images")
    create_directory_helper(root, "Documents")
    create_directory_helper(root, "PDFs")
    create_directory_helper(root, "Zips")
    create_directory_helper(root, "Miscellaneous")


def create_directory_helper(root, directory):
    if not os.path.exists(os.path.join(root, directory)):
        os.mkdir(os.path.join(root, directory))


if __name__ == "__main__":
    main()
