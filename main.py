from book_class import Book
from manager_class import Manager
from ui_class import MainScreen

# ---------------------------- UI SETUP ------------------------------- #
main = MainScreen()
book = Book()

# ---------------------------- SAVE PASSWORD ------------------------------- #
manager = Manager(wn_entry=main.wn_entry, ue_entry=main.ue_entry, pw_entry=main.pw_entry, main=main)

main.save_button.config(command=manager.save_data)
main.gen_button.config(command=manager.generate_pw)
main.book_button.config(command=main.open_book)
main.bind("<Configure>", main.move_child_with_parent)
main.mainloop()