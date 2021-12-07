import tkinter as tk
from tkinter import constants
from services.gameservice import GameService


class FinishedView:

    def __init__(self, root, handle_show_score_view, handle_show_start_view, game):
        self._root = root
        self._handle_show_score_view = handle_show_score_view
        self._handle_show_start_view = handle_show_start_view
        self._frame = None
        self._game = game

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

        info_label = tk.Label(
            master=self._frame,
            text=f"Pelaajan {self._game.player_name()} pisteet:\n {self._game.player_score()}",
            foreground="black",
            background="orange",
            width=50,
            height=10
        )

        button = tk.Button(
            master=self._frame,
            text="Alkuun",
            width=15,
            height=5,
            background="grey",
            foreground="black",
            command=self._handle_show_start_view
        )

        bg_label.grid(row=0, column=0, columnspan=5, rowspan=6)
        info_label.grid(row=2, column=2)
        button.grid(row=4, column=2)
