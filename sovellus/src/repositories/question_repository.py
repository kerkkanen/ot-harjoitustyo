from pathlib import Path
from config import COUNTRIES_FILE_PATH


class QuestionRepository:
    """Luokka huolehtii maiden tietojen lukemisesta ja listaamisesta.
    """

    def __init__(self, file_path):
        """Luokan konstruktori.

        Args:
            file_path : Polku tiedostoon, josta maat löytyvät
        """
        self._file_path = file_path

    def read_countries(self):
        """Avaa cvs-tiedoston, jossa tieto maista pääkaupunkeineen ja maanosineen.

        Returns:
            dict: Sanakirja, jossa avaimena maa, arvona pääkaupunki
        """
        countries_n_capitals = {}

        with open(self._file_path, encoding="utf8") as file:
            for row in file:
                parts = row.split(",")
                countries_n_capitals[parts[0]] = [parts[1], parts[2].strip()]

        return countries_n_capitals

    def countries_list(self, countries_n_capitals, area):
        """Listaa maat pelialueen mukaan.

        Args:
            countries_n_capitals (list): Lista maista

        Returns:
            list: Lista, jossa kaikki maat
        """
        country_list = []
        if area == "Maailma":
            for country in countries_n_capitals:
                country_list.append(country)
        else:
            for country in countries_n_capitals:
                if countries_n_capitals[country][1] == area:
                    country_list.append(country)
        return country_list


question_repository = QuestionRepository(COUNTRIES_FILE_PATH)
