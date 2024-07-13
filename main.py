import json
import os
import tkinter as tk
from tkinter import messagebox

def initialize_count(file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            json.dump({'count': 0}, file)
        return 0
    else:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data.get('count', 0)

def update_count(file_path, count):
    with open(file_path, 'w') as file:
        json.dump({'count': count}, file)

def show_reminder(count, max_glasses):
    root = tk.Tk()
    root.withdraw()

    dialog = tk.Toplevel(root)
    dialog.title("Water Reminder")

    message = tk.Label(dialog, text="Go and drink a glass of water :D")
    message.pack()

    count_label = tk.Label(dialog, text=f"Glasses consumed: {count}")
    count_label.pack()

    def on_yes():
        nonlocal count
        count += 1
        count_label.config(text=f"Glasses consumed: {count}")

    def on_no():
        nonlocal count
        if count > 0:
            count -= 1
            count_label.config(text=f"Glasses consumed: {count}")

    def on_done():
        root.withdraw()
        root.quit()

    yes_button = tk.Button(dialog, text="Yes", command=on_yes)
    yes_button.pack(side=tk.LEFT, padx=10)

    no_button = tk.Button(dialog, text="No", command=on_no)
    no_button.pack(side=tk.LEFT, padx=10)

    done_button = tk.Button(dialog, text="Done", command=on_done)
    done_button.pack(side=tk.LEFT, padx=10)

    dialog.protocol("WM_DELETE_WINDOW", on_done)
    root.mainloop()

    return count

def main():
    file_path = r'C:\Users\Public\Desktop\Water Count\water_count.json'
    max_glasses = 8

    count = initialize_count(file_path)

    if not os.path.exists(icon_path):
        create_placeholder_icon(icon_path)


    count = show_reminder(count, max_glasses)
    update_count(file_path, count)
    print(f"Glasses of water drunk: {count}")

    print("Maximum glasses reached. Terminating the program.")

if __name__ == "__main__":
    main()
