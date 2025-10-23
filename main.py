import os
from manager_class import Manager
from ui_class import MainScreen
import pandas as pd

# ---------------------------- UI SETUP ------------------------------- #
main = MainScreen()

# ---------------------------- SAVE PASSWORD & MANAGE SAVED ------------------------------- #
manager = Manager(wn_entry=main.wn_entry, ue_entry=main.ue_entry, pw_entry=main.pw_entry, main=main)

# make sure the book.csv file exists by creating it
if not os.path.isfile("book.csv"):
    file = pd.DataFrame(columns=["id", "website", "username", "password"])
    file.to_csv('book.csv', index=False)

# ---------------------------- BUTTON FUNCTION ------------------------------- #
main.save_button.config(command=manager.save_data)
main.gen_button.config(command=manager.generate_pw)
main.book_button.config(command=main.open_book)
main.bind("<Configure>", main.move_child_with_parent)
main.mainloop()