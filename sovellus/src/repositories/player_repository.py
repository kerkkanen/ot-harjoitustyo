from pathlib import Path
from config import SCORE_FILE_PATH


class PlayerRepository:

    def __init__(self, file_path):
        self._file_path = file_path

    def read_highscores(self):
        highscores = {}

        with open(self._file_path) as file:
            for row in file:
                parts = row.split(",")
                highscores[parts[0]] = parts[1]

        return highscores

    # def write_high_scores(self):
        # with open(self._file_path, "w") as file:


player_repository = PlayerRepository(SCORE_FILE_PATH)
