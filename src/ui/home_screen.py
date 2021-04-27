from tkinter import Image, ttk, Tk, constants
import tkinter
from services.quizzy_service import quizzy_service


class HomeScreen:
    def __init__(self, root, handle_logout, handle_start):
        self.root = root
        self.handle_logoout = handle_logout
        self.handle_start = handle_start
        self.frame = None
        self.selection_frame = None
        self.q_num = 5
        self.bg=tkinter.PhotoImage(file="src/resources/boat-5889919_1280.png")

        self.initialize()

    def initialize(self):
        self.frame = tkinter.Frame(master=self.root, width=1200, height=700)
        self.selection_frame = tkinter.Frame(
            self.root, width=900, height=500, bg="white")

        label_bg = tkinter.Label(master=self.frame, image=self.bg)
        label_bg.place(x=0, y=0)

        logout_button = tkinter.Button(
            master=self.frame, text="Logout", command=self.handle_logoout, fg="white", bg="white")
        logout_button.place(x=1100, y=10)

        user = quizzy_service.get_current_user()
        username_label = tkinter.Label(
            self.frame, text=f"Signed in as {user.username}", fg="black", bg="white")
        username_label.place(x=10, y=15)

        label = tkinter.Label(master=self.selection_frame,
                              text=f"Welcome to Quizzy, {user.username}!", fg="black", bg="white", font=("Arial", 25))
        label.place(x=450, y=30, anchor=constants.N)

        label2 = tkinter.Label(self.selection_frame, text="Please choose the amount of questions: ", fg="black", bg="white")
        label2.place(x=400, y=350, anchor=constants.N)

        num_options = [3,5,10]
        self.chosen = tkinter.StringVar()
        self.chosen.set(num_options[0])
        num = tkinter.OptionMenu(self.selection_frame, self.chosen, *num_options)
        num.place(x=580, y=350, anchor=constants.N)

        start_button = tkinter.Button(
            self.selection_frame, text="Start the quiz", command=self.start_handler, fg="white", bg="white")
        start_button.place(x=450, y=400, anchor=constants.N)

        self.selection_frame.place(x=600, y=100, anchor=constants.N)

    def start_handler(self):
        self.q_num = self.chosen.get()
        quizzy_service.set_number_of_questions(self.q_num)
        self.handle_start()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()
