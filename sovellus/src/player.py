class Player:

    def __init__(self, name):
        self._name = name
        self._score = 0

    def name(self):
        return self._name

    def score(self):
        return self._score

    def add_score(self, points):
        self._score += points