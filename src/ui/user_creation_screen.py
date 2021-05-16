from tkinter import ttk, constants
import tkinter
from services.quizzy_service import quizzy_service


class UserCreation:

    """ Luokka näkymälle, jossa käyttäjä voi luoda uuden käyttäjän sovellukseen.

    Luokka tarjoaa näkymän, jossa käyttäjä voi luoda uuden käyttäjän syöttämällä etunimen, sukunimen,
    valitseman käyttäjätunnuksen ja salasanan niitä vastaaviin kenttiin. Käyttäjätunnuksen tulee olla uniikki, 
    eikä käyttäjätunnus tai salasana voi olla tyhjiä syötteitä.
    """

    def __init__(self, root, handle_creation, handle_login):
        self._root = root
        self._handle_creation = handle_creation
        self._handle_login = handle_login
        self._frame = None
        self._creation_frame = None
        self._username_entry = None
        self._first_name_entry = None
        self._last_name_entry = None
        self._password_entry = None
        self._error_label = None
        self._bg=tkinter.PhotoImage(file="src/resources/boat-5889919_1280.png")
        self._initialize()

    def _initialize(self):
        self._frame = tkinter.Frame(master=self._root, width=1200, height=700)
        self._creation_frame = tkinter.Frame(self._root, background="white")

        label_bg = tkinter.Label(master=self._frame, image=self._bg)
        label_bg.place(x=0, y=0)

        label = tkinter.Label(self._creation_frame, text="Create a new user",
                              fg="black", bg="white", font=("Arial", 25))

        label.grid(padx=50, pady=10, sticky=constants.EW)

        self._first_name_field()
        self._last_name_field()
        self._username_field()
        self._password_field()

        button_create_user = tkinter.Button(
            master=self._creation_frame, text="Create user", command=self._creation_handler, fg="white", bg="white", bd=0)
        button_login_screen = tkinter.Button(
            master=self._creation_frame, text="Go back", command=self._handle_login, fg="white", bg="white", bd=0)

        button_create_user.grid(padx=50, pady=5, sticky=constants.EW)
        button_login_screen.grid(padx=50, pady=5, sticky=constants.EW)

        self._creation_frame.place(x=70, y=70)

    def pack(self):

        """ Pakkaa kehyksen. """

        self._frame.pack(fill=constants.X)

    def destroy(self):

        """ Tuohoaa kehyksen. """

        self._frame.destroy()

    def _creation_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
        firstname = self._first_name_entry.get()
        lastname = self._last_name_entry.get()

        if len(username) == 0 or len(password) == 0:
            if self._error_label:
                self._error_label.destroy()
            self._error_label = tkinter.Label(
                self._creation_frame, text="Username and password are required", fg="black", bg="white")
            self._error_label.grid(padx=50, pady=10)
            return

        try:
            quizzy_service.create_user(username, password, firstname, lastname)
            self._handle_creation()
        except:
            if self._error_label:
                self._error_label.destroy()
            self._error_label = tkinter.Label(
                self._creation_frame, text="Username already exists", fg="black", bg="white")
            self._error_label.grid(padx=50, pady=10)

    def _first_name_field(self):
        label = tkinter.Label(master=self._creation_frame,
                              text="First name", fg="black", bg="white")
        self._first_name_entry = ttk.Entry(master=self._creation_frame)

        label.grid(padx=50, pady=5, sticky=constants.W)
        self._first_name_entry.grid(padx=50, pady=5, sticky=constants.EW)

    def _last_name_field(self):
        label = tkinter.Label(master=self._creation_frame,
                              text="Last name", fg="black", bg="white")
        self._last_name_entry = ttk.Entry(master=self._creation_frame)

        label.grid(padx=50, pady=5, sticky=constants.W)
        self._last_name_entry.grid(padx=50, pady=5, sticky=constants.EW)

    def _username_field(self):
        label = tkinter.Label(master=self._creation_frame,
                              text="Username", fg="black", bg="white")
        self._username_entry = ttk.Entry(master=self._creation_frame)

        label.grid(padx=50, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=50, pady=5, sticky=constants.EW)

    def _password_field(self):
        label = tkinter.Label(master=self._creation_frame,
                              text="Password", fg="black", bg="white")
        self._password_entry = ttk.Entry(master=self._creation_frame)

        label.grid(padx=50, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=50, pady=5, sticky=constants.EW)
