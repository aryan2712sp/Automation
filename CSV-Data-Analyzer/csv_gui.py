import tkinter as tk
from tkinter import filedialog, messagebox
import csv

data = []

def load_csv():
    global data
    file = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    
    if not file:
        return

    data.clear()

    try:
        with open(file, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                # Convert numeric values
                try:
                    data.append(float(row[0]))
                except:
                    pass

        messagebox.showinfo("Success", "CSV Loaded Successfully!")

    except:
        messagebox.showerror("Error", "Failed to load file")

def show_data():
    if not data:
        messagebox.showwarning("Warning", "No data loaded!")
        return

    messagebox.showinfo("Data", str(data))

def calculate_average():
    if not data:
        messagebox.showwarning("Warning", "No data loaded!")
        return

    avg = sum(data) / len(data)
    messagebox.showinfo("Average", f"Average = {avg}")

def find_max():
    if not data:
        messagebox.showwarning("Warning", "No data loaded!")
        return

    messagebox.showinfo("Maximum", f"Max = {max(data)}")

def find_min():
    if not data:
        messagebox.showwarning("Warning", "No data loaded!")
        return

    messagebox.showinfo("Minimum", f"Min = {min(data)}")

# GUI Setup
root = tk.Tk()
root.title("CSV Data Analyzer")
root.geometry("350x300")

tk.Label(root, text="CSV Data Analyzer", font=("Arial", 14)).pack(pady=10)

tk.Button(root, text="Load CSV", command=load_csv).pack(pady=5)
tk.Button(root, text="Show Data", command=show_data).pack(pady=5)
tk.Button(root, text="Average", command=calculate_average).pack(pady=5)
tk.Button(root, text="Maximum", command=find_max).pack(pady=5)
tk.Button(root, text="Minimum", command=find_min).pack(pady=5)

root.mainloop()