import tkinter as tk
import re
from tkinter import ttk, messagebox

# Regular expressions for validation
NAME_REGEX = re.compile(r'^[a-zA-Z]+(?:\s[a-zA-Z]+)*$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
PHONE_REGEX = re.compile(r'^\d{10}$')

# Domain-specific form
class DomainForm(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Form widgets
        self.name_label = tk.Label(self, text="Name:", font=("Arial", 16))
        self.name_entry = tk.Entry(self, font=("Arial", 16))
        self.email_label = tk.Label(self, text="Email:", font=("Arial", 16))
        self.email_entry = tk.Entry(self, font=("Arial", 16))
        self.phone_label = tk.Label(self, text="Phone:", font=("Arial", 16))
        self.phone_entry = tk.Entry(self, font=("Arial", 16))
        self.gender_label = tk.Label(self, text="Gender:", font=("Arial", 16))
        self.gender_dropdown = ttk.Combobox(self, values=['', 'Male', 'Female', 'Other'], font=("Arial", 16), style='Combobox.TCombobox')
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_form, font=("Arial", 16))

        # Form validation
        self.name_entry.config(validate='key', validatecommand=(self.register(self.validate_name), '%S'))
        self.email_entry.config(validate='key', validatecommand=(self.register(self.validate_email), '%S'))
        self.phone_entry.config(validate='key', validatecommand=(self.register(self.validate_phone), '%S'))

        # Form layout
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.email_label.grid(row=1, column=0, padx=10, pady=10)
        self.email_entry.grid(row=1, column=1, padx=10, pady=10)

        self.phone_label.grid(row=2, column=0, padx=10, pady=10)
        self.phone_entry.grid(row=2, column=1, padx=10, pady=10)

        self.gender_label.grid(row=3, column=0, padx=10, pady=10)
        self.gender_dropdown.grid(row=3, column=1, padx=10, pady=10)

        self.submit_button.grid(row=4, column=1, padx=10, pady=20, columnspan=2)

        # Form styling
        self.configure(bg='#f0f0f0')  # Background color
        for widget in self.winfo_children():
            widget.configure(foreground="black", background='#f0f0f0')  # Font and background color

    # Validation functions
    def validate_name(self, value):
        return NAME_REGEX.match(value) is not None

    def validate_email(self, value):
        return EMAIL_REGEX.match(value) is not None

    def validate_phone(self, value):
        return PHONE_REGEX.match(value) is not None

    # Submit form function
    def submit_form(self):
        """Submit the form data."""

        # Validate the form data.
        if not self.validate_name(self.name_entry.get()):
            messagebox.showerror("Validation Error", "Invalid name.")
            return

        if not self.validate_email(self.email_entry.get()):
            messagebox.showerror("Validation Error", "Invalid email.")
            return

        if not self.validate_phone(self.phone_entry.get()):
            messagebox.showerror("Validation Error", "Invalid phone number.")
            return

        if not self.gender_dropdown.get():
            messagebox.showerror("Validation Error", "Please select a gender.")
            return

        # Form data is valid, you can proceed with further actions here.
        messagebox.showinfo("Success", "Form submitted successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Domain Form")
    root.geometry("400x300")  # Set the initial window size
    domain_form = DomainForm(root)
    domain_form.pack(fill=tk.BOTH, expand=True)  # Expand to fill the window
    root.mainloop()
