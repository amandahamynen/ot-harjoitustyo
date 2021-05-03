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

    """ Sovelluksen sovelluslogiikasta vastaava luokka. """

    def __init__(self, user_repository=default_user_repository, question_repository=default_question_repository):

        """ Luokan konstruktori, joka luo sovelluslogiikasta vastaavan palvelun sovellukselle.

        Args:
            user_repository: Oletusarvoltaan UserRepository-olio, jolla on kyseistä luokkaa vastaavat metodit.
            question_repository: Oletusarvoltaan QuestionRepository-olio, jolla on kyseistä luokkaa vastaavat metodot.
        """

        self.user_repository = default_user_repository
        self.question_repository = default_question_repository
        self.user = None
        self.number_of_questions = 5

    def create_user(self, username, password, logged_in=True):

        """ Luo uuden käyttäjän ja kirjaa sen sisään.

        Args:
            username: Kuvastaa käyttäjän käyttäjätunnusta, tyypiltään String.
            password: Kuvastaa käyttäjän salasanaa, tyypiltään String.
            logged_in: Kertoo kirjataanko käyttäjä sisään onnistuneen sisäänkirjautumisen jälkeen, tyypiltään Boolean.

        Returns:
            User-olio.
        """

        existing_user = self.user_repository.find_by_username(username)
        if existing_user:
            print("Username already exists")
        user = User(username, password, 0)
        new_user = self.user_repository.create(user)
        if logged_in:
            self.user = user
        return new_user

    def login(self, username, password):

        """ Kirjaa käyttäjän sisään sovellukseen.

        Args:
            username: Kuvastaa käyttäjän käyttäjätunnusta, tyypiltään String.
            password: Kuvastaa käyttäjän salasanaa, tyypiltään String.

        Raises:
            InvalidCredentialsError: Jos käyttäjän syöttämä käyttäjätunnus ja salasana eivät tästää, tulee kyseinen virhe.

        Returns:
            Kirjautunut User-olio.
        """

        user = self.user_repository.find_by_username(username)
        if not user or user.password != password:
            raise InvalidCredentialsError('Invalid username or password')
        self.user = user
        return user

    def logout(self):

        """ Kirjaa nykyisen käyttäjän ulos sovelluksesta. """

        self.user = None

    def get_current_user(self):

        """ Palauttaa sovellukseen kirjautuneen käyttäjän.

        Returns:
            Sisään kirjautuneet User-olion.
        """

        return self.user

    def get_highscore(self):

        """ Palauttaa käyttäjän korkeimman pistemäärän.

        Returns:
            Käyttäjän korkein pistemäärä, tyypiltään Integer.
        """

        return self.user.highscore

    def get_users(self):

        """ Palauttaa kaikki sovellukseen rekisteröityneet käyttäjät.

        Returns:
            Listan User-olioista.
        """

        return self.user_repository.find_all()

    def set_number_of_questions(self, n):

        """ Asettaa kysymysten määräksi käyttäjän valitseman määrän. 
        Args:
            n: Kysymysten määrä, tyypiltään Integer.
        """

        self.number_of_questions = n

    def get_number_of_questions(self):

        """ Palauttaa kysymysten määrän.

        Returns:
            Kysymysten määrän, tyypiltään Integer.
        """

        return self.number_of_questions

    def get_questions(self):

        """ Palauttaa kaikki tiedostossa olevat kysymykset.

        Returns:
            Listan kysymyksistä.
        """

        questions = self.question_repository.find_all()
        return questions

    def check_if_correct(self, question, chosen):

        """ Tarkistaa, onko kysymykseen vastattu oikein.

        Args:
            question: Question-olio
            chosen: Käyttäjän valitsema vaihtoehto.
        Returns:
            Onko vastaus oikein, tyypiltään Boolean.
        """

        if question.answer == chosen:
            return True
        else:
            return False

    def update_user_highscore(self, points):

        """ Päivittää tarvittaessa sisään kirjautuneen käyttäjän korkeimman pistemäärän.
        Args:
            points = Käyttäjän saama pistemäärä pelistä.
        """

        if points > self.user.highscore:
            self.user_repository.update_highscore(self.user.username, points)

    def next_question(self, q_num):

        """ Kasvattaa kysymyksen numero yhdellä, jotta saadaan seuraava kysymys pelissä.
        Args:
            q_num = Nykyinen kysymysnumero, tyypiltään Integer.
        Returns:
            Kysymysnumeron, jota on yhden enemmän.
        """

        q_num += 1
        return q_num

    def check_for_more_questions(self, q_num, questions):

        """ Tarkistaa onko pelissä kysymyksiä jäljellä.
        Args:
            q_num = Nykyinen kysymysnumero, tyypiltään Integer.
            questions = Lista kysymyksistä
        Returns:
            Onko jäljellä kysymyksiä, tyypiltään Boolean.
        """

        if q_num < len(questions):
            return True
        else:
            return False

    def restart_quiz(self, points, q_num):

        """ Aloittaa pelin uudelleen.
        Args:
            points = Pelistä tähän asti saadut pisteet, tyypiltään Integer.
            q_num = Nykyinen kysymysnumero, tyypiltään Integer.
        Returns:
            Pisteet ja kysymysnumeron, jotka ovat nollattu.
        """

        points = 0
        q_num = -1
        return points, q_num


quizzy_service = QuizzyService()
