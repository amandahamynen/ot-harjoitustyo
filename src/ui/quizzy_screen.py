import random
from tkinter import Label, StringVar, ttk, Tk, constants
import tkinter
from entities.question import Question
from services.quizzy_service import quizzy_service

points = 0
q_num = 0


class QuizzyScreen:
    def __init__(self, root, handle_back):
        self.root = root
        self.handle_back = handle_back
        self.how_many = 5
        self.questions = []
        self.frame = None
        self.question_frame = None
        self.question_view = None
        self.initialize_questions()
        self.initialize()

    def initialize_questions(self):
        global points
        points = 0
        self.how_many = int(quizzy_service.get_number_of_questions())
        self.questions = quizzy_service.get_questions()
        random.shuffle(self.questions)
        self.questions = [x for index, x in enumerate(self.questions) if index < self.how_many]

    def initialize(self):
        global points
        self.frame = tkinter.Frame(self.root, width=1200, height=700)
        self.question_frame = tkinter.Frame(self.root, bg="white")

        go_back_button = tkinter.Button(
            self.frame, text="Return to homescreen", command=self.back_handler)
        go_back_button.place(x=1000, y=10)

        self.initialize_question_view()
        self.question_frame.place(x=600, y=200, anchor=constants.N)

    def initialize_question_view(self):
        global q_num
        global points
        if self.question_view:
            self.question_view.destroy()
        if quizzy_service.check_for_more_questions(q_num, self.questions):
            question = self.questions[q_num]
            self.question_view = QuestionView(
                self.question_frame, question, self.initialize_question_view)
            self.question_view.pack()
        else:
            result = tkinter.Label(
                self.question_frame, text=f"You got {points}/{len(self.questions)} right!", fg="black", bg="white")
            result.pack()
            quizzy_service.update_user_highscore(points)
            end = tkinter.Label(
                self.question_frame, text=f"Please return to homescreen", fg="black", bg="white")
            end.pack()
            points, q_num = quizzy_service.restart_quiz(points, q_num)
        q_num = quizzy_service.next_question(q_num)

    def back_handler(self):
        global q_num 
        global points
        q_num = 0
        points = 0
        self.handle_back()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()


class QuestionView:
    def __init__(self, root, question: Question, handle_next):
        self.root = root
        self.question = question
        self.handle_next = handle_next
        self.frame = None
        self.answerd = False
        self.submit = None
        self.next = None
        self.initialize()

    def initialize(self):
        global q_num
        self.frame = tkinter.Frame(self.root, bg="white")
        q = tkinter.Label(
            self.frame, text=f"{q_num+1}. {self.question.question}", fg="black", bg="white", padx=200, pady=20)
        q.pack()
        var = tkinter.StringVar()
        var.set(self.question.options[0])
        for opt in self.question.options:
            tkinter.Radiobutton(self.frame, text=opt, variable=var,
                                value=opt, fg="black", bg="white", pady=5).pack()
        self.submit = tkinter.Button(self.frame, text="Submit", command=lambda: self.handle_submit(
            var.get()), fg="white", bg="white", bd=0)
        self.submit.pack()

    def handle_submit(self, value):
        global points
        global q_num
        if not self.answerd:
            if quizzy_service.check_if_correct(self.question, value):
                points += 1
                right_answer = tkinter.Label(
                    self.frame, text=f"You got a point!", fg="black", bg="white")
                right_answer.pack()
            else:
                wrong_answer = tkinter.Label(
                    self.frame, text=f"Answer was wrong\nRight answer was {self.question.answer}", fg="black", bg="white")
                wrong_answer.pack()
            self.submit.destroy()
            self.next = tkinter.Button(
                self.frame, text="Next question", command=self.handle_next, fg="white", bg="white", bd=0)
            self.next.pack()
        self.answerd = True

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()
