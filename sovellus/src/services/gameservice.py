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
    """Luokka, joka huolehtii pelin logiikasta: kysymyksien luomisesta, tarkistamisesta ja pelaajan pisteitstä.
    """

    def __init__(self, level, name, area):
        """Luokan konstruktori, joka luo repositoriot kysymyksille ja pelaajalle

        Args:
            level (int): Pelin vaikeustason eli vastausvaihtoehtojen määrittävä arvo
            name (str): Pelaajan nimimerkki, jolla pisteet talletetaan
            area (str): Alue, jonka maista kysymykset tulevat

        Attributes:
            question_repository: repositorio, joka huolehtii kysymyslistojen luomisesta
            player_repository: repositorio, joka huolehtii pisteiden lukemisesta ja tallettamisesta
            question: entiteetti, joka säilöö yhden kysymyksen tiedot
            cnc_dict: sanakirja, jossa avaimina maat ja arvoina pääkaupungit
            country_list: lista maista
            highscores: lista kaikista pisteistä
        """

        self._question_repository = default_question_repository
        self._player_repository = default_player_repository

        self._question = None
        self._player = Player(name)
        self._level = int(level)
        self._area = area

        self._cnc_dict = self._question_repository.read_countries()
        self._country_list = self._question_repository.countries_list(
            self._cnc_dict, self._area)
        self._highscores = None

    def create_question(self):
        """Luo uuden kysymyksen: arvotaan maa, asetetaan oikea pääkaupunki ja luodaan väärät vastausvaihtoehdot.
        """
        rndints = []
        while len(rndints) < int(self._level):
            rnd = randint(0, len(self._country_list)-1)
            if rnd not in rndints:
                rndints.append(rnd)
        country = self._country_list[rndints.pop(0)]
        capital = self._cnc_dict[country][0]
        options = self.create_options(rndints)
        options.append(capital)
        shuffle(options)
        self._question = Question(country, capital, options)

    def create_options(self, option_numbers):
        """Luo kysymykselle väärät vastausvaihtoehdot.

        Args:
            option_nubmers (int): Peliin tarvittava vastausvaihtoehtojen määrä

        Returns:
            list: Lista vääristä vastausvaihtoehdoista
        """
        capital_options = []
        while len(option_numbers) > 0:
            country = self._country_list[option_numbers.pop(0)]
            capital_options.append(self._cnc_dict[country][0])
        return capital_options

    def check_capital(self, answer, time):
        """Tarkistaa, onko vastaus oikea ja kutsuu pisteitä tallettavaa metodia player-luokassa.

        Args:
            answer (str): Pelaajan valitsema vastaus
            time (float): [Vastauksen valitsemiseen kulunut aika

        Returns:
            boolean: Onko vastaus oikein vai väärin
        """
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

    def level(self):
        return self._level

    def save_score(self):
        """Kutsuu player-repositorion pisteitä tiedostoon kirjoittavaa metodia.
        """
        self._player_repository.write_highscores(
            self.player_name(), str(self.player_score()), self.level_to_words(), self._area)

    def level_to_words(self):
        """Muuntaa pelitason sanalliseen muotoon.

        Returns:
            str: Pelin vaikeustaso
        """
        if self._level == 2:
            return "helppo"
        if self._level == 3:
            return "normaali"
        return "vaikea"

    def get_highscores(self):
        """Luo listan, jolla on kaikkien pelattujen pelien pistetiedot.

        Returns:
            list: Lista, jonka rivillä on pelaajan nimimerkki, pelatun pelin vaikeustaso ja pisteet / "TYHJÄ".
        """
        self._highscores = self._player_repository.read_highscores()
        self._highscores.sort()
        self._highscores.reverse()

        score_list = []

        index = 0
        for score in self._highscores:
            if index == 3:
                break
            score_list.append(
                f"{score[1]}\n{score[2]}\n {score[3]}\n{score[0]}")
            index += 1
        while len(score_list) < 3:
            score_list.append("TYHJÄ")
        return score_list

    def get_score(self, scores):
        """Hakee yhden rivin pistetilastoon.

        Args:
            scores (list): Lista, jolla on kaikki pisteet

        Returns:
            [str]: Listalla olevan parhaiten pisteitä saaneen tiedot (nimi, pelin taso, pisteet)
        """
        return scores.pop(0)
