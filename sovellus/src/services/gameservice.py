from random import randint
from entities.game import Game
from entities.player import Player


class GameService:

    def __init__(self, player, level):
        self._player = Player(player)
        self._game = Game(player, level)
        self._options = []

    def new_question(self):
        self._game.create_question()

    def country(self):
        return self._game.country()

    def capital(self):
        return self._game.capital()

    def capital_options(self):
        for option in self._game.other_capitals():
            self._options.append(option)

    def option(self):
        return self._options.pop(randint(0, len(self._options)-1))

    def check_if_correct(self, answer):
        return self._game.check_capital(answer)
