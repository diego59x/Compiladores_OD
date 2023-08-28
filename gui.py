import tkinter as tk
from tkinter import ttk
from tkinter import font
import subprocess
import os

def save_to_file():
    content = entry.get("1.0", tk.END).strip()

    if not content:
        display_error("Error: por favor, no envíe archivos vacíos.")
        return

    selected_file = file_selector.get()
    with open(f'./tests/{selected_file}', 'w') as file:
        file.write(content)

    try:
        result = subprocess.check_output(['python', 'main.py', selected_file], text=True)
        display_error(result.strip())
    except subprocess.CalledProcessError as e:
        display_error(f"Error: {e.output}")

def clear_input():
    entry.delete("1.0", tk.END)
    file_selector.set("New")
    clear_error()

def display_error(message):
    error_display.configure(state=tk.NORMAL)
    error_display.delete("1.0", tk.END)
    error_display.insert(tk.END, "Console\n", "label")
    
    if message.startswith("Success:"):
        error_display.insert(tk.END, message, "success")
    else:
        error_display.insert(tk.END, message, "error")

    error_display.configure(state=tk.DISABLED)

def clear_error():
    error_display.configure(state=tk.NORMAL)
    error_display.delete("1.0", tk.END)
    error_display.configure(state=tk.DISABLED)

def on_hover(event):
    if event.widget["text"] == "Quit":
        event.widget.configure(bg="red")
    elif event.widget["text"] == "Compile":
        event.widget.configure(bg="green")
    else:
        event.widget.configure(bg="#3a3c3f")

def on_leave(event):
    event.widget.configure(bg="#1e1f1c")

def on_key_release(event):
    if event.char == '(':
        entry.insert(tk.INSERT, ')')

def load_selected_file(event):
    selected_file = file_selector.get()
    if selected_file == "New":
        entry.delete("1.0", tk.END)
        return
    filepath = os.path.join('tests', selected_file)
    with open(filepath, 'r') as file:
        content = file.read()
    entry.delete("1.0", tk.END)
    entry.insert(tk.END, content)

root = tk.Tk()
root.title("Text Saver")
root.state('zoomed')
root.configure(bg="#272822")

default_font = font.nametofont("TkDefaultFont")
default_font.configure(size=14)
big_font = font.Font(size=18)
label_font = font.Font(size=12)

# Main Editor Label and Text Box
tk.Label(root, text="Editor", bg="#272822", fg="white", font=label_font).pack(pady=(0,2), anchor="nw")
entry = tk.Text(root, wrap=tk.WORD, bg="#272822", fg="white", font=default_font, insertbackground="white")
entry.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, anchor="nw", padx=(10,5))
entry.bind("<KeyRelease>", on_key_release)

# Top Input Label and Text Box
# tk.Label(root, text="Input", bg="#272822", fg="white", font=label_font).pack(pady=(0,2), anchor="nw", side=tk.TOP)
top_entry = tk.Text(root, wrap=tk.WORD, bg="#272822", fg="white", font=default_font, height=10, insertbackground="white")
top_entry.pack(fill=tk.X, anchor="nw", padx=(5,10))

# Button definitions
for btn_text, btn_command in [("Compile", save_to_file), ("Clear", clear_input), ("Quit", root.quit)]:
    btn = tk.Button(root, text=btn_text, command=btn_command, bg="#1e1f1c", fg="white", font=big_font)
    btn.pack(fill=tk.X, padx=(5,10), pady=(2,2))
    btn.bind("<Enter>", on_hover)
    btn.bind("<Leave>", on_leave)

# Combobox to select files
files_in_directory = ["New"] + [f for f in os.listdir('tests') if os.path.isfile(os.path.join('tests', f))]
file_selector_label = tk.Label(root, text="Selecciona un archivo:", bg="#272822", fg="white", font=label_font)
file_selector_label.pack(pady=(10,2), anchor="nw", side=tk.TOP)
file_selector = ttk.Combobox(root, values=files_in_directory)
file_selector.pack(fill=tk.X, padx=(5,10))
file_selector.bind("<<ComboboxSelected>>", load_selected_file)

# Console/Error Display Text Box
error_display = tk.Text(root, wrap=tk.WORD, bg="#272822", fg="white", font=default_font, height=5, insertbackground="white")
error_display.pack(fill=tk.BOTH, padx=(10,10), pady=(5,10), expand=True)
error_display.tag_configure("error", foreground="red")
error_display.tag_configure("success", foreground="green")
error_display.tag_configure("label", foreground="white")
error_display.insert(tk.END, "Console\n", "label")
error_display.configure(state=tk.DISABLED)

root.mainloop()
