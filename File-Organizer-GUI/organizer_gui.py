import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def organize_files(path):
    folders = {
        "Images": [".jpg", ".png", ".jpeg"],
        "PDF": [".pdf"],
        "Text": [".txt"],
        "Music": [".mp3"],
        "Videos": [".mp4"]
    }

    moved_count = 0

    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            for folder, extensions in folders.items():
                if file.lower().endswith(tuple(extensions)):
                    folder_path = os.path.join(path, folder)

                    os.makedirs(folder_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(folder_path, file))

                    moved_count += 1
                    break

    return moved_count

def select_folder():
    folder = filedialog.askdirectory()
    path_entry.delete(0, tk.END)
    path_entry.insert(0, folder)

def start_organizing():
    path = path_entry.get()

    if not os.path.exists(path):
        messagebox.showerror("Error", "Invalid folder path!")
        return

    moved = organize_files(path)
    messagebox.showinfo("Success", f"{moved} files organized successfully!")

# GUI Setup
root = tk.Tk()
root.title("File Organizer")
root.geometry("400x200")

# Label
label = tk.Label(root, text="Select Folder to Organize", font=("Arial", 12))
label.pack(pady=10)

# Entry
path_entry = tk.Entry(root, width=40)
path_entry.pack(pady=5)

# Browse Button
browse_btn = tk.Button(root, text="Browse", command=select_folder)
browse_btn.pack(pady=5)

# Organize Button
organize_btn = tk.Button(root, text="Organize Files", command=start_organizing)
organize_btn.pack(pady=10)

# Run GUI
root.mainloop()