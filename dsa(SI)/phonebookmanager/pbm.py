import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv
import os

class PhoneBookManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Phone Book Manager")
        
        self.contacts = {}
        self.file_path = r"C:\Users\Shubham\Downloads\contacts.csv"  # Updated file path here
        
        self.load_contacts()
        
        self.create_homepage()
        
    def create_homepage(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        self.title_label = ttk.Label(self.master, text="Welcome to Phonebook Manager", font=('Arial', 20))
        self.title_label.pack(pady=20)

        self.add_contact_button = ttk.Button(self.master, text="Add a New Contact", command=self.add_contact_page)
        self.add_contact_button.pack(pady=10, padx=20, fill='x')

        self.search_contact_button = ttk.Button(self.master, text="Search Contact", command=self.search_contact_page)
        self.search_contact_button.pack(pady=10, padx=20, fill='x')

        self.view_contacts_button = ttk.Button(self.master, text="View Contact List", command=self.view_contacts)
        self.view_contacts_button.pack(pady=10, padx=20, fill='x')

        self.delete_contact_button = ttk.Button(self.master, text="Delete Contact", command=self.delete_contact_page)
        self.delete_contact_button.pack(pady=10, padx=20, fill='x')
        
        self.update_contact_button = ttk.Button(self.master, text="Update Contact", command=self.update_contact_page)
        self.update_contact_button.pack(pady=10, padx=20, fill='x')

    def add_contact_page(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        self.title_label = ttk.Label(self.master, text="Add a New Contact", font=('Arial', 20))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)

        self.first_name_label = ttk.Label(self.master, text="First Name:")
        self.first_name_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.first_name_entry = ttk.Entry(self.master)
        self.first_name_entry.grid(row=1, column=1, padx=10, pady=10)

        self.last_name_label = ttk.Label(self.master, text="Last Name:")
        self.last_name_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.last_name_entry = ttk.Entry(self.master)
        self.last_name_entry.grid(row=2, column=1, padx=10, pady=10)

        self.phone_label = ttk.Label(self.master, text="Phone Number:")
        self.phone_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.phone_entry = ttk.Entry(self.master)
        self.phone_entry.grid(row=3, column=1, padx=10, pady=10)

        self.submit_button = ttk.Button(self.master, text="Add Contact", command=self.add_contact)
        self.submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="we")

        self.back_button = ttk.Button(self.master, text="Back", command=self.create_homepage)
        self.back_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="we")
        
    def add_contact(self):
        first_name = self.first_name_entry.get().strip()
        last_name = self.last_name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        
        # Validate phone number
        if len(phone) != 10 or not phone.isdigit() or phone.startswith('0'):
            messagebox.showerror("Error", "Please enter a valid 10-digit phone number.")
            return
        
        full_name = f"{first_name} {last_name}"
        if first_name and last_name and phone:
            if full_name in self.contacts:
                messagebox.showerror("Error", "Contact already exists!")
            else:
                self.contacts[full_name] = phone
                self.save_contacts()
                messagebox.showinfo("Success", "Contact added successfully!")
                self.first_name_entry.delete(0, tk.END)
                self.last_name_entry.delete(0, tk.END)
                self.phone_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter valid information for all fields!")
    
    def search_contact_page(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        self.title_label = ttk.Label(self.master, text="Search Contact", font=('Arial', 20))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)

        self.search_label = ttk.Label(self.master, text="First Name:")
        self.search_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.search_entry = ttk.Entry(self.master)
        self.search_entry.grid(row=1, column=1, padx=10, pady=10)

        self.search_button = ttk.Button(self.master, text="Search", command=self.search_contact)
        self.search_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="we")

        self.back_button = ttk.Button(self.master, text="Back", command=self.create_homepage)
        self.back_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="we")
    
    def search_contact(self):
        search_name = self.search_entry.get().strip()
        if search_name:
            if search_name in self.contacts:
                messagebox.showinfo("Search Result", f"{search_name}: {self.contacts[search_name]}")
            else:
                messagebox.showinfo("Search Result", "Contact not found.")
        else:
            messagebox.showerror("Error", "Please enter a first name to search.")
    
    def view_contacts(self):
        if self.contacts:
            top = tk.Toplevel(self.master)
            top.title("Contact List")
            top.geometry("500x400")

            contacts_str = "Serial No.  First Name     Last Name      Phone Number\n"
            contacts_str += "-"*60 + "\n"
            serial_no = 1
            for name, phone in self.contacts.items():
                first_name, last_name = name.split(" ")
                contacts_str += f"{serial_no:<12}{first_name:<15}{last_name:<15}{phone}\n"
                serial_no += 1

            contacts_text = tk.Text(top, wrap="none", font=("Courier New", 10))
            contacts_text.insert(tk.END, contacts_str)
            contacts_text.config(state="disabled")
            contacts_text.pack(expand=True, fill='both')
        else:
            messagebox.showinfo("Contacts", "No contacts found.")
    
    def delete_contact_page(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        self.title_label = ttk.Label(self.master, text="Delete Contact", font=('Arial', 20))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)

        self.delete_label = ttk.Label(self.master, text="Full Name:")
        self.delete_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.delete_entry = ttk.Entry(self.master)
        self.delete_entry.grid(row=1, column=1, padx=10, pady=10)

        self.delete_button = ttk.Button(self.master, text="Delete", command=self.delete_contact)
        self.delete_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="we")

        self.back_button = ttk.Button(self.master, text="Back", command=self.create_homepage)
        self.back_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="we")
    
    def delete_contact(self):
        delete_name = self.delete_entry.get().strip()
        if delete_name:
            if delete_name in self.contacts:
                del self.contacts[delete_name]
                self.save_contacts()
                messagebox.showinfo("Success", "Contact deleted successfully!")
            else:
                messagebox.showinfo("Error", "Contact not found.")
        else:
            messagebox.showerror("Error", "Please enter the full name to delete.")
    
    def update_contact_page(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        self.title_label = ttk.Label(self.master, text="Update Contact", font=('Arial', 20))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)

        self.update_label = ttk.Label(self.master, text="Full Name:")
        self.update_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.update_entry = ttk.Entry(self.master)
        self.update_entry.grid(row=1, column=1, padx=10, pady=10)

        self.update_phone_label = ttk.Label(self.master, text="New Phone Number:")
        self.update_phone_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.update_phone_entry = ttk.Entry(self.master)
        self.update_phone_entry.grid(row=2, column=1, padx=10, pady=10)

        self.update_button = ttk.Button(self.master, text="Update", command=self.update_contact)
        self.update_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="we")

        self.back_button = ttk.Button(self.master, text="Back", command=self.create_homepage)
        self.back_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="we")
    
    def update_contact(self):
        update_name = self.update_entry.get().strip()
        new_phone = self.update_phone_entry.get().strip()
        
        # Validate phone number
        if len(new_phone) != 10 or not new_phone.isdigit() or new_phone.startswith('0'):
            messagebox.showerror("Error", "Please enter a valid 10-digit phone number.")
            return
        
        if update_name:
            if update_name in self.contacts:
                self.contacts[update_name] = new_phone
                self.save_contacts()
                messagebox.showinfo("Success", "Contact updated successfully!")
                self.update_entry.delete(0, tk.END)
                self.update_phone_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Contact not found.")
        else:
            messagebox.showerror("Error", "Please enter the full name to update.")

    def save_contacts(self):
        with open(self.file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Serial No.", "First Name", "Last Name", "Phone Number"])
            serial_no = 1
            for name, phone in self.contacts.items():
                first_name, last_name = name.split(" ")
                writer.writerow([serial_no, first_name, last_name, phone])
                serial_no += 1
    
    def load_contacts(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    if row:
                        serial_no, first_name, last_name, phone = row
                        self.contacts[f"{first_name} {last_name}"] = phone

if __name__ == "__main__":
    root = tk.Tk()
    app = PhoneBookManager(root)
    root.mainloop()
