import tkinter as tk
from tkinter import *
from tkinter import constants, messagebox

from services.gameservice import GameService


class NormalGameView:

    def __init__(self, root, handle_show_finished_view, game):
        self._root = root
        self._handle_show_finished_view = handle_show_finished_view
        self._frame = None
        self._game = game

        self._box = messagebox
        self._end_box = messagebox

        self._country = StringVar()
        self._first_option = StringVar()
        self._second_option = StringVar()
        self._third_option = StringVar()

        self._ans_one = None
        self._ans_two = None
        self._ans_three = None

        self._rounds = 3

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _run_game(self):

        self._game.create_question()

        self._ans_one = self._game.option()
        self._ans_two = self._game.option()
        self._ans_three = self._game.option()

        self._country.set(self._game.country())
        self._first_option.set(self._ans_one)
        self._second_option.set(self._ans_two)
        self._third_option.set(self._ans_three)

    def _initialize(self):

        self._run_game()

        self._frame = tk.Frame(master=self._root)

        bg_label = tk.Label(
            master=self._frame,
            background="green",
            width=120,
            height=45
        )

        name_label = tk.Label(
            master=self._frame,
            text="Valitse oikea pääkaupunki maalle:",
            foreground="black",
            background="green",
            width=35,
            height=5
        )

        country_label = tk.Label(
            master=self._frame,
            textvariable=self._country,
            foreground="black",
            background="orange",
            width=35,
            height=5
        )

        st_button = tk.Button(
            master=self._frame,
            textvariable=self._first_option,
            width=35,
            height=5,
            background="white",
            foreground="black",
            command=self._select_st_answer
        )

        nd_button = tk.Button(
            master=self._frame,
            textvariable=self._second_option,
            width=35,
            height=5,
            background="white",
            foreground="black",
            command=self._select_nd_answer
        )

        rd_button = tk.Button(
            master=self._frame,
            textvariable=self._third_option,
            width=35,
            height=5,
            background="white",
            foreground="black",
            command=self._select_rd_answer
        )

        bg_label.grid(row=0, column=2, columnspan=4, rowspan=4)
        name_label.grid(row=0, column=2, columnspan=4,
                        pady=45, sticky=constants.N)
        country_label.grid(row=0, column=2, columnspan=4,
                           pady=100, sticky=constants.S)
        st_button.grid(row=1, column=2, columnspan=4)
        nd_button.grid(row=2, column=2, columnspan=4)
        rd_button.grid(row=3, column=2, columnspan=4)

    def _select_st_answer(self):
        self._feedback_message(self._game.check_capital(self._ans_one))

    def _select_nd_answer(self):
        self._feedback_message(self._game.check_capital(self._ans_two))

    def _select_rd_answer(self):
        self._feedback_message(self._game.check_capital(self._ans_three))

    def _feedback_message(self, answer):
        if answer:
            click = self._box.askquestion("Oikein", "Hienoa!\n\nJatketaanko?")
            self._box_click(click)
        else:
            click = self._box.askquestion(
                "Väärin", f"Oikea vastaus on {self._game.capital()}\n\nJatketaanko?")
            self._box_click(click)

    def _box_click(self, clicked):
        if clicked == "no":
            self._end()
        if clicked == "yes":
            self._initialize()

    def _end(self):
        self._end_box.showinfo("Heippa!", "Peli päättyy.")
        self._handle_finished_view()

    def _handle_finished_view(self):

        self._handle_show_finished_view(self._game)
