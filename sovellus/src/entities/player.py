
class Player:
    """Luokka, jonka avulla pidetään tietoa pelin pelaajasta.
    """

    def __init__(self, name):
        """Luokan konstruktori, joka luo pelaajan ja alkupisteet.

        Args:
            name (str): Pelaajan nimimerkki
            score (float): Pelaajan alkupisteet
        """

        self._name = name
        self._score = 0

    def name(self):
        return self._name

    def score(self):
        return self._score

    def add_score(self, time):
        """Lisää pelaajalle pisteitä oikeasta vastauksesta käytetyn vastausajan mukaan.
        """

        if time < 1:
            self._score += 100
        elif time < 1.2:
            self._score += 95
        elif time < 1.5:
            self._score += 90
        elif time < 2:
            self._score += 85
        elif time < 3:
            self._score += 70
        elif time < 4:
            self._score += 60
        elif time < 5:
            self._score += 50
        elif time < 6:
            self._score += 40
        elif time < 7:
            self._score += 30
        elif time < 9:
            self._score += 20
        else:
            self._score += 10
