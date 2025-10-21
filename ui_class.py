import os
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.ttk import Treeview
import tkinter.font as tkfont
import pandas as pd
from constants import *

class MainScreen(Tk):
    def __init__(self):
        super().__init__()

        self.delete_button = None
        self.book_window = None
        self.bw_list = None
        self.bw_scrollbar = None

        self.title("Password Manager")

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.winfo_reqwidth()) // 2
        y = (screen_height - self.winfo_reqheight()) // 2

        self.resizable(False, False)
        self.geometry(f"470x200+{x - 160}+{y - 100}")

        self.canvas = Canvas(self, width=466, height=196, bg=BG_COLOUR, highlightthickness=0)
        self.logo = PhotoImage(file="logo.png")
        self.canvas.create_image(65, 100, image=self.logo)

        self.title_label = Label(text="Welcome to Password Manager!", font=("Courier", 13, "bold"), fg= "White", bg=BG_COLOUR, highlightthickness=0)
        self.canvas.create_window(290, 30, window=self.title_label)

        self.wn_label = Label(text="Website:", font=("Courier", 11, "normal"), fg= "White", bg=BG_COLOUR, highlightthickness=0)
        self.canvas.create_window(170, 70, window=self.wn_label)

        self.wn_entry = Entry(width=38, highlightthickness=0)
        self.wn_entry.focus()
        self.canvas.create_window(330, 70, window=self.wn_entry)

        self.ue_label = Label(text="Email/User:", font=("Courier", 11, "normal"), fg= "White", bg=BG_COLOUR, highlightthickness=0)
        self.canvas.create_window(182, 100, window=self.ue_label)

        self.ue_entry = Entry(width=34, highlightthickness=0)
        self.canvas.create_window(342, 100, window=self.ue_entry)

        self.pw_label = Label(text="Password:", font=("Courier", 11, "normal"), fg= "White", bg=BG_COLOUR, highlightthickness=0)
        self.canvas.create_window(172, 130, window=self.pw_label)

        self.pw_entry = Entry(width=26, highlightthickness=0)
        self.canvas.create_window(300, 130, window=self.pw_entry)

        self.gen_button = Button(text="Generate", highlightthickness=0)
        self.canvas.create_window(418, 130, window=self.gen_button)

        self.save_button = Button(text="Save", highlightthickness=0, width= 20)
        self.canvas.create_window(207, 170, window=self.save_button)

        self.book_button = Button(text="Open Book", highlightthickness=0, width= 20)
        self.canvas.create_window(372, 170, window=self.book_button)

        self.canvas.pack()
        self.canvas.focus()

    def open_book(self):
        if not self.book_window:
            self.book_window = Toplevel(self)
            self.book_window.title("Password Manager Book")
            self.book_window.resizable(False, False)
            self.book_window.wm_transient(self)
            self.book_window.bind("<Destroy>", self.destroy_child)
            x = self.winfo_x()
            y = self.winfo_y()
            if self.book_window is not None:
                self.book_window.geometry(f"400x400+{x + 480}+{y + 0}")

            self.delete_button = Button(self.book_window, text="Delete", width=15, command=self.delete_from_book)
            self.delete_button.pack(side="bottom", pady=10)

            self.bw_scrollbar = Scrollbar(self.book_window, orient="vertical")
            self.bw_scrollbar.pack(side="right", fill="both")

            self.bw_list = Treeview(
                self.book_window,
                height=18,
                yscrollcommand=self.bw_scrollbar.set,
                selectmode="browse",
                show ='tree'
            )

            self.bw_scrollbar.config(command=self.bw_list.yview)

            self.bw_list.pack(padx=10, pady=10, side="left", expand=True)
            self.bw_list.column('#0', width=360)
            self.bw_list.bind('<<TreeviewSelect>>', self.on_select)

            style = ttk.Style()
            style.configure("Treeview", font=("Arial", 11))

            if not os.path.isfile("book.csv"):
                file = pd.DataFrame(columns=["id", "website", "username", "password"])
                file.to_csv('book.csv', index=False)

            df = pd.read_csv('book.csv', index_col=0)

            for index, row in df.iterrows():
                parent_id = self.bw_list.insert('', 'end', text=f'{index}. {row['website']}', values=([f"-{index}"]))
                self.bw_list.insert(parent_id, 'end', text=f"User: {row['username']}", values=(["+"]))
                self.bw_list.insert(parent_id, 'end', text=f"Password: {row['password']}", values=(["++"]))

        else:
            self.book_window.destroy()
            self.destroy_child("")

    def move_child_with_parent(self, event):
        if self.book_window is not None:
            x = self.winfo_x()
            y = self.winfo_y()
            self.book_window.geometry(f"+{x + 480}+{y + 0}")

    def on_select(self, event):
        selected_items = self.bw_list.selection()
        for item in selected_items:
            item_value = self.bw_list.item(item, 'value')
            item_text = self.bw_list.item(item, 'text')

            if item_value[0] == "+":
                self.clipboard_clear()
                self.clipboard_append(item_text.replace("User: ",""))
                messagebox.showinfo(title="Info", message=f"{item_text.replace("User: ","")} : was copied to Clipboard.")
            elif item_value[0] == "++":
                self.clipboard_clear()
                self.clipboard_append(item_text.replace("Password: ",""))
                messagebox.showinfo(title="Info", message=f"{item_text.replace("Password: ","")} : was copied to Clipboard.")

    def delete_from_book(self):
        selected_items = self.bw_list.selection()
        for item in selected_items:
            item_value = self.bw_list.item(item, 'value')
            item_text = self.bw_list.item(item, 'text')

            if item_value[0][0] == "-":
                self.clipboard_clear()
                self.clipboard_append(item_text.replace("User: ",""))
                confirm = messagebox.askyesno(title="Info", message=f"Are you Sure you want to delete: \n\n{item_text.replace("User: ","")}")
                if confirm:
                    df = pd.read_csv('book.csv', index_col=0)
                    index = int(item_value[0][1:len(item_value[0])])
                    df.drop(index, inplace=True)
                    df.to_csv('book.csv', index=True)
                    messagebox.showinfo(title="Info", message=f"{item_text.replace("Password: ", "")} : has been Deleted.")
                    self.open_book()
                    self.open_book()

    def destroy_child(self, event):
        if self.book_window:
            self.book_window = None
