from tkinter import *
from constants import *


class MainScreen(Tk):
    def __init__(self):
        super().__init__()
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

        self.open_book = Button(text="Open Book", highlightthickness=0, width= 20)
        self.canvas.create_window(372, 170, window=self.open_book)

        self.canvas.pack()
        self.canvas.focus()
