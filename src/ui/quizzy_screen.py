import random
from tkinter import constants
import tkinter
from entities.question import Question
from services.quizzy_service import quizzy_service

points = 0
q_num = 0


class QuizzyScreen:

    """ Luokka näkymälle, jossa käyttäjä voi pelata tietovisaa.

    Luokka tarjoaa näkymän, jossa käyttäjä pelaa tietovisaa kotinäytöllä määritettyjen asetusten mukaisesti.
    Tietovisassa käyttäjä voi vastata kysymykseen valitsemalla yhden neljästä vastausvaihtoehdosta. Käyttäjä
    saa pisteen jokaisesta oikeasta vastauksesta, ja näkee tietovisan lopuksi saamansa pistemäärän.
    """

    def __init__(self, root, handle_back):
        self._root = root
        self._handle_back = handle_back
        self._how_many = 5
        self._questions = []
        self._frame = None
        self._question_frame = None
        self._question_view = None
        self._bg = tkinter.PhotoImage(
            file="src/resources/boat-5889919_1280.png")
        self._initialize_questions()
        self._initialize()

    def _initialize_questions(self):
        global points
        points = 0
        self._how_many = int(quizzy_service.get_number_of_questions())
        self._questions = quizzy_service.get_questions()
        random.shuffle(self._questions)
        self._questions = [x for index, x in enumerate(
            self._questions) if index < self._how_many]

    def _initialize(self):
        global points
        self._frame = tkinter.Frame(self._root, width=1200, height=700)
        self._question_frame = tkinter.Frame(self._root, bg="white")

        label_bg = tkinter.Label(master=self._frame, image=self._bg)
        label_bg.place(x=0, y=0)

        go_back_button = tkinter.Button(
            self._frame, text="Return to homescreen", command=self._back_handler)
        go_back_button.place(x=1000, y=10)

        self._initialize_question_view()
        self._question_frame.place(x=600, y=200, anchor=constants.N)

    def _initialize_question_view(self):
        global q_num
        global points
        if self._question_view:
            self._question_view.destroy()
        if quizzy_service.check_for_more_questions(q_num, self._questions):
            question = self._questions[q_num]
            self._question_view = QuestionView(
                self._question_frame, question, self._initialize_question_view)
            self._question_view.pack()
        else:
            result = tkinter.Label(
                self._question_frame, text=f"You got {points}/{len(self._questions)} right!", fg="black", bg="white")
            result.pack()
            end = tkinter.Label(
                self._question_frame, text=f"Please return to homescreen", fg="black", bg="white")
            end.pack()
            points, q_num = quizzy_service.restart_quiz(points, q_num)
        q_num = quizzy_service.next_question(q_num)

    def _back_handler(self):
        global q_num
        global points
        q_num = 0
        points = 0
        self._handle_back()

    def pack(self):
        """ Pakkaa kehyksen. """

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """ Tuohoaa kehyksen. """

        self._frame.destroy()


class QuestionView:
    def __init__(self, root, question: Question, handle_next):
        self._root = root
        self._question = question
        self._handle_next = handle_next
        self._frame = None
        self._answerd = False
        self._submit = None
        self._next = None
        self._initialize()

    def _initialize(self):
        global q_num
        self._frame = tkinter.Frame(self._root, bg="white")
        q = tkinter.Label(
            self._frame, text=f"{q_num+1}. {self._question.question}", fg="black", bg="white", padx=200, pady=20)
        q.pack()
        var = tkinter.StringVar()
        var.set(self._question.options[0])
        for opt in self._question.options:
            tkinter.Radiobutton(self._frame, text=opt, variable=var,
                                value=opt, fg="black", bg="white", pady=5).pack()
        self.submit = tkinter.Button(self._frame, text="Submit", command=lambda: self._handle_submit(
            var.get()), fg="white", bg="white", bd=0)
        self.submit.pack()

    def _handle_submit(self, value):
        global points
        global q_num
        if not self._answerd:
            if quizzy_service.check_if_correct(self._question, value):
                points += 1
                right_answer = tkinter.Label(
                    self._frame, text=f"You got a point!", fg="black", bg="white")
                right_answer.pack()
            else:
                wrong_answer = tkinter.Label(
                    self._frame, text=f"Answer was wrong\nRight answer was {self._question.answer}", fg="black", bg="white")
                wrong_answer.pack()
            self.submit.destroy()
            self.next = tkinter.Button(
                self._frame, text="Next question", command=self._handle_next, fg="white", bg="white", bd=0)
            self.next.pack()
        self.answerd = True

    def pack(self):
        """ Pakkaa kehyksen. """

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """ Tuohoaa kehyksen. """

        self._frame.destroy()
