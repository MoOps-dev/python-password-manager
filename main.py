from manager_class import Manager
from ui_class import MainScreen

# ---------------------------- UI SETUP ------------------------------- #
main = MainScreen()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
manager = Manager(wn_entry=main.wn_entry, ue_entry=main.ue_entry, pw_entry=main.pw_entry)

main.save_button.config(command=manager.save_data)

main.mainloop()