import os
import random
import pandas as pd
from tkinter import END, messagebox
from constants import LETTERS, NUMBERS, SYMBOLS


class Manager:
    def __init__(self, **kwargs):
        self.website = kwargs.get("wn_entry")
        self.user = kwargs.get("ue_entry")
        self.password = kwargs.get("pw_entry")
        self.main = kwargs.get("main")

    def save_data(self):
        """Creates the data frame structure and save it to the book"""

        # check if the fields are populated then create the data frame structure
        if self.validate():
            data_strct = {
                "website" : [self.website.get()],
                "user" : [self.user.get()],
                "password" : [self.password.get()]
            }

            # read the last index of the last row or set the index to zero if there are not records
            existing_df = pd.read_csv('book.csv', index_col=0)
            if existing_df.index.empty:
                last_index = 0
            else:
                last_index = existing_df.index.max()

            # save the data from the app fields to the csv file
            new_data = pd.DataFrame(data_strct)
            new_data.index = range(last_index + 1, last_index + 1 + len(new_data))
            new_data.to_csv('book.csv', mode='a', header=False)

            self.clear() # clear the fields

            messagebox.showinfo(title="Info", message="Credentials were saved to your book.")

            # update the book
            self.main.update_book()

    def validate(self):
        """Makes sure all the fields are populated"""

        if self.website.get() == "":
            messagebox.showerror(title="Field Required", message="The field: 'Website' is required.")
            return False

        if self.user.get() == "":
            messagebox.showerror(title="Field Required", message="The field: 'Email/User' is required.")
            return False

        if self.password.get() == "":
            messagebox.showerror(title="Field Required", message="The field: 'Password' is required.")
            return False

        # if all the fields are populated ask for saving confirmation and return it to save_data
        confirm = messagebox.askyesno(title="Save Confirmation", message=f"Are you sure you want to save these credentials? \nWebsite name: {self.website.get()} \nEmail/User: {self.user.get()} \nPassword: {self.password.get()}")
        return confirm

    def generate_pw(self):
        """Generates a random password upon calling the function, populate the password field with the generated password and copy it ti clipboard"""

        # use list comprehension to generate the random characters required
        password_letters = [random.choice(LETTERS) for _ in range(random.randint(8, 10))]
        password_numbers = [random.choice(NUMBERS) for _ in range(random.randint(2, 4))]
        password_symbols = [random.choice(SYMBOLS) for _ in range(random.randint(2, 4))]

        # add the characters together then shuffle them inside the list
        raw_password = password_letters + password_numbers + password_symbols
        random.shuffle(raw_password)

        # take all the characters from the list and make them plain text
        password = "".join(raw_password)

        # populate the password field with the generated password
        self.password.delete(0, END)
        self.password.insert(0, password)

        # copy the generated password to clipboard
        self.main.clipboard_clear()
        self.main.clipboard_append(password)

        messagebox.showinfo(title="Info", message="Password was copied to Clipboard.")

    def clear(self):
        """Clears all the fields and focuses the first field"""
        self.website.delete(0, END)
        self.website.focus()
        self.user.delete(0, END)
        self.password.delete(0, END)
