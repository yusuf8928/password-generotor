import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate a random password
def generate_password():
    password_length = int(length_entry.get())
    if password_length < 8:
        messagebox.showerror("Error", "Password length should be at least 8 characters.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Label and entry for password length
length_label = tk.Label(window, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()

# Button to generate password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

# Entry to display generated password
password_entry = tk.Entry(window)
password_entry.pack()

# Run the Tkinter main loop
window.mainloop()
