from reader import Reader
from random import randint
import random
from player import Player

class Game:

    def __init__(self, player, level):
        self._player = player
        self._level = level   

        self._reader = Reader("all.csv")
        self._countries_n_capitals = self._reader.download()

        self._country_list = []        
        self._country = ""
        self._capital = ""
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

    def create_options(self, list):
        self._capital_options.clear()
        while len(list) > 0:
            country = self._country_list[list.pop(0)]
            self._capital_options.append(self._countries_n_capitals[country])
    
    def country(self):
        return self._country

    def capital(self):
        return self._countries_n_capitals[self._country]    
    
    def other_capitals(self):
        self._capital_options.append(self._capital)
        random.shuffle(self._capital_options)
        return self._capital_options         
   
    def check_capital(self, answer):
        if self._capital == answer:
            self._player.add_score(50)
            return True
        return False

