from pathlib import Path
from config import COUNTRIES_FILE_PATH


class QuestionRepository:

    def __init__(self, file_path):
        self._file_path = file_path

    # Lukee tiedostosta maat ja pääkapungit sanakirjaan ja palauttaa sen
    def read_countries(self):
        countries_n_capitals = {}

        with open(self._file_path) as file:
            for row in file:
                parts = row.split(",")
                countries_n_capitals[parts[0]] = parts[1]

        return countries_n_capitals

    # palauttaa maat listalla
    def countries_list(self, countries_n_capitals):
        country_list = []
        for country in countries_n_capitals:
            country_list.append(country)

        return country_list


question_repository = QuestionRepository(COUNTRIES_FILE_PATH)
