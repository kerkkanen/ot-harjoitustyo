class Question:

    def __init__(self, country, capital, options):
        self._country = country
        self._capital = capital
        self._capital_options = options

    def country(self):
        return self._country

    def capital(self):
        return self._capital

    def options(self):
        return self._capital_options.pop(0)
