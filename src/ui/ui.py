""" UI-luokkien päämoduuli, joka suorittaa näkymien näkymisen ja vaihtumisen. """

from ui.login_screen import LoginScreen
from ui.user_creation_screen import UserCreation
from ui.home_screen import HomeScreen
from ui.quizzy_screen import QuizzyScreen


class UI():
    def __init__(self, root):
        self._root = root
        self._root.resizable(0, 0)
        self._current = None

    def start(self):
        """ Käynnistää sovelluksen ensimmäisen näkymän, joka on kirjautumisnäkymä. """

        self._show_login_screen()

    def _show_login_screen(self):
        self._hide_current()
        self._current = LoginScreen(
            self._root, self._show_home_screen, self._show_user_creation_screen)
        self._current.pack()

    def _show_user_creation_screen(self):
        self._hide_current()
        self._current = UserCreation(
            self._root, self._show_home_screen, self._show_login_screen)
        self._current.pack()

    def _show_home_screen(self):
        self._hide_current()
        self._current = HomeScreen(
            self._root, self._show_login_screen, self._show_quiz_screen)
        self._current.pack()

    def _show_quiz_screen(self):
        self._hide_current()
        self._current = QuizzyScreen(self._root, self._show_home_screen)
        self._current.pack()

    def _hide_current(self):
        if self._current:
            self._current.destroy()
        self._current = None
