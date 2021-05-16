from tkinter import constants
import tkinter
from services.quizzy_service import quizzy_service


class HomeScreen:

    """ Luokka näkymälle, jossa käyttäjä voi kirjautua ulos sovelluksesta, valita haluamansa
    asetukset peliin ja aloittaa pelin pelaamisen.

    Luokka tarjoaa näkymän, jossa käyttäjä voi kirjautua ulos näkymän oikeassa yläkulmassa olevasta
    painikkeesta. Näkymässä käyttäjä voi vaihtaa kahta asetusta peliin liittyen; kysymysten aihealueen ja
    kysymysten lukumäärän. Käyttäjä voi aloittaa pelin pelaamisen 'Start the quiz' painikkeesta.
    """

    def __init__(self, root, handle_logout, handle_start):
        self._root = root
        self._handle_logoout = handle_logout
        self._handle_start = handle_start
        self._frame = None
        self._selection_frame = None
        self._q_num = 5
        self._bg=tkinter.PhotoImage(file="src/resources/boat-5889919_1280.png")

        self._initialize()

    def _initialize(self):
        self._frame = tkinter.Frame(master=self._root, width=1200, height=700)
        self._selection_frame = tkinter.Frame(
            self._root, width=900, height=500, bg="white")

        label_bg = tkinter.Label(master=self._frame, image=self._bg)
        label_bg.place(x=0, y=0)

        logout_button = tkinter.Button(
            master=self._frame, text="Logout", command=self._handle_logoout, fg="white", bg="white")
        logout_button.place(x=1100, y=10)

        user = quizzy_service.get_current_user()
        username_label = tkinter.Label(
            self._frame, text=f"Signed in as {user.username}", fg="black", bg="white")
        username_label.place(x=10, y=15)

        label = tkinter.Label(master=self._selection_frame,
                              text=f"Welcome to Quizzy, {user.firstname} {user.lastname}!", fg="black", bg="white", font=("Arial", 25))
        label.place(x=450, y=30, anchor=constants.N)

        label1 = tkinter.Label(self._selection_frame, text="Please choose the topic of questions: ", fg="black", bg="white")
        label1.place(x=400, y=250, anchor=constants.N)

        topic_options = ['Capital cities', 'Films', 'Games']
        self._topic = tkinter.StringVar()
        self._topic.set(topic_options[0])
        t = tkinter.OptionMenu(self._selection_frame, self._topic, *topic_options)
        t.place(x=580, y=250, anchor=constants.N)

        label2 = tkinter.Label(self._selection_frame, text="Please choose the amount of questions: ", fg="black", bg="white")
        label2.place(x=400, y=350, anchor=constants.N)

        num_options = [3,5,10]
        self._chosen = tkinter.StringVar()
        self._chosen.set(num_options[0])
        num = tkinter.OptionMenu(self._selection_frame, self._chosen, *num_options)
        num.place(x=580, y=350, anchor=constants.N)

        start_button = tkinter.Button(
            self._selection_frame, text="Start the quiz", command=self._start_handler, fg="white", bg="white")
        start_button.place(x=450, y=400, anchor=constants.N)

        self._selection_frame.place(x=600, y=100, anchor=constants.N)

    def _start_handler(self):
        self._chosen_topic = self._topic.get()
        quizzy_service.set_topic_of_questions(self._chosen_topic)
        self._q_num = self._chosen.get()
        quizzy_service.set_number_of_questions(self._q_num)
        self._handle_start()

    def pack(self):

        """ Pakkaa kehyksen. """

        self._frame.pack(fill=constants.X)

    def destroy(self):

        """ Tuohoaa kehyksen. """
    
        self._frame.destroy()
