from reader import Reader
from random import randint

class Countries:

    def __init__(self):
        self._reader = Reader("all.csv")
        self._cnc = self._reader.download()
        self._list = []
        self.countries_list()
        self._country = ""
        self._answer = ""
        self._options = []
        
    def countries_list(self):
        for country in self._cnc:
            self._list.append(country)

    def create_question(self, options):
        rndints = []
        while len(rndints)<options: 
            rnd = randint(0, len(self._list)-1)
            if rnd not in rndints:
                rndints.append(rnd)
        self._country = self._list[rndints.pop(0)]
        self._answer = self._cnc[self._country]        
        self.create_options(rndints)

    def create_options(self, list):
        self._options.clear()
        while len(list) > 0:
            country = self._list[list.pop(0)]
            self._options.append(self._cnc[country])
    
    def question(self):
        return self._country

    def answer(self):
        return self._cnc[self._country]    
    
    def other_options(self):
        return self._options         
   
    def check_answer(self, answer):
        if self._answer == answer:
            return True
        return False

c = Countries()
while True:        
    c.create_question(5)
    print(f"kysytty maa:  {c.question()}")
    vastaus = input("sen pääkaupunki? ")
    if vastaus == "-1":
        break
    if c.check_answer(vastaus):
        print("Oikein!")
    else:
        print(f"Väärin! Oikea vastaus on {c.answer()}")
    print("----------------------------")

