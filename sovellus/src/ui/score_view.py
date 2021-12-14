import tkinter as tk
from tkinter import constants
from services.gameservice import GameService


class ScoreView:
    """Pistetilastonäykmä. Näyttää kolme parasta pelaajaa.
    """

    def __init__(self, root, handle_show_start_view, game):
        """Luokan konstruktori.

        Args:
            root (tkInter): Käyttöliittymän juuri
            handle_show_start_view (function): Kutsuu aloitusnäkymän käynnistystä
            game (class): Pelattu peli, jossa tarvittavat tiedot pistetilastoon
        """
        self._root = root
        self._handle_show_start_view = handle_show_start_view
        self._frame = None
        self._game = game

        self._scores = self._game.get_highscores()

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        """Luo alustat pisteille ja napin pelin uudelleen pelaamiseksi.
        """
        self._frame = tk.Frame(master=self._root)

        bg_label = tk.Label(
            master=self._frame,
            background="green",
            width=120,
            height=45
        )

        scores = tk.Label(
            master=self._frame,
            text="TOP 3 PISTEET",
            foreground="black",
            background="orange",
            width=35,
            height=5
        )

        score_st = tk.Label(
            master=self._frame,
            text=self._game.get_score(self._scores),
            foreground="black",
            background="orange",
            width=35,
            height=5
        )

        score_nd = tk.Label(
            master=self._frame,
            text=self._game.get_score(self._scores),
            foreground="black",
            background="orange",
            width=35,
            height=5
        )

        score_rd = tk.Label(
            master=self._frame,
            text=self._game.get_score(self._scores),
            foreground="black",
            background="orange",
            width=35,
            height=5
        )

        button = tk.Button(
            master=self._frame,
            text="PELAA UUDELLEEN",
            width=15,
            height=5,
            background="grey",
            foreground="black",
            command=self._handle_show_start_view
        )

        bg_label.grid(row=0, column=0, columnspan=5, rowspan=6)
        scores.grid(row=1, column=2)
        score_st.grid(row=2, column=2)
        score_nd.grid(row=3, column=2)
        score_rd.grid(row=4, column=2)

        button.grid(row=5, column=2)
