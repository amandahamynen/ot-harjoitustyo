import unittest
from repositories.question_repository import question_repository


class TestQuestionRepository(unittest.TestCase):
    def test_find_all(self):
        questions = question_repository.find_all()
        self.assertEqual(len(questions), 30)
