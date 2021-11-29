import tkinter as tk
from services.gameservice import GameService
from tkinter import constants

class GameView:

    def __init__(self, root, handle_show_score_view):
        self._root = root
        self._handle_show_score_view = handle_show_score_view
        #self._handle_start_game()
        self._frame = None
        
        
        self._initialize()

    def _handle_start_game(self):
        #game = Game(Player("Kisu"), 3)
        pass
    
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
            text="Maa:",
            foreground="black",
            background="orange",
            width=35,
            height=5
        )

        st_button = tk.Button(
            master=self._frame,
            text="",
            width=35,
            height=5,
            background="white",
            foreground="black",
            #command=self._handle_show_score_view
        )

        nd_button = tk.Button(
            master=self._frame,
            text="",
            width=35,
            height=5,
            background="white",
            foreground="black",
            command=self._handle_show_score_view
        )

        rd_button = tk.Button(
            master=self._frame,
            text="",
            width=35,
            height=5,
            background="white",
            foreground="black",
            #command=self._handle_show_score_view
        )

        bg_label.grid(row=0, column=2, columnspan=4, rowspan=4)
        name_label.grid(row=0, column=2, columnspan=4,
                        pady=45, sticky=constants.N)
        country_label.grid(row=0, column=2, columnspan=4,
                           pady=100, sticky=constants.S)
        st_button.grid(row=1, column=2, columnspan=4)
        nd_button.grid(row=2, column=2, columnspan=4)
        rd_button.grid(row=3, column=2, columnspan=4)
