from tkinter import Label, Tk, ttk, constants, PhotoImage
import tkinter
from services.quizzy_service import quizzy_service, InvalidCredentialsError


class LoginScreen():
    def __init__(self, root, handle_login, handle_user_creation):
        self.root = root
        self.handle_login = handle_login
        self.handle_user_creation = handle_user_creation
        self.frame = None
        self.login_frame = None
        self.username_entry = None
        self.password_entry = None
        self.error_label = None
        self.initialize()

    def initialize(self):
        self.frame = tkinter.Frame(master=self.root, width=1200, height=700)
        self.login_frame = tkinter.Frame(self.root, background="WHITE")

        label = tkinter.Label(master=self.login_frame, text="Login to Quizzy",
                              fg="black", bg="white", font=("Arial", 25))
        label.grid(padx=50, pady=20, sticky=constants.N)

        self.username_field()
        self.password_field()

        button_login = tkinter.Button(
            master=self.login_frame, text="Login", command=self.login_handler, fg="white", bg="white", bd=0)
        button_create_user = tkinter.Button(
            master=self.login_frame, text="Create a new user", command=self.handle_user_creation, fg="white", bg="white", bd=0)
        button_login.grid(padx=50, pady=10, sticky=constants.EW)
        button_create_user.grid(padx=50, pady=20, sticky=constants.EW)
        self.login_frame.place(x=70, y=70)

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def username_field(self):
        label = tkinter.Label(master=self.login_frame,
                              text="Username", fg="black", bg="white")
        self.username_entry = ttk.Entry(master=self.login_frame)

        label.grid(padx=50, pady=5, sticky=constants.W)
        self.username_entry.grid(padx=50, pady=5, sticky=constants.EW)

    def password_field(self):
        label = tkinter.Label(master=self.login_frame,
                              text="Password", fg="black", bg="white")
        self.password_entry = ttk.Entry(master=self.login_frame)

        label.grid(padx=50, pady=5, sticky=constants.W)
        self.password_entry.grid(padx=50, pady=5, sticky=constants.EW)

    def login_handler(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            quizzy_service.login(username, password)
            self.handle_login()
        except InvalidCredentialsError:
            if self.error_label:
                self.error_label.destroy()
            self.error_label = tkinter.Label(
                self.login_frame, text="Invalid username or password", fg="black", bg="white")
            self.error_label.grid(padx=50, pady=10)
