import random
import string
import tkinter as tk
from tkinter import messagebox

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x600")
        self.root.title("Random Password Generator")

        self.label = tk.Label(root, text="Enter password length:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

    def generate_password(self):
        try:
            length = int(self.entry.get())
            if length <= 0:
                messagebox.showerror("Error", "Password length should be a positive integer.")
                return

            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            messagebox.showinfo("Generated Password", f"Your generated password:\n\n {password}")

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for password length.")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
