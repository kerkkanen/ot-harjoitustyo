from random import randint
from random import shuffle
from entities.question import Question
from entities.player import Player

from repositories.question_repository import(
    question_repository as default_question_repository
)
from repositories.player_repository import(
    player_repository as default_player_repository
)


class GameService:

    def __init__(self, level, name):

        self._question_repository = default_question_repository
        self._player_repository = default_player_repository

        self._question = None
        self._player = Player(name)
        self._level = int(level)

        self._cnc_dict = self._question_repository.read_countries()
        self._country_list = self._question_repository.countries_list(
            self._cnc_dict)

    def create_question(self):
        rndints = []
        while len(rndints) < int(self._level):
            rnd = randint(0, len(self._country_list)-1)
            if rnd not in rndints:
                rndints.append(rnd)
        country = self._country_list[rndints.pop(0)]
        capital = self._cnc_dict[country]
        options = self.create_options(rndints)
        options.append(capital)
        shuffle(options)
        self._question = Question(country, capital, options)

    def create_options(self, option_nubmers):
        capital_options = []
        while len(option_nubmers) > 0:
            country = self._country_list[option_nubmers.pop(0)]
            capital_options.append(self._cnc_dict[country])
        return capital_options

    def check_capital(self, answer):
        if self._question.capital() == answer:
            self._player.add_score(50)
            return True
        return False

    def country(self):
        return self._question.country()

    def capital(self):
        return self._question.capital()

    def option(self):
        return self._question.options()

    def player_name(self):
        return self._player.name()

    def player_score(self):
        return self._player.score()
