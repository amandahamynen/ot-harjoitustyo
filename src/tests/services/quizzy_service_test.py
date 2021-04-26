import unittest
from entities.question import Question
from entities.user import User
from services.quizzy_service import QuizzyService, InvalidCredentialsError

class FakeUserRepository:
    def __init__(self, users = None):
        self.users = users or []

    def find_all(self):
        return self.users

    def find_by_username(self, username):
        matching_users = filter(
            lambda user: user.username == username,
            self.users
        )

        matching_users_list = list(matching_users)

        return matching_users_list[0] if len(matching_users_list) > 0 else None

    def create(self, user):
        self.users.append(user)

        return user

    def delete_all(self):
        self.users = []


class FakeQuestionRepository:
    def __init__(self, questions = None):
        self.questions = questions or []

    def find_all(self):
        return self.questions


class TestQuizzyService(unittest.TestCase):
    def setUp(self):
        self.quizzy_service = QuizzyService(FakeUserRepository(), FakeQuestionRepository())
        self.user_amanda = User("amanda", "a123", 0)
        self.question = Question("q", ["1","2","3","4"],"1")

    def login_user(self, user):
        self.quizzy_service.create_user(user.username, user.password)

    def test_login_with_correct_username_and_password(self):
        self.quizzy_service.create_user("testi_username", "testi_password")
        user = self.quizzy_service.login("testi_username", "testi_password")
        self.assertEqual(user.username, "testi_username")

    def test_login_with_incorrect_username_or_password(self):
        self.assertRaises(InvalidCredentialsError, lambda: self.quizzy_service.login("wrong", "username_or_password"))

    def test_get_current_user(self):
        self.login_user(self.user_amanda)
        user = self.quizzy_service.get_current_user()
        self.assertEqual(user.username, self.user_amanda.username)

    