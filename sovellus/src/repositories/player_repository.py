from pathlib import Path
from config import SCORE_FILE_PATH


class PlayerRepository:

    def __init__(self, file_path):
        self._file_path = file_path

    def read_highscores(self):
        highscores = []

        with open(self._file_path) as file:
            for row in file:
                parts = row.split(",")
                score_info = [parts[0], parts[1], parts[2]]
                highscores.append(score_info)

        return highscores

    def write_highscores(self, name, score, level):
        with open(self._file_path, "w") as file:
            file.write(f"{score},{name},{level}\n")


player_repository = PlayerRepository(SCORE_FILE_PATH)
