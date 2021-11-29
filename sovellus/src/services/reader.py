class Reader:

    def __init__(self, document):
        self._document = document

    def download(self):
        countries_n_capitals = {}

        with open(self._document) as doc:
            for row in doc:
                parts = row.split(",")
                countries_n_capitals[parts[0]] = parts[1]

        return countries_n_capitals
