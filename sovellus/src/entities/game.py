
import random
from random import randint
from services.reader import Reader
from entities.player import Player


class Game:

    def __init__(self, player, level):
        self._player = player
        self._level = level

        self._reader = Reader("data/country_list_all.csv")
        self._countries_n_capitals = self._reader.download()

        self._country_list = []
        self._country = None
        self._capital = None
        self._capital_options = []

        self.countries_list()

    def countries_list(self):
        for country in self._countries_n_capitals:
            self._country_list.append(country)

    def create_question(self):
        rndints = []
        while len(rndints) < self._level:
            rnd = randint(0, len(self._country_list)-1)
            if rnd not in rndints:
                rndints.append(rnd)
        self._country = self._country_list[rndints.pop(0)]
        self._capital = self._countries_n_capitals[self._country]
        self.create_options(rndints)

    def create_options(self, option_nubmers):
        self._capital_options.clear()
        while len(option_nubmers) > 0:
            country = self._country_list[option_nubmers.pop(0)]
            self._capital_options.append(self._countries_n_capitals[country])

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        self._country = country

    @property
    def capital(self):
        return self._countries_n_capitals[self._country]

    @capital.setter
    def capital(self, capital):
        self._capital = capital

    def other_capitals(self):
        self._capital_options.append(self._capital)
        random.shuffle(self._capital_options)
        return self._capital_options

    def check_capital(self, answer):
        if self._capital == answer:
            self._player.add_score(50)
            return True
        return False

