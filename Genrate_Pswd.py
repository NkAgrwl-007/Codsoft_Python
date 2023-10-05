import tkinter as tk
import secrets
import string

alphabet = string.ascii_letters + string.digits + string.punctuation
root = tk.Tk()
root.title("Password Generator")

class PasswordGenerator(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.password_length = tk.IntVar( )
        self.password_entry = tk.Entry(self, textvariable=self.password_length )
        self.password_entry.pack()

        self.generate_password_button = tk.Button(self, text="Generate Password", command=self.generate_password ,bg="#8B7D6B")
        self.generate_password_button.pack()
        
        self.password_label = tk.Label(self, text="\nGenerated Password:" )
        self.password_label.pack()

        self.password_text = tk.Text(self, height=2, width=25)
        self.password_text.pack()

    def generate_password(self):
        password = ""
        for i in range(self.password_length.get()):
            password += secrets.choice(alphabet)

        self.password_text.delete(1.0, tk.END)
        self.password_text.insert(1.0, password)

if __name__ == "__main__":
    password_generator = PasswordGenerator(root)
    password_generator.pack()

    root.geometry("250x200")
    root.mainloop()
