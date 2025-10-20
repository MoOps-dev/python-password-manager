import os
import pandas as pd
from tkinter import END, messagebox


class Manager:
    def __init__(self, **kwargs):
        self.website = kwargs.get("wn_entry")
        self.user = kwargs.get("ue_entry")
        self.password = kwargs.get("pw_entry")

    def save_data(self):
        if self.validate():
            data_strct = {
                "website" : [self.website.get()],
                "user" : [self.user.get()],
                "password" : [self.password.get()]
            }

            if not os.path.isfile("book.csv"):
                file = pd.DataFrame(columns=["id", "website", "username", "password"])
                file.to_csv('book.csv', index=False)

            existing_df = pd.read_csv('book.csv', index_col=0)
            if existing_df.index.empty:
                last_index = 0
            else:
                last_index = existing_df.index.max()

            new_data = pd.DataFrame(data_strct)
            new_data.index = range(last_index + 1, last_index + 1 + len(new_data))
            new_data.to_csv('book.csv', mode='a', header=False)

            self.clear()

    def validate(self):
        if self.website.get() == "":
            messagebox.showerror(title="Field Required", message="The field: 'Website' is required")
            return False

        if self.user.get() == "":
            messagebox.showerror(title="Field Required", message="The field: 'Email/User' is required")
            return False

        if self.password.get() == "":
            messagebox.showerror(title="Field Required", message="The field: 'Password' is required")
            return False

        confirm = messagebox.askyesno(title="Save Confirmation", message=f"These are the info that will be saved to your book: \nWebsite name: {self.website.get()} \nEmail/User: {self.user.get()} \nPassword: {self.password.get()}")
        return confirm

    def clear(self):
        self.website.delete(0, END)
        self.website.focus()
        self.user.delete(0, END)
        self.password.delete(0, END)
