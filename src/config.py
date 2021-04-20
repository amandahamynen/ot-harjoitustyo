import os

dirname = os.path.dirname(__file__)

DATABASE_FILENAME = os.getenv('DATABASE_FILENAME') or 'database.sqlite'
DATABASE_FILE_PATH = os.path.join(dirname, '..', 'data', DATABASE_FILENAME)

QUESTIONS_FILENAME = os.getenv('QUESTIONS_FILENAME') or 'questions.csv'
QUESTIONS_FILE_PATH = os.path.join(dirname, '..', 'data', QUESTIONS_FILENAME)
