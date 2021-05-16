class User:

    """ Luokka, joka kuvaa yksittäistä käyttäjää sovelluksessa.
    Attributes:
        username: Kuvastaa käyttäjän käyttäjätunnusta, tyypiltään String.
        password: Kuvastaa käyttäjän salasanaa, tyypiltään String.
    """

    def __init__(self, username, password, firstname, lastname):
        """ Luokan konstruktori, joka luo uuden käyttäjän.
        Args:
            username: Kuvastaa käyttäjän käyttäjätunnusta, tyypiltään String.
            password: Kuvastaa käyttäjän salasanaa, tyypiltään String.
            highscore: Kuvastaa käyttäjän korkeintä pistemäärää, tyypiltään Integer.
        """

        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
