import tkinter as tk
from tkinter import constants
from services.gameservice import GameService


class ReadyView:

    def __init__(
        self, root,
        handle_show_start_view,
        handle_show_easy_game_view,
        handle_show_normal_game_view,
        handle_show_hard_game_view,
        player_name,
        game_level,
        game_area
    ):

        self._root = root
        self._handle_show_start_view = handle_show_start_view
        self._handle_show_easy_game_view = handle_show_easy_game_view
        self._handle_show_normal_game_view = handle_show_normal_game_view
        self._handle_show_hard_game_view = handle_show_hard_game_view
        self._player_name = player_name
        self._game_level = game_level
        self._game_area = game_area
        self._frame = None

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
        self._player_name_entry = None

        info_label = tk.Label(
            master=self._frame,
            text=f"Nimimerkkisi: {self._player_name}\n Pelin vaikeustaso: {self._game_level} vastausvaihtoehtoa\nPelialue: {self._game_area}",
            foreground="black",
            background="orange",
            width=50,
            height=10
        )

        return_button = tk.Button(
            master=self._frame,
            text="Alkuun",
            width=15,
            height=5,
            background="grey",
            foreground="black",
            command=self._handle_show_start_view
        )

        start_button = tk.Button(
            master=self._frame,
            text="Aloita peli",
            width=15,
            height=5,
            background="grey",
            foreground="black",
            command=self._start
        )

        bg_label.grid(row=0, column=0, columnspan=5, rowspan=6)
        info_label.grid(row=1, column=2, rowspan=2, pady=45)
        return_button.grid(row=5, column=1, columnspan=1, pady=40)
        start_button.grid(row=5, column=3, columnspan=1, pady=40)

    def _start(self):
        game = GameService(self._game_level, self._player_name, self._game_area)

        if self._game_level == 2:
            self._handle_show_easy_game_view(game)
        elif self._game_level == 3:
            self._handle_show_normal_game_view(game)
        else:
            self._handle_show_hard_game_view(game)
