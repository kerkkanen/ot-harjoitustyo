import tkinter as tk
from tkinter import constants
from services.gameservice import GameService


class ScoreView:

    def __init__(self, root, handle_show_start_view, game):

        self._root = root
        self._handle_show_start_view = handle_show_start_view
        self._frame = None
        self._game = game

        self._normal_scores = self._game.get_normal_highscores()
        self._sudden_death_scores = self._game.get_sudden_death_highscores()

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):

        self._frame = tk.Frame(master=self._root)

        bg_label = tk.Label(
            master=self._frame,
            background="green",
            width=120,
            height=45
        )

        scores = tk.Label(
            master=self._frame,
            text="TOP 3 -PISTEET",
            font=("bold", 18),
            foreground="black",
            background="orange",
            width=25,
            height=5
        )

        self._create_normal_list_items()
        self._create_sudden_death_list_items()

        button = tk.Button(
            master=self._frame,
            text="PELAA UUDELLEEN",
            width=15,
            height=5,
            background="grey",
            foreground="black",
            command=self._handle_show_start_view
        )

        bg_label.grid(row=0, column=0, columnspan=6, rowspan=6)
        scores.grid(row=0, column=2, columnspan=2, pady=20)
        button.grid(row=5, column=2, columnspan=2, pady=30)

    def _create_normal_list_items(self):

        normal = tk.Label(
            master=self._frame,
            text='"Turvallisesti loppuun"',
            font=(16),
            foreground="white",
            background="green",
            width=25,
            height=5
        )

        score_st = tk.Label(
            master=self._frame,
            text=self._game.get_score(self._normal_scores),
            font=(14),
            foreground="black",
            background="orange",
            width=25,
            height=5
        )

        score_nd = tk.Label(
            master=self._frame,
            text=self._game.get_score(self._normal_scores),
            font=(14),
            foreground="black",
            background="orange",
            width=25,
            height=5
        )

        score_rd = tk.Label(
            master=self._frame,
            text=self._game.get_score(self._normal_scores),
            font=(14),
            foreground="black",
            background="orange",
            width=25,
            height=5
        )

        normal.grid(row=1, column=2)
        score_st.grid(row=2, column=2, pady=3)
        score_nd.grid(row=3, column=2, pady=3)
        score_rd.grid(row=4, column=2, pady=3)

    def _create_sudden_death_list_items(self):

        sudden_death = tk.Label(
            master=self._frame,
            text='"Kerrasta poikki"',
            font=(16),
            foreground="white",
            background="green",
            width=25,
            height=5
        )

        score_st = tk.Label(
            master=self._frame,
            text=self._game.get_score(self._sudden_death_scores),
            font=(14),
            foreground="black",
            background="orange",
            width=25,
            height=5
        )

        score_nd = tk.Label(
            master=self._frame,
            text=self._game.get_score(self._sudden_death_scores),
            font=(14),
            foreground="black",
            background="orange",
            width=25,
            height=5
        )

        score_rd = tk.Label(
            master=self._frame,
            text=self._game.get_score(self._sudden_death_scores),
            font=(14),
            foreground="black",
            background="orange",
            width=25,
            height=5
        )
        sudden_death.grid(row=1, column=3)
        score_st.grid(row=2, column=3)
        score_nd.grid(row=3, column=3)
        score_rd.grid(row=4, column=3)
