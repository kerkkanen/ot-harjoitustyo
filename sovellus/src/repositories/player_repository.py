from pathlib import Path
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
        """Lukee pisteet cvs-tiedostosta ja listaa pisteet-

        Returns:
            [list]: Lista, jossa rivillä on yhden pelikerran pelaajan pisteet, nimi ja pelin vaikeustaso
        """
        highscores = []
        if Path(self._file_path).stat().st_size != 0:
            with open(self._file_path, encoding="utf8") as file:
                for row in file:
                    if row != "":
                        parts = row.split(",")
                        score_info = [parts[0], parts[1], parts[2]]
                        highscores.append(score_info)

        return highscores

    def write_highscores(self, name, score, level):
        """Tallettaa cvs-tiedostoon pelin pelaajan, pisteet ja vaikeustason.

        Args:
            name (str): Pelin pelaajan nimimerkki
            score (str): Pelaajan pisteet
            level (str): Pelin vaikeustaso
        """
        with open(self._file_path, "a", encoding="utf8") as file:
            file.writelines(f"{score},{name},{level}\n")


player_repository = PlayerRepository(SCORE_FILE_PATH)
