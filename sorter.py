import os
import shutil
import tkinter as tk
from tkinter import filedialog, Label, Button


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("427x140")
        self.root.title("File Sorter")
        self.root.grid_columnconfigure(0, weight = 1)

        self.num_sorted = None
        self.num_untouched = None

        self.empty_label = Label(self.root, text = "")
        self.select_file_b = Button(self.root, text = "Select Directory", command = self.select_directory)
        self.selected_file_str = Label(self.root, text = "")
        self.sorted_str = Label(self.root, text = f" Number of files sorted: 0", font = ("Verdana", 12))
        self.untouched_str = Label(self.root, text = f" Number of files untouched: 0", font = ("Verdana", 12))
        self.untouched_desc = Label(self.root, text = "Files may be untouched due to name duplicates.",
                                    font = ("Verdana", 8))

    def main(self):
        position_right = int(self.root.winfo_screenwidth()/2 - 214)
        position_down = int(self.root.winfo_screenheight()/2 - 70)
        self.root.geometry("+{}+{}".format(position_right, position_down))

        self.display_window()
        self.root.mainloop()

    def display_window(self):
        self.sorted_str.grid(row = 1)
        self.untouched_str.grid(row = 2, pady = 1)
        self.untouched_desc.grid(row = 3)
        self.empty_label.grid(row = 4)
        self.selected_file_str.grid(row = 5)
        self.select_file_b.grid(row = 6)

    def select_directory(self):
        self.root.withdraw()
        self.root.directory = filedialog.askdirectory()

        if self.root.directory != "":
            self.num_sorted = 0
            self.num_untouched = 0

            self.create_directories(self.root.directory)

            selected_file_str = Label(self.root, text = self.root.directory)
            selected_file_str.grid(row = 5)

            self.sort_files()

        self.root.deiconify()

    # noinspection PyMethodMayBeStatic
    def sort_files(self):
        for root, dirs, files in os.walk(self.root.directory):
            dirs.clear()

            for file in files:
                file_path = os.path.join(root, file)
                _, file_ext = os.path.splitext(file)
                file_ext = file_ext.lower()

                if file_ext == ".exe" or file_ext == ".msi":
                    destination = os.path.join(os.path.join(self.root.directory, "Applications"), file)
                    if not os.path.exists(destination):
                        shutil.move(file_path, destination)
                        self.num_sorted += 1
                    else:
                        self.num_untouched += 1

                elif file_ext == ".mp3" or file_ext == ".wav" or file_ext == ".m4a":
                    destination = os.path.join(os.path.join(self.root.directory, "Audio"), file)
                    if not os.path.exists(destination):
                        shutil.move(file_path, destination)
                        self.num_sorted += 1
                    else:
                        self.num_untouched += 1

                elif file_ext == ".jpg" or file_ext == ".png" or file_ext == ".gif" or file_ext == ".heic":
                    destination = os.path.join(os.path.join(self.root.directory, "Images"), file)
                    if not os.path.exists(destination):
                        shutil.move(file_path, destination)
                        self.num_sorted += 1
                    else:
                        self.num_untouched += 1

                elif file_ext == ".docx":
                    destination = os.path.join(os.path.join(self.root.directory, "Documents"), file)
                    if not os.path.exists(destination):
                        shutil.move(file_path, destination)
                        self.num_sorted += 1
                    else:
                        self.num_untouched += 1

                elif file_ext == ".pdf":
                    destination = os.path.join(os.path.join(self.root.directory, "PDFs"), file)
                    if not os.path.exists(destination):
                        shutil.move(file_path, destination)
                        self.num_sorted += 1
                    else:
                        self.num_untouched += 1

                elif file_ext == ".zip":
                    destination = os.path.join(os.path.join(self.root.directory, "Images"), file)
                    if not os.path.exists(destination):
                        shutil.move(file_path, destination)
                        self.num_sorted += 1
                    else:
                        self.num_untouched += 1

                else:
                    destination = os.path.join(os.path.join(self.root.directory, "Miscellaneous"), file)
                    if not os.path.exists(destination):
                        shutil.move(file_path, destination)
                        self.num_sorted += 1
                    else:
                        self.num_untouched += 1
        self.update()

    def create_directories(self, base):
        self.create_directory_helper(base, "Applications")
        self.create_directory_helper(base, "Audio")
        self.create_directory_helper(base, "Images")
        self.create_directory_helper(base, "Documents")
        self.create_directory_helper(base, "PDFs")
        self.create_directory_helper(base, "Zips")
        self.create_directory_helper(base, "Miscellaneous")

    # noinspection PyMethodMayBeStatic
    def create_directory_helper(self, base, directory):
        if not os.path.exists(os.path.join(base, directory)):
            os.mkdir(os.path.join(base, directory))

    def update(self):
        self.sorted_str = Label(self.root, text = f" Number of files sorted: {self.num_sorted}", font = ("Verdana", 12))
        self.untouched_str = Label(self.root, text = f" Number of files untouched: {self.num_untouched}",
                                   font = ("Verdana", 12))
        self.display_window()


def main():
    App().main()


if __name__ == "__main__":
    main()
