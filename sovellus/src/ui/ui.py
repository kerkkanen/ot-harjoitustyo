from ui.score_view import ScoreView
from ui.start_view import StartView
from ui.game_view import GameView
from entities.game import Game
from entities.player import Player



class UI:

    # def __init__(self):
    #   self.txt_ui()

    def __init__(self, root):
        self._root = root
        self._current_view = None
        

    def start(self):
        self._show_start_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    # handelers

    def _handle_start_game(self):
        print("hello")
        self._show_game_view()

    # show_views

    def _show_start_view(self):
        self._hide_current_view()

        self._current_view = StartView(
            self._root,
            self._show_game_view
        )
        self._current_view.pack()

    def _show_game_view(self):
        self._hide_current_view()

        self._current_view = GameView(
            self._root,
            self._show_score_view
        )
        self._current_view.pack()

    def _show_score_view(self):
        self._hide_current_view()

        self._current_view = ScoreView(
            self._root,
            self._show_start_view
        )
        self._current_view.pack()

    def txt_ui(self):
        while True:            
            answer = input("Pelaa (1) tai lopeta (2)")
            if answer == "2":
                break
            while True:
                name = input("Syötä nimimerkki (nimimerkki ei voi olla tyhjä):\n")
                if len(name) > 0:
                    break
            rounds = 0
            while True:
                try:
                    answer = int(input("Valitse kierrosten määrä (1-10)\n"))
                except ValueError:
                    answer = -1
                if 1 <= answer <= 10:
                    rounds = answer
                    break
            level = 0            
            while True:
                diff = input("Valitse vaikeustaso: helppo(h), keskitaso(k), vaikea(v)\n")
                if diff == "h":
                    level = 2
                    break
                if diff == "k":
                    level = 3
                    break
                if diff == "v":
                    level = 5
                    break
            player = Player(name)
            game = Game(player, level)
            print(f"Pelataan {rounds} kierrosta. Oikeasta vastauksesta saat 50 pistettä, väärästä 0.")
            print()
            for i in range(1, rounds+1):
                print(f"Kierros {i}")
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
