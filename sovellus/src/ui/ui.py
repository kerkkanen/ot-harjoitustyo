from ui.score_view import ScoreView
from ui.start_view import StartView
from ui.ready_view import ReadyView
from ui.easy_game_view import EasyGameView
from ui.normal_game_view import NormalGameView
from ui.hard_game_view import HardGameView
from ui.check_answer_view import CheckAnswerView
from ui.finished_view import FinishedView
from services.gameservice import GameService


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

    # show_views

    def _show_start_view(self):
        self._hide_current_view()

        self._current_view = StartView(
            self._root,
            self._show_ready_view
        )
        self._current_view.pack()

    def _show_ready_view(self, player_name, game_level):
        self._hide_current_view()

        self._current_view = ReadyView(
            self._root,
            self._show_start_view,
            self._show_easy_game_view,
            self._show_normal_game_view,
            self._show_hard_game_view,
            player_name,
            game_level
        )
        self._current_view.pack()

    def _show_easy_game_view(self, game):
        self._hide_current_view()

        self._current_view = EasyGameView(
            self._root,
            self._show_check_answer_view,
            self._show_easy_game_view,
            game
        )

        self._current_view.pack()

    def _show_normal_game_view(self, game):
        self._hide_current_view()

        self._current_view = NormalGameView(
            self._root,
            self._show_check_answer_view,
            self._show_normal_game_view,
            game
        )

        self._current_view.pack()

    def _show_hard_game_view(self, game):
        self._hide_current_view()

        self._current_view = HardGameView(
            self._root,
            self._show_check_answer_view,
            self._show_hard_game_view,
            game
        )

        self._current_view.pack()

    def _show_check_answer_view(self, return_view, answer):
        self._hide_current_view()

        self._current_view = CheckAnswerView(
            self._root,
            self._show_finished_view,
            return_view,
            answer
        )

        self._current_view.pack()

    def _show_finished_view(self):
        self._hide_current_view()

        self._current_view = FinishedView(
            self._root,
            self._show_finished_view,
            self._show_score_view,
            self._show_start_view
        )

        self._current_view.pack()

    def _show_score_view(self):
        self._hide_current_view()

        self._current_view = ScoreView(
            self._root,
            self._show_start_view
        )
        self._current_view.pack()

    # väliaikainen tekstikäyttöliittymä

    def txt_ui(self):
        while True:
            answer = input("Pelaa (1) tai lopeta (2)")
            if answer == "2":
                break
            while True:
                name = input(
                    "Syötä nimimerkki (nimimerkki ei voi olla tyhjä):\n")
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
                diff = input(
                    "Valitse vaikeustaso: helppo(h), keskitaso(k), vaikea(v)\n")
                if diff == "h":
                    level = 2
                    break
                if diff == "k":
                    level = 3
                    break
                if diff == "v":
                    level = 5
                    break

            game_service = GameService(level, name)
            print(
                f"Pelataan {rounds} kierrosta. Oikeasta vastauksesta saat 50 pistettä, väärästä 0.")
            print()
            for i in range(1, rounds+1):
                print(f"Kierros {i}")
                game_service.create_question()
                print("??????????????????????????????????????????????????")
                print(f"Mikä on maan {game_service.country()} pääkaupunki  ")
                print("??????????????????????????????????????????????????")
                print()
                j = 0
                while j < level:
                    print(game_service.option())
                    j += 1
                print()
                vastaus = input("Vastaus ")
                print()
                if game_service.check_capital(vastaus):
                    print("***************")
                    print("**  Oikein!  **")
                    print("***************")
                    print()
                else:
                    print("---------------------------------------------")
                    print(f"Väärin! Oikea vastaus on {game_service.capital()}")
                    print("---------------------------------------------")
                    print()

            print(
                f"Pelaajan {game_service.player_name()} pisteet: ***{game_service.player_score()}***")