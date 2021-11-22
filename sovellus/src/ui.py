from game import Game
from player import Player
import tkinter as tk


class UI:

    def __init__(self, root):
        self._root = root

    def start(self):
        label = tk.Label(
            master=self._root,            
            text="Syötä nimimerkki",
            foreground="black",
            background="orange",
            width=120,
            height=40
        )
        label.pack()

   # def __init__(self):        
    #    pass

    def txt_ui(self):
        name = input("Syötä nimimerkki: ")
        player = Player(name)
        game = Game(player, 5)
        print("Pelataan 10 kierrosta. Oikeasta vastauksesta jaa 50 pistettä, väärästä 0.")
        print()
        for i in range(5):
            game.create_question()
            print("??????????????????????????????????????????????????")
            print(f"Mikä on maan {game.country} pääkaupunki  ")
            print("??????????????????????????????????????????????????")
            print()           
            for capital in game.other_capitals():
                print(capital)
            print()
            vastaus = input("Vastaus ")
            print()
            if game.check_capital(vastaus):
                print("***************")
                print("**  Oikein!  **")
                print("***************")
                print()
            else:
                print("---------------------------------------------")
                print(f"Väärin! Oikea vastaus on {game.capital}")
                print("---------------------------------------------")
                print()

        print(f"Pelaajan {player.name()} pisteet: ***{player.score()}***")
        

    def highscore_view(self):
        pass


