from tkinter import *
from tkinter import ttk
import string
import random
import pyperclip  # Import the 'pyperclip' module for clipboard functionality

letters = string.ascii_letters
symbols = "()!@#&,.%_+-"
digits = string.digits
characters = symbols + letters + digits

root = Tk()
root.title("Password Generator")
root.geometry("300x200")
root.resizable(0, 0)

password = StringVar()
length = IntVar()


# Function to generate a random password and copy it to the clipboard
def generate_password():
    generated_password = "".join(random.sample(characters, length.get()))
    password.set(generated_password)
    pyperclip.copy(generated_password)  # Copy the password to the clipboard


pass_display = ttk.Entry(
    root,
    textvariable=password,
    font=("roboto medium", 10),
)
pass_display.pack(pady=5, ipadx=10)
pass_label = ttk.Label(root, text="Enter desired length")
pass_label.pack()

length_entry = ttk.Entry(
    root, textvariable=length, width=3, font=("Helvetica", 10, "bold")
)
length_entry.pack()

gen_button = ttk.Button(root, text="Generate", command=generate_password)
gen_button.pack(pady=10)

# Button to copy the generated password to the clipboard
copy_button = ttk.Button(
    root, text="Copy to Clipboard", command=lambda: pyperclip.copy(password.get())
)
copy_button.pack()

quit_button = ttk.Button(root, text="Exit", command=root.destroy)
quit_button.pack(anchor="ne", pady=19,)

root.mainloop()
