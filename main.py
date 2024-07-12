import tkinter as tk
from tkinter import ttk
import hashlib

def hash_md5():
    text = entry.get()
    result = hashlib.md5(text.encode()).hexdigest()
    result_label.config(text=result)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_label.cget("text"))

root = tk.Tk()
root.title("OgMD5")
root.geometry("400x250")
root.configure(bg='black')
root.attributes('-alpha', 0.9)

entry = ttk.Entry(root, font=('Arial', 14))
entry.pack(pady=10)

hash_button = tk.Button(root, text="Hashle", command=hash_md5, bg='red', fg='white')
hash_button.pack(pady=10)

result_label = ttk.Label(root, text="", font=('Arial', 14), background='black', foreground='white')
result_label.pack(pady=10)

copy_button = tk.Button(root, text="Kopyala", command=copy_to_clipboard, bg='red', fg='white')
copy_button.pack(pady=10)

root.mainloop()
