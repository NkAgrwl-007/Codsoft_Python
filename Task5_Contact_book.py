import tkinter as tk
from tkinter import font

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        return self.contacts

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
            return True
        return False

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    new_contact = Contact(name, phone, email, address)
    contact_book.add_contact(new_contact)

    feedback_label.config(text="Contact added successfully!", fg="green")
    view_contacts()

def view_contacts():
    contacts = contact_book.view_contacts()
    contact_listbox.delete(0, tk.END)
    for i, contact in enumerate(contacts, start=1):
        contact_info = f"Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}"
        contact_listbox.insert(tk.END, contact_info)

    count_label.config(text=f"Total Contacts: {len(contacts)}")

def delete_contact():
    selected_index = contact_listbox.curselection()
    if selected_index:
        success = contact_book.delete_contact(selected_index[0])
        if success:
            view_contacts()
            feedback_label.config(text="Contact deleted successfully!", fg="green")
        else:
            feedback_label.config(text="Invalid contact index.", fg="red")

contact_book = ContactBook()

root = tk.Tk()
root.title("Contact Management System")
root.geometry("600x400")
root.configure(bg='#F0F0F0')

bold_font = font.Font(weight='bold')
stylish_font = font.Font(family='Helvetica', size=14, weight='bold', slant='italic')

heading_label = tk.Label(root, text="Contact Book", font=('Helvetica', 20, 'bold'), bg='#F0F0F0')
heading_label.pack()

name_label = tk.Label(root, text="Name:", font=stylish_font, bg='#F0F0F0')
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

phone_label = tk.Label(root, text="Phone:", font=stylish_font, bg='#F0F0F0')
phone_label.pack()

phone_entry = tk.Entry(root)
phone_entry.pack()

email_label = tk.Label(root, text="Email:", font=stylish_font, bg='#F0F0F0')
email_label.pack()

email_entry = tk.Entry(root)
email_entry.pack()

address_label = tk.Label(root, text="Address:", font=stylish_font, bg='#F0F0F0')
address_label.pack()

address_entry = tk.Entry(root)
address_entry.pack()

add_button = tk.Button(root, text="Add Contact", command=add_contact, bg='#4CAF50', fg='white', font=bold_font)
add_button.pack()

view_button = tk.Button(root, text="View Contacts", command=view_contacts, bg='#2196F3', fg='white', font=bold_font)
view_button.pack()

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact, bg='#FF5722', fg='white', font=bold_font)
delete_button.pack()

feedback_label = tk.Label(root, text="", fg="green", bg='#F0F0F0')
feedback_label.pack()

count_label = tk.Label(root, text="Total Contacts: 0", font=stylish_font, bg='#F0F0F0')
count_label.pack()

contact_listbox = tk.Listbox(root, width=50, height=10)
contact_listbox.pack()

root.mainloop()
