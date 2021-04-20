from entities.question import Question
from config import QUESTIONS_FILE_PATH


class QuestionRepository:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        questions = []
        with open(self.file_path) as file:
            for row in file:
                row = row.replace('\n', '')
                parts = row.split(',')

                question = parts[0]
                options = parts[1:-1]
                answer = parts[-1]

                questions.append(Question(question, options, answer))
        return questions

    def find_all(self):
        return self.read()


question_repository = QuestionRepository(QUESTIONS_FILE_PATH)
