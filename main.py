from manager_class import Manager
from ui_class import MainScreen

# ---------------------------- UI SETUP ------------------------------- #
main = MainScreen()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
manager = Manager(wn_entry=main.wn_entry, ue_entry=main.ue_entry, pw_entry=main.pw_entry, main=main)

main.save_button.config(command=manager.save_data)
main.gen_button.config(command=manager.generate_pw)

main.mainloop()