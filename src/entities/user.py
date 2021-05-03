class User:

    """ Luokka, joka kuvaa yksittäistä käyttäjää sovelluksessa.
    Attributes: 
        username: Kuvastaa käyttäjän käyttäjätunnusta, tyypiltään String.
        password: Kuvastaa käyttäjän salasanaa, tyypiltään String.
        highscore: Kuvastaa käyttäjän korkeintä pistemäärää, tyypiltään Integer.
    """

    def __init__(self, username, password, highscore):

        """ Luokan konstruktori, joka luo uuden käyttäjän.
        Args:
            username: Kuvastaa käyttäjän käyttäjätunnusta, tyypiltään String.
            password: Kuvastaa käyttäjän salasanaa, tyypiltään String.
            highscore: Kuvastaa käyttäjän korkeintä pistemäärää, tyypiltään Integer.
        """

        self.username = username
        self.password = password
        self.highscore = highscore
