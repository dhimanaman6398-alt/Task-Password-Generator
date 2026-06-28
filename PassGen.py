import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())

        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than 0")
            return

        characters = ""

        if lowercase_var.get():
            characters += string.ascii_lowercase

        if uppercase_var.get():
            characters += string.ascii_uppercase

        if numbers_var.get():
            characters += string.digits

        if symbols_var.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Select at least one character type")
            return

        password = ''.join(random.choice(characters) for _ in range(length))

        password_entry.config(state="normal")
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_entry.config(state="readonly")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.resizable(False, False)

title_label = tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

lowercase_var = tk.BooleanVar(value=True)
uppercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Lowercase (a-z)", variable=lowercase_var).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Include Uppercase (A-Z)", variable=uppercase_var).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Include Numbers (0-9)", variable=numbers_var).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Include Symbols (!@#$)", variable=symbols_var).pack(anchor="w", padx=50)

generate_btn = tk.Button(root, text="Generate Password", command=generate_password,
                         bg="green", fg="white", font=("Arial", 10, "bold"))
generate_btn.pack(pady=15)

output_label = tk.Label(root, text="Generated Password:")
output_label.pack()

password_entry = tk.Entry(root, width=35, justify="center", state="readonly")
password_entry.pack(pady=5)

root.mainloop()