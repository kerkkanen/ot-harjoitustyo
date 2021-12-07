import tkinter as tk
from tkinter import constants
from services.gameservice import GameService


class CheckAnswerView:

    def __init__(
        self,
        root,
        handle_show_finished_view,
        handle_return_to_game,
        answer
    ):

        self._root = root
        self._handle_return_to_game = handle_return_to_game
        self._handle_show_finished_view = handle_show_finished_view
        self._answer = answer
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

        answer_label = tk.Label(
            master=self._frame,
            text=self._answer,
            foreground="black",
            background="orange",
            width=35,
            height=5
        )

        button = tk.Button(
            master=self._frame,
            text="Alkuun",
            width=15,
            height=5,
            background="grey",
            foreground="black",
            # command=self._handle_show_start_view
        )

        bg_label.grid(row=0, column=0)
        answer_label.grid(row=2, column=0)
        button.grid(row=5, column=0)
