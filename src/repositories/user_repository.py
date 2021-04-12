from entities.user import User
from database_connection import get_database_connection

def get_users_by_row(row):
    return User(row["username"], row["password"], row["highscore"]) if row else None

class UserRepository:
    
    def __init__(self, connection):
        self.connection = connection

    def create(self, user):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Users (username, password, highscore) values (?,?,?)", (user.username, user.password, 0))
        self.connection.commit()
        return user

    def find_by_username(self, username):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
        row = cursor.fetchone()
        return get_users_by_row(row)

    def find_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Users")
        rows = cursor.fetchall()
        return list(map(get_users_by_row, rows))

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM Users')
        self.connection.commit()

    def update_highscore(self, username, score):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE Users SET highscore = ? WHERE username = ?", (score, username))
        self.connection.commit()


user_repository = UserRepository(get_database_connection())