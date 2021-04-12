from tkinter import Tk, ttk
from ui.login_screen import LoginScreen
from ui.user_creation_screen import UserCreation
from ui.home_screen import HomeScreen

class UI():
    def __init__(self, root):
        self.root = root
        self.root.resizable(0,0)
        self.current = None

    def start(self):
        self.show_login_screen()

    def show_login_screen(self):
        self.hide_current()
        self.current = LoginScreen(self.root, self.show_home_screen, self.show_user_creation_screen)
        self.current.pack()

    def show_user_creation_screen(self):
        self.hide_current()
        self.current = UserCreation(self.root, self.show_home_screen, self.show_login_screen)
        self.current.pack()

    def show_home_screen(self):
        self.hide_current()
        self.current = HomeScreen(self.root, self.show_login_screen)
        self.current.pack()

    def hide_current(self):
        if self.current:
            self.current.destroy()
        self.current = None