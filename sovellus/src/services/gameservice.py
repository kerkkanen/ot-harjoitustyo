from random import randint
from random import shuffle
import math
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
        self._highscores = None

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

    def check_capital(self, answer, time):
        time = math.floor(time*100)/100
        if self._question.capital() == answer:
            self._player.add_score(time)
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

    def save_score(self):
        self._player_repository.write_highscores(
            self.player_name(), str(self.player_score()), self.level())

    def level(self):
        if self._level == 2:
            return "helppo"
        if self._level == 3:
            return "normaali"
        return "vaikea"

    def get_highscores(self):
        self._highscores = self._player_repository.read_highscores()
        self._highscores.sort()
        self._highscores.reverse()

        score_list = []

        index = 0
        for score in self._highscores:
            if index == 5:
                break
            score_list.append(f"{score[1]}\n{score[2]}\n{score[0]}")
            index += 1
        while len(score_list) < 3:
            score_list.append("TYHJÄ")
        return score_list

    def get_score(self, scores):
        return scores.pop(0)
