import os
from config import SCORE_FILE_PATH


class PlayerRepository:
    """Luokka, joka huolehtii pisteiden lukemisesta ja tallentamisesta.
    """

    def __init__(self, file_path):
        """Luokan konstruktori

        Args:
            file_path : Polku tiedostoon, josta pisteet löytyvät ja jonne ne talletetaan
        """
        self._file_path = file_path

    def read_highscores(self):
        """Lukee pisteet cvs-tiedostosta ja listaa pisteet.

        Returns:
            list: Lista, jossa rivillä on yhden pelikerran pelaajan
            pisteet, nimi ja pelin vaikeustaso
        """
        highscores = []

        with open(self._file_path, encoding="utf8") as file:

            if os.stat(self._file_path).st_size == 0:
                return highscores

            for row in file:
                if len(row) > 5:
                    parts = row.split(",")
                    score_info = [int(parts[0]), parts[1].strip(
                    ), parts[3].strip(), parts[2].strip(), parts[4].strip()]
                    highscores.append(score_info)

        return highscores

    def write_highscores(self, name, score, level, area, sudden_death):
        """Tallettaa cvs-tiedostoon pelin pelaajan, pisteet ja vaikeustason.

        Args:
            name (str): Pelin pelaajan nimimerkki
            score (str): Pelaajan pisteet
            level (str): Pelin vaikeustaso
            sudden_death (str): Tieto pelin tyypistä
        """
        with open(self._file_path, "a", encoding="utf8") as file:
            file.writelines(f"{score},{name},{level},{area},{sudden_death}\n")

    def delete_all(self):
        with open(self._file_path, "w", encoding="utf8") as file:
            pass


player_repository = PlayerRepository(SCORE_FILE_PATH)
