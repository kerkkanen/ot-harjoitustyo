import tkinter as tk
from tkinter import PhotoImage, constants
from services.gameservice import GameService


class StartView:
    def __init__(self, root, handle_show_create_game_view):
        self._root = root
        self._handle_show_create_game_view = handle_show_create_game_view
        self._frame = None
        self._player_name_entry = None
        self._level = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _game_handler(self):
        name = self._player_name_entry.get()
        player = Player(name)
        game = Game(player, 3)

    def _initialize(self):
        self._frame = tk.Frame(master=self._root)

        bg_label = tk.Label(
            master=self._frame,
            background="green",
            width=120,
            height=45
        )

        name_label = tk.Label(
            master=self._frame,
            text="Syötä nimimerkki",
            foreground="black",
            background="green",
            width=20,
            height=5
        )

        self._player_name_entry = tk.Entry(
            master=self._frame,
            foreground="black",
            background="white",
            width=30
        )

        option_easy = tk.Radiobutton(
            master=self._frame,
            text="Helppo",
            width=10,
            height=5,
            background="orange",
            foreground="black",
        )

        option_normal = tk.Radiobutton(
            master=self._frame,
            text="Keskitaso",
            width=10,
            height=5,
            background="orange",
            foreground="black",
        )

        option_hard = tk.Radiobutton(
            master=self._frame,
            text="Vaikea",
            width=10,
            height=5,
            background="orange",
            foreground="black",
        )

        button = tk.Button(
            master=self._frame,
            text="Aloita",
            width=15,
            height=5,
            background="white",
            foreground="black",
            command=self._handle_show_create_game_view
        )

        bg_label.grid(row=0, column=0, columnspan=5, rowspan=5)
        name_label.grid(row=1, column=1, columnspan=5, pady=45)
        self._player_name_entry .grid(row=2, column=2)
        option_easy.grid(row=3, column=1, columnspan=1, padx=80,  pady=60)
        option_normal.grid(row=3, column=2, columnspan=1, padx=30, pady=60)
        option_hard.grid(row=3, column=3, columnspan=1,  padx=80, pady=60)
        button.grid(row=4, column=2, columnspan=1, sticky=constants.N, pady=40)
