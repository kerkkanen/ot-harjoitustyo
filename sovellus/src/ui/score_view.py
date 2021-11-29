import tkinter as tk
from tkinter import constants
from services.gameservice import GameService


class ScoreView:

    def __init__(self, root, handle_show_start_view):
        self._root = root
        self._handle_show_start_view = handle_show_start_view
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = tk.Frame(master=self._root)

        label = tk.Label(
            master=self._frame,
            text="Highscore",
            foreground="green",
            background="red",
            width=120,
            height=40
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

        label.grid(row=5, column=0)
        button.grid(row=5, column=0)
