from entities.user import User
from database_connection import get_database_connection


def get_users_by_row(row):
    return User(row["username"], row["password"], row["firstname"], row["lastname"]) if row else None


class UserRepository:

    """ Luokka, joka hoitaa käyttäjiin liittyvät tietokantatoiminnot. """

    def __init__(self, connection):
        self.connection = connection

    def create(self, user):

        """ Lisää uuden käyttäjän tietokantaan.

        Args:
            user: User-tyyppinen olio.
        Returns:
            Luodun User-olion.
        """

        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Users (username, password, firstname, lastname) values (?,?,?,?)",
                       (user.username, user.password, user.firstname, user.lastname))
        self.connection.commit()
        return user

    def find_by_username(self, username):

        """ Etsii tietokannasta käyttäjän parametrina annetun käyttäjänimen avulla.

        Args:
            username: Kuvastaa käyttäjän käyttäjätunnusta, tyypiltään String.
        Returns:
            User-olion, jos se on olemassa tietokannassa.
        """

        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
        row = cursor.fetchone()
        return get_users_by_row(row)

    def find_all(self):

        """ Etsii kaikki käyttäjät tietokannasta.

        Returns:
            Lista käyttäjistä.
        """

        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Users")
        rows = cursor.fetchall()
        return list(map(get_users_by_row, rows))

    def delete_all(self):

        """ Poistaa kaikki käyttäjät tietokannasta. """

        cursor = self.connection.cursor()
        cursor.execute('DELETE FROM Users')
        self.connection.commit()


user_repository = UserRepository(get_database_connection())
