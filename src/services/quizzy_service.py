import tkinter
from entities.user import User
from entities.question import Question

from repositories.user_repository import (
    user_repository as default_user_repository)
from repositories.question_repository import (
    question_repository as default_question_repository)


class InvalidCredentialsError(Exception):
    pass


class QuizzyService:
    def __init__(self, user_repository=default_user_repository, question_repository=default_question_repository):
        self.user_repository = default_user_repository
        self.question_repository = default_question_repository
        self.user = None
        self.number_of_questions = 5

    def create_user(self, username, password, logged_in=True):
        existing_user = self.user_repository.find_by_username(username)
        if existing_user:
            print("Username already exists")
        user = User(username, password, 0)
        new_user = self.user_repository.create(user)
        if logged_in:
            self.user = user
        return new_user

    def login(self, username, password):
        user = self.user_repository.find_by_username(username)
        if not user or user.password != password:
            raise InvalidCredentialsError('Invalid username or password')
        self.user = user
        return user

    def logout(self):
        self.user = None

    def get_current_user(self):
        return self.user

    def get_highscore(self):
        return self.user.highscore

    def get_users(self):
        return self.user_repository.find_all()

    def set_number_of_questions(self, n):
        self.number_of_questions = n

    def get_number_of_questions(self):
        return self.number_of_questions

    def get_questions(self):
        questions = self.question_repository.find_all()
        return questions

    def check_if_correct(self, question, chosen):
        if question.answer == chosen:
            return True
        else:
            return False

    def update_user_highscore(self, points):
        if points > self.user.highscore:
            self.user_repository.update_highscore(self.user.username, points)

    def next_question(self, q_num):
        q_num += 1
        return q_num

    def check_for_more_questions(self, q_num, questions):
        if q_num < len(questions):
            return True
        else:
            return False

    def restart_quiz(self, points, q_num):
        points = 0
        q_num = -1
        return points, q_num


quizzy_service = QuizzyService()
