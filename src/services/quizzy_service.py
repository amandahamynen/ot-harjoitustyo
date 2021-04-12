import tkinter
from entities.user import User

from repositories.user_repository import (user_repository as default_user_repository)

class InvalidCredentialsError(Exception):
    pass

class QuizzyService:
    def __init__(self, user_repository = default_user_repository):
        self.user_repository = default_user_repository
        self.user = None

    def create_user(self, username, password, logged_in = True):
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

        
quizzy_service = QuizzyService()