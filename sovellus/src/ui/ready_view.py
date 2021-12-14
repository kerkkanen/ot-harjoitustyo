import tkinter as tk
from tkinter import constants
from services.gameservice import GameService


class ReadyView:

    def __init__(
        self, root,
        handle_show_start_view,
        handle_show_game_view,
        player_name,
        game_level,
        game_area
    ):

        self._root = root
        self._handle_show_start_view = handle_show_start_view
        self._handle_show_game_view = handle_show_game_view
        self._player_name = player_name
        self._game_level = game_level
        self._game_area = game_area
        self._sudden_death = False
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
            text=f"Nimimerkkisi:\n{self._player_name}\n\nPelin vaikeustaso:\n{self._game_level} vastausvaihtoehtoa\n\nPelialue:\n{self._game_area}",
            foreground="black",
            background="orange",
            width=50,
            height=10
        )

        return_button = tk.Button(
            master=self._frame,
            text="ALKUUN",
            width=15,
            height=5,
            background="grey",
            foreground="black",
            command=self._handle_show_start_view
        )

        start_rounds_button = tk.Button(
            master=self._frame,
            text='"Turvallisesti loppuun"\n\n Peli kestää\n10 kierrosta\n\n\nALOITA',
            width=20,
            height=10,
            background="grey",
            foreground="black",
            command=self._start
        )

        start_sudden_death_button = tk.Button(
            master=self._frame,
            text='"Kerrasta poikki"\n\nPeli päättyy\nväärästä vastauksesta\n\n\nALOITA',
            width=20,
            height=10,
            background="grey",
            foreground="black",
            command=self._death
        )

        bg_label.grid(row=0, column=0, columnspan=8, rowspan=6)
        info_label.grid(row=1, column=2, rowspan=1, columnspan=2, pady=45)
        start_sudden_death_button.grid(row=4, column=1, columnspan=1, pady=40)
        start_rounds_button.grid(row=4, column=4, columnspan=1, pady=40)
        return_button.grid(row=5, column=2, columnspan=2, pady=40)

    def _death(self):
        self._sudden_death = True
        self._start()

    def _start(self):
        game = GameService(
            self._game_level, self._player_name, self._game_area)
        self._handle_show_game_view(game, self._sudden_death)
