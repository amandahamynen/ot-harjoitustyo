from tkinter import Label, Tk, ttk, constants, PhotoImage
import tkinter
from services.quizzy_service import quizzy_service, InvalidCredentialsError


class LoginScreen():

    """ Luokka näkymälle, jossa käyttäjä voi kirjautua sisään.

    Luokka tarjoaa näkymän, jossa käyttäjä voi kirjautua sisään syöttämällä käyttäjätunnuksen ja salasanan niitä
    vastaaviin kenttiin.
    """

    def __init__(self, root, handle_login, handle_user_creation):
        self._root = root
        self._handle_login = handle_login
        self._handle_user_creation = handle_user_creation
        self._frame = None
        self._login_frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_label = None
        self._bg=tkinter.PhotoImage(file="src/resources/boat-5889919_1280.png")
        self._initialize()

    def _initialize(self):
        self._frame = tkinter.Frame(master=self._root, width=1200, height=700)
        self._login_frame = tkinter.Frame(self._root, background="WHITE")

        label_bg = tkinter.Label(master=self._frame, image=self._bg)
        label_bg.place(x=0, y=0)

        label = tkinter.Label(master=self._login_frame, text="Login to Quizzy",
                              fg="black", bg="white", font=("Arial", 25))
        label.grid(padx=50, pady=20, sticky=constants.N)

        self._username_field()
        self._password_field()

        button_login = tkinter.Button(
            master=self._login_frame, text="Login", command=self._login_handler, fg="white", bg="white", bd=0)
        button_create_user = tkinter.Button(
            master=self._login_frame, text="Create a new user", command=self._handle_user_creation, fg="white", bg="white", bd=0)
        button_login.grid(padx=50, pady=10, sticky=constants.EW)
        button_create_user.grid(padx=50, pady=20, sticky=constants.EW)
        self._login_frame.place(x=70, y=70)

    def pack(self):

        """ Pakkaa kehyksen. """

        self._frame.pack(fill=constants.X)

    def destroy(self):

        """ Tuohoaa kehyksen. """

        self._frame.destroy()

    def _username_field(self):
        label = tkinter.Label(master=self._login_frame,
                              text="Username", fg="black", bg="white")
        self._username_entry = ttk.Entry(master=self._login_frame)

        label.grid(padx=50, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=50, pady=5, sticky=constants.EW)

    def _password_field(self):
        label = tkinter.Label(master=self._login_frame,
                              text="Password", fg="black", bg="white")
        self._password_entry = ttk.Entry(master=self._login_frame)

        label.grid(padx=50, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=50, pady=5, sticky=constants.EW)

    def _login_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            quizzy_service.login(username, password)
            self._handle_login()
        except InvalidCredentialsError:
            if self._error_label:
                self._error_label.destroy()
            self._error_label = tkinter.Label(
                self._login_frame, text="Invalid username or password", fg="black", bg="white")
            self._error_label.grid(padx=50, pady=10)
