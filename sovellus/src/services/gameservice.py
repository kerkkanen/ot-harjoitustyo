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

    def __init__(self, level, name, area, sudden_death):
        """Luokan konstruktori, joka luo repositoriot kysymyksille ja pelaajalle

        Args:
            level (int): Pelin vaikeustason eli vastausvaihtoehtojen määrittävä arvo
            name (str): Pelaajan nimimerkki, jolla pisteet talletetaan
            area (str): Alue, jonka maista kysymykset tulevat
            sudden_death (bool): Tieto pelityypistä

        Attributes:
            question_repository: repositorio, joka huolehtii kysymyslistojen luomisesta
            player_repository: repositorio, joka huolehtii pisteiden lukemisesta ja tallettamisesta
            question: entiteetti, joka säilöö yhden kysymyksen tiedot
            cnc_dict: sanakirja, jossa avaimina maat ja arvoina pääkaupungit
            country_list: lista maista
            asked: joukko jo kysytyistä maista
        """

        self._question_repository = default_question_repository
        self._player_repository = default_player_repository

        self._question = None
        self._player = Player(name)
        self._level = int(level)
        self._area = area
        self._sudden_death = sudden_death

        self._cnc_dict = self._question_repository.read_countries()
        self._country_list = self._question_repository.countries_list(
            self._cnc_dict, self._area)
        self._asked = set()

    def create_question(self):
        """Kutsuu uuden kysymyksen luovaa metodia kunnes valittuna on maa, jota ei ole jo kysytty.
        """
        while True:
            self._new_question()
            if self._question.country() not in self._asked:
                break
        self._asked.add(self._question.country())

    def _new_question(self):
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
            bool: Onko vastaus oikein vai väärin
        """
        time = math.floor(time*100)/100
        if self._question.capital() == answer:
            self._player.add_score(time, self._sudden_death)
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

    def sudden_death(self):
        return self._sudden_death

    def rounds_left(self):
        return len(self._asked) < len(self._country_list)

    def save_score(self):
        """Kutsuu player-repositorion pisteitä tiedostoon kirjoittavaa metodia.
        """
        if self._sudden_death:
            death_tick = "yes"
        else:
            death_tick = "no"
        self._player_repository.write_highscores(
            self.player_name(), str(self.player_score()), self.level_to_words(), self._area, death_tick)

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

    def get_sudden_death_highscores(self):
        return self.get_scorelist(True)

    def get_normal_highscores(self):
        return self.get_scorelist(False)

    def get_scorelist(self, sudden_death):
        """Luo listan, jolla on parametrin mukaisesti pelattujen pelien pistetiedot.

        Args:
            sudden_death (bool): Tieto pelistä, jonka pisteet halutaan listalle.

        Returns:
            list: Lista, jonka rivillä on pelaajan nimimerkki, pelatun pelin vaikeustaso ja pisteet / "TYHJÄ".
        """
        highscores = self._player_repository.read_highscores()
        highscores.sort()
        highscores.reverse()

        score_list = []

        for score in highscores:
            if sudden_death:
                if score[4] == "yes":
                    score_list.append(
                        f"{score[1]}\n{score[2]}\n {score[3]}\n{score[0]} peräkkäin")
            else:
                if score[4] == "no":
                    score_list.append(
                        f"{score[1]}\n{score[2]}\n {score[3]}\n{score[0]}")

        while len(score_list) < 3:
            score_list.append("TYHJÄ")

        return score_list

    def get_score(self, scores):
        """Hakee yhden rivin pistetilastoon.

        Args:
            scores (list): Lista, jolla on kaikki pisteet

        Returns:
            str: Listan ensimmäisen eli eniten pisteitä saaneen tiedot (nimi, pelin taso, pisteet)
        """
        return scores.pop(0)
