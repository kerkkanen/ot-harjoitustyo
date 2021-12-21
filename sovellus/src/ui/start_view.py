import tkinter as tk
from tkinter import ttk
from tkinter import constants
from tkinter import *
from services.gameservice import GameService


class StartView:
    def __init__(self, root, handle_show_ready_view, handle_show_score_view):
        self._root = root
        self._handle_show_ready_view = handle_show_ready_view
        self._handle_show_score_view = handle_show_score_view
        self._frame = None
        self._level_var = 3
        self._area_var = "Maailma"
        self._player_name_entry = None
        self._player_name = "Maailmanmatkaaja"
        self._level = 3
        self._area = "Maailma"

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = tk.Frame(master=self._root)
        self._level_var = IntVar()
        self._area_var = StringVar()

        bg_label = tk.Label(
            master=self._frame,
            background="green",
            width=120,
            height=45
        )

        name_label = tk.Label(
            master=self._frame,
            text="Syötä nimimerkki:",
            font=(18),
            foreground="black",
            background="orange",
            width=20,
            height=3
        )

        self._player_name_entry = tk.Entry(
            master=self._frame,
            foreground="black",
            background="white",
            width=30
        )

        level_label = tk.Label(
            master=self._frame,
            text="Vaikeustaso:",
            font=(18),
            foreground="black",
            background="orange",
            width=25,
            height=5
        )

        area_label = tk.Label(
            master=self._frame,
            text="Pelialue:",
            font=(18),
            foreground="black",
            background="orange",
            width=25,
            height=5
        )

        self._create_difficulty_buttons()
        self._create_area_buttons()
        self._create_choosing_buttons()

        bg_label.grid(row=0, column=0, columnspan=6, rowspan=9)
        name_label.grid(row=1, column=1, pady=45, sticky=constants.E)
        self._player_name_entry.grid(row=1, column=3, columnspan=2)
        level_label.grid(row=3, column=1, pady=45, sticky=constants.S)
        area_label.grid(row=3, column=4, columnspan=2,
                        pady=45, sticky=constants.S)

    def _create_difficulty_buttons(self):
        option_easy = tk.Radiobutton(
            master=self._frame,
            text="Helppo",
            variable=self._level_var,
            value=2,
            width=10,
            height=3,
            background="#000fff000",
            foreground="black",
            command=self._select_level
        )

        option_normal = tk.Radiobutton(
            master=self._frame,
            text="Keskitaso",
            variable=self._level_var,
            value=3,
            width=10,
            height=3,
            background="#000fff000",
            foreground="black",
            command=self._select_level
        )

        option_hard = tk.Radiobutton(
            master=self._frame,
            text="Vaikea",
            variable=self._level_var,
            value=6,
            width=10,
            height=3,
            background="#000fff000",
            foreground="black",
            command=self._select_level
        )

        option_easy.grid(row=4, column=1,  sticky=constants.N)
        option_normal.grid(row=4, column=1,  pady=55)
        option_hard.grid(row=4, column=1,  sticky=constants.S)

    def _create_area_buttons(self):
        asia = tk.Radiobutton(
            master=self._frame,
            text="Aasia",
            variable=self._area_var,
            value="Aasia",
            width=25,
            height=3,
            background="#000fff000",
            foreground="black",
            command=self._select_area
        )

        africa = tk.Radiobutton(
            master=self._frame,
            text="Afrikka",
            variable=self._area_var,
            value="Afrikka",
            width=25,
            height=3,
            background="#000fff000",
            foreground="black",
            command=self._select_area
        )

        america = tk.Radiobutton(
            master=self._frame,
            text="Etelä- ja Pohjois-Amerikka",
            variable=self._area_var,
            value="Amerikka",
            width=25,
            height=3,
            background="#000fff000",
            foreground="black",
            command=self._select_area
        )

        europe = tk.Radiobutton(
            master=self._frame,
            text="Eurooppa",
            variable=self._area_var,
            value="Eurooppa",
            width=25,
            height=3,
            background="#000fff000",
            foreground="black",
            command=self._select_area
        )

        oseania = tk.Radiobutton(
            master=self._frame,
            text="Oseania",
            variable=self._area_var,
            value="Oseania",
            width=25,
            height=3,
            background="#000fff000",
            foreground="black",
            command=self._select_area
        )

        all = tk.Radiobutton(
            master=self._frame,
            text="Koko maailma",
            variable=self._area_var,
            value="Maailma",
            width=25,
            height=3,
            background="#000fff000",
            foreground="black",
            command=self._select_area
        )

        asia.grid(row=4, column=4, sticky=constants.N)
        africa.grid(row=4, column=4, pady=55)
        america.grid(row=4, column=4, sticky=constants.S)
        europe.grid(row=4, column=5, sticky=constants.N)
        oseania.grid(row=4, column=5, pady=55)
        all.grid(row=4, column=5, sticky=constants.S)

    def _create_choosing_buttons(self):

        scores_button = tk.Button(
            master=self._frame,
            text="TOP-PISTEET",
            width=15,
            height=5,
            background="grey",
            foreground="black",
            command=self._show_scores
        )

        ready_button = tk.Button(
            master=self._frame,
            text="VALMISTA",
            width=15,
            height=5,
            background="grey",
            foreground="black",
            command=self._confirm
        )

        scores_button.grid(row=5, column=1, pady=40, sticky=constants.S)
        ready_button.grid(row=5, column=5, pady=40, sticky=constants.SW)

    def _select_level(self):
        self._level = int(self._level_var.get())

    def _select_area(self):
        self._area = str(self._area_var.get())

    def _confirm(self):
        if self._player_name_entry.get() != "" and len(self._player_name_entry.get()) < 20:
            self._player_name = self._player_name_entry.get()
        self._handle_show_ready_view(
            self._player_name, self._level, self._area)

    def _show_scores(self):
        self._handle_show_score_view(
            GameService(3, self._player_name, self._area, False))
