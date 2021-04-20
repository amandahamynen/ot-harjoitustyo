from tkinter import ttk, Tk, constants
import tkinter
from services.quizzy_service import quizzy_service


class UserCreation:
    def __init__(self, root, handle_creation, handle_login):
        self.root = root
        self.handle_creation = handle_creation
        self.handle_login = handle_login
        self.frame = None
        self.creation_frame = None
        self.username_entry = None
        self.first_name_entry = None
        self.last_name_entry = None
        self.password_entry = None
        self.error_label = None
        self.initialize()

    def initialize(self):
        self.frame = tkinter.Frame(master=self.root, width=1200, height=700)
        self.creation_frame = tkinter.Frame(self.root, background="white")

        label = tkinter.Label(self.creation_frame, text="Create a new user",
                              fg="black", bg="white", font=("Arial", 25))

        label.grid(padx=50, pady=10, sticky=constants.EW)

        self.first_name_field()
        self.last_name_field()
        self.username_field()
        self.password_field()

        button_create_user = tkinter.Button(
            master=self.creation_frame, text="Create user", command=self.creation_handler, fg="white", bg="white", bd=0)
        button_login_screen = tkinter.Button(
            master=self.creation_frame, text="Go back", command=self.handle_login, fg="white", bg="white", bd=0)

        button_create_user.grid(padx=50, pady=5, sticky=constants.EW)
        button_login_screen.grid(padx=50, pady=5, sticky=constants.EW)

        self.creation_frame.place(x=70, y=70)

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def creation_handler(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if len(username) == 0 or len(password) == 0:
            if self.error_label:
                self.error_label.destroy()
            self.error_label = tkinter.Label(
                self.creation_frame, text="Username and password are required", fg="black", bg="white")
            self.error_label.grid(padx=50, pady=10)
            return

        try:
            quizzy_service.create_user(username, password)
            self.handle_creation()
        except:
            if self.error_label:
                self.error_label.destroy()
            self.error_label = tkinter.Label(
                self.creation_frame, text="Username already exists", fg="black", bg="white")
            self.error_label.grid(padx=50, pady=10)

    def first_name_field(self):
        label = tkinter.Label(master=self.creation_frame,
                              text="First name", fg="black", bg="white")
        self.first_name_entry = ttk.Entry(master=self.creation_frame)

        label.grid(padx=50, pady=5, sticky=constants.W)
        self.first_name_entry.grid(padx=50, pady=5, sticky=constants.EW)

    def last_name_field(self):
        label = tkinter.Label(master=self.creation_frame,
                              text="Last name", fg="black", bg="white")
        self.last_name_entry = ttk.Entry(master=self.creation_frame)

        label.grid(padx=50, pady=5, sticky=constants.W)
        self.last_name_entry.grid(padx=50, pady=5, sticky=constants.EW)

    def username_field(self):
        label = tkinter.Label(master=self.creation_frame,
                              text="Username", fg="black", bg="white")
        self.username_entry = ttk.Entry(master=self.creation_frame)

        label.grid(padx=50, pady=5, sticky=constants.W)
        self.username_entry.grid(padx=50, pady=5, sticky=constants.EW)

    def password_field(self):
        label = tkinter.Label(master=self.creation_frame,
                              text="Password", fg="black", bg="white")
        self.password_entry = ttk.Entry(master=self.creation_frame)

        label.grid(padx=50, pady=5, sticky=constants.W)
        self.password_entry.grid(padx=50, pady=5, sticky=constants.EW)
