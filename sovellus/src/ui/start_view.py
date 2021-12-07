import tkinter as tk
from tkinter import constants
from tkinter import *
from services.gameservice import GameService


class StartView:
    def __init__(self, root, handle_show_ready_view):
        self._root = root
        self._handle_show_ready_view = handle_show_ready_view
        self._frame = None
        self._var = 3
        self._player_name_entry = None
        self._player_name = "Pelaaja 1"
        self._level = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = tk.Frame(master=self._root)
        self._var = IntVar()

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
            background="orange",
            width=20,
            height=5
        )

        self._player_name_entry = tk.Entry(
            master=self._frame,
            foreground="black",
            background="white",
            width=30
        )

        instr_label = tk.Label(
            master=self._frame,
            text="Valitse vastausvaihtoehtojen määrä:",
            foreground="black",
            background="orange",
            width=50,
            height=5
        )

        option_easy = tk.Radiobutton(
            master=self._frame,
            text="2",
            variable=self._var,
            value=2,
            width=20,
            height=5,
            background="#000fff000",
            foreground="black",
            command=self._select
        )

        option_normal = tk.Radiobutton(
            master=self._frame,
            text="3",
            variable=self._var,
            value=3,
            width=20,
            height=5,
            background="#000fff000",
            foreground="black",
            command=self._select
        )

        option_hard = tk.Radiobutton(
            master=self._frame,
            text="6",
            variable=self._var,
            value=6,
            width=20,
            height=5,
            background="#000fff000",
            foreground="black",
            command=self._select
        )

        button = tk.Button(
            master=self._frame,
            text="Valmista",
            width=15,
            height=5,
            background="grey",
            foreground="black",
            command=self._confirm
        )

        bg_label.grid(row=0, column=0, columnspan=5, rowspan=6)
        name_label.grid(row=1, column=2, rowspan=2, pady=45)
        self._player_name_entry .grid(row=2, column=2, sticky=constants.S)
        instr_label.grid(row=3, column=2, sticky=constants.S)
        option_easy.grid(row=4, column=1, sticky=constants.E, pady=60)
        option_normal.grid(row=4, column=2, pady=60)
        option_hard.grid(row=4, column=3, sticky=constants.W, pady=60)
        button.grid(row=5, column=2, columnspan=1, pady=40)

    def _select(self):
        self._level = int(self._var.get())

    def _confirm(self):
        if self._player_name_entry.get() != "":
            self._player_name = self._player_name_entry.get()
        self._handle_show_ready_view(self._player_name, self._level)
