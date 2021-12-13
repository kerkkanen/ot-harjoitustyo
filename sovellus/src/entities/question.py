class Question:
    """Luokkaan tallentuu yksittäinen kysymys, oikea vastaus ja vastausvaihtoehdot.
    """

    def __init__(self, country, capital, options):
        """Luokan konstruktori, joka luo uuden kysymyksen.

        Args:
            country (str): Kysyttävä maa
            capital (str): Vastaus eli oikea pääkaupunki
            options (str): Muut vastausvaihtoehdot
        """
        self._country = country
        self._capital = capital
        self._capital_options = options

    def country(self):
        return self._country

    def capital(self):
        return self._capital

    def options(self):
        return self._capital_options.pop(0)
