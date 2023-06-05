# App opens window with text field and during typing it updates number of characters typed in field by user

import tkinter as tk

def update_character_count(*args):
    user_input = entry.get()
    length = len(user_input)
    character_count.set(f'"{user_input}" has {length} characters')

root = tk.Tk()
root.title("Character Count")

entry = tk.Entry(root)
entry.grid(row=0, column=0, padx=15, pady=15)

entry.bind("<KeyRelease>", update_character_count)

character_count = tk.StringVar()

label = tk.Label(root, textvariable=character_count)
label.grid(row=1, column=0, padx=15, pady=15)

root.mainloop()