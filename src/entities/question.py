class Question:

    """ Luokka, joka kuvaa yksittäistä kysymystä.
    Attributes:
        question: Kysymys, tyypiltään String.
        options: Vastaus vaihtoehdot kysymykseen, tyypiltään lista.
        answer:  Oikea vastaus kysymykseen vaihtoehdoista, tyypiltään String.
    """

    def __init__(self, question, options, answer):

        """ Luokan konstruktori, joka luo uuden kysymyksen.
        Args:
            question: Kysymys, tyypiltään String.
            options: Vastaus vaihtoehdot kysymykseen, tyypiltään lista.
            answer: Oikea vastaus kysymykseen vaihtoehdoista, tyypiltään String.
        """

        self.question = question
        self.options = options
        self.answer = answer
