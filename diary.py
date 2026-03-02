import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

# -------------------------------
# MODULE 2 – FILE HANDLING & DATE-TIME
# -------------------------------

def save_to_file(entry_text, file_path):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("daily_diary.txt", "a", encoding="utf-8") as file:
        file.write(f"Date-Time: {current_time}\n")
        file.write(f"Entry:\n{entry_text}\n")
        if file_path:
            file.write(f"Attached File: {file_path}\n")
        file.write("\n--------------------------\n")


# -------------------------------
# MODULE 1 – INPUT INTERFACE & ENTRY CAPTURE
# -------------------------------

def save_entry():
    entry_text = diary_text.get("1.0", tk.END).strip()

    if not entry_text:
        messagebox.showerror("Error", "Diary entry cannot be empty!")
        return

    save_to_file(entry_text, selected_file.get())

    messagebox.showinfo("Success", "Diary Saved Successfully!")
    diary_text.delete("1.0", tk.END)
    selected_file.set("")

def attach_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        selected_file.set(file_path)


# -------------------------------
# GUI DESIGN
# -------------------------------

root = tk.Tk()
root.title("Daily Digital Diary")
root.geometry("500x500")

tk.Label(root, text="Daily Digital Diary", font=("Arial", 16)).pack(pady=10)

diary_text = tk.Text(root, height=15, width=55)
diary_text.pack()

selected_file = tk.StringVar()

tk.Button(root, text="Attach File", command=attach_file).pack(pady=5)
tk.Label(root, textvariable=selected_file, wraplength=400).pack()

tk.Button(root, text="Save Entry", command=save_entry).pack(pady=10)

root.mainloop()
