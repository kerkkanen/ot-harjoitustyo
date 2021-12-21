
class Player:
    """Luokan avulla pidetään tietoa pelin pelaajasta.
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

    def add_score(self, time, sudden_death):
        """Lisää pelaajalle pisteitä oikeasta vastauksesta käytetyn vastausajan mukaan
            tai yhden pisteen oikeasta maasta.
        """

        if sudden_death:
            self._score += 1
        else:
            if time < 0.8:
                self._score += 150
            elif time < 1:
                self._score += 135
            elif time < 1.2:
                self._score += 120
            elif time < 1.5:
                self._score += 105
            elif time <= 2:
                self._score += 90
            elif time < 2.5:
                self._score += 75
            elif time <= 3:
                self._score += 60
            elif time < 4:
                self._score += 45
            elif time < 5:
                self._score += 30
            elif time < 6:
                self._score += 15
            else:
                self._score += 5
