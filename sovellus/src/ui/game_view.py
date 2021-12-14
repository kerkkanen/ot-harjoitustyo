import tkinter as tk
import time
from tkinter import *
from tkinter import constants, messagebox

from services.gameservice import GameService


class GameView:
    """Luokan konstruktori, josta käynnistetään näkymän luonti.

        Args:
            root (tkInter]): Käyttöliittymän juuri
            handle_show_score_view (function): Kutsuu pistenäkymän käynnistävää funktiota
            game (class): GameService, jossa tiedot pelistä
            sudden_death (boolean): Tieto, pelataanko niin, että peli päättyy väärästä vastauksesta

        Attributes:
            frame: Näkymä, johon elementit asetetaan
            start/end_time: Vastaamisen alku- ja loppuaika
            box/endbox: Tekstilaatikot vastauspalautteelle ja pelin loppumiselle
            country: Kysytty maa-teksti"Pelaaja 1"
            ans_o/t/t: Vastausvaihtoehdot
            rounds: Pelattujen kierrosten lukumäärä
        """

    def __init__(self, root, handle_show_score_view, game, sudden_death):
        self._root = root
        self._handle_show_score_view = handle_show_score_view
        self._frame = None
        self._game = game
        self._level = self._game.level()
        self._sudden_death = sudden_death

        self._start_time = None
        self._end_time = None

        self._box = messagebox
        self._end_box = messagebox

        self._country = StringVar()
        self._first_option = StringVar()
        self._second_option = StringVar()
        self._third_option = StringVar()
        self._fourth_option = StringVar()
        self._fifth_option = StringVar()
        self._sixth_option = StringVar()

        self._ans_one = None
        self._ans_two = None
        self._ans_three = None
        self._ans_four = None
        self._ans_five = None
        self._ans_six = None

        self._rounds = 10

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _run_game(self):
        """Luo uuden kysymyksen ja tallettaa kysytyn maan ja vaihtoehdot oikeisiin muuttujiin pelin vaikeustason mukaan.
        """

        self._game.create_question()

        self._country.set(self._game.country())

        self._ans_one = self._game.option()
        self._ans_two = self._game.option()

        self._first_option.set(self._ans_one)
        self._second_option.set(self._ans_two)

        if self._level >= 3:
            self._ans_three = self._game.option()
            self._third_option.set(self._ans_three)
        if self._level == 6:
            self._ans_four = self._game.option()
            self._ans_five = self._game.option()
            self._ans_six = self._game.option()
            self._fourth_option.set(self._ans_four)
            self._fifth_option.set(self._ans_five)
            self._sixth_option.set(self._ans_six)

    def _initialize(self):
        """Alustaa näkymän: luo elementit, asettaa muuttujat niihin ja elementit paikoilleen.
        """
        self._start_time = time.time()

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

        rth_button = tk.Button(
            master=self._frame,
            textvariable=self._fourth_option,
            width=35,
            height=5,
            background="white",
            foreground="black",
            command=self._select_rth_answer
        )

        fth_button = tk.Button(
            master=self._frame,
            textvariable=self._fifth_option,
            width=35,
            height=5,
            background="white",
            foreground="black",
            command=self._select_fth_answer
        )

        xth_button = tk.Button(
            master=self._frame,
            textvariable=self._sixth_option,
            width=35,
            height=5,
            background="white",
            foreground="black",
            command=self._select_xth_answer
        )

        if self._level == 2:
            bg_label.grid(row=0, column=2, columnspan=4, rowspan=4)
            name_label.grid(row=0, column=2, columnspan=4,
                            pady=45, sticky=constants.N)
            country_label.grid(row=0, column=2, columnspan=4,
                               pady=100, sticky=constants.S)
            st_button.grid(row=1, column=2, columnspan=4)
            nd_button.grid(row=3, column=2, columnspan=4)
        elif self._level == 3:
            bg_label.grid(row=0, column=2, columnspan=4, rowspan=4)
            name_label.grid(row=0, column=2, columnspan=4,
                            pady=45, sticky=constants.N)
            country_label.grid(row=0, column=2, columnspan=4,
                               pady=100, sticky=constants.S)
            st_button.grid(row=1, column=2, columnspan=4)
            nd_button.grid(row=2, column=2, columnspan=4)
            rd_button.grid(row=3, column=2, columnspan=4)
        else:
            bg_label.grid(row=0, column=2, columnspan=6, rowspan=6)
            name_label.grid(row=0, column=3, columnspan=4,
                            pady=45, sticky=constants.N)
            country_label.grid(row=0, column=3, columnspan=4,
                               pady=100, sticky=constants.S)
            st_button.grid(row=1, column=2, columnspan=4)
            nd_button.grid(row=1, column=4, columnspan=4)
            rd_button.grid(row=2, column=2, columnspan=4)
            rth_button.grid(row=2, column=4, columnspan=4)
            fth_button.grid(row=3, column=2, columnspan=4)
            xth_button.grid(row=3, column=4, columnspan=4)

    def _select_st_answer(self):
        """Toiminta, kun pelaaja on klikannut vastausvaihtoehtoa.
            Otetaan vastausaika talteen. Kutsutaan vastauspalautelaatikkoa,
            jolle syötetään oikean vastauksen tarkistava funktio ja vastausaika.
            (select_answerit on kytketty eri nappeihin)
        """
        self._end_time = time.time()
        ans_time = self._end_time - self._start_time
        self._feedback_message(
            self._game.check_capital(self._ans_one, ans_time))

    def _select_nd_answer(self):
        self._end_time = time.time()
        ans_time = self._end_time - self._start_time
        self._feedback_message(
            self._game.check_capital(self._ans_two, ans_time))

    def _select_rd_answer(self):
        self._end_time = time.time()
        ans_time = self._end_time - self._start_time
        self._feedback_message(
            self._game.check_capital(self._ans_three, ans_time))

    def _select_rth_answer(self):
        self._end_time = time.time()
        ans_time = self._end_time - self._start_time
        self._feedback_message(
            self._game.check_capital(self._ans_four, ans_time))

    def _select_fth_answer(self):
        self._end_time = time.time()
        ans_time = self._end_time - self._start_time
        self._feedback_message(
            self._game.check_capital(self._ans_five, ans_time))

    def _select_xth_answer(self):
        self._end_time = time.time()
        ans_time = self._end_time - self._start_time
        self._feedback_message(
            self._game.check_capital(self._ans_six, ans_time))

    def _feedback_message(self, answer):
        """Avaa messageboxin, jossa palaute väärästä ja oikeasta vastauksesta.
           Pelaajalla mahdollisuus jatkaa peliä (yes)
           tai lopettaa ennen kierrosmäärän päättymistä (no):

        Args:
            answer (boolean): Tieto, onko pelaajan vastaus oikein vai väärin
        """
        if answer:
            click = self._box.askquestion("Oikein", "Hienoa!\n\nJatketaanko?")
            self._box_click(click)
        elif not self._sudden_death:
            click = self._box.askquestion(
                "Väärin", f"Oikea vastaus on {self._game.capital()}\n\nJatketaanko?")
            self._box_click(click)
        else:
            self._end()

    def _box_click(self, clicked):
        """Napinpainalluksen käsittelijä.

        Args:
            clicked (str): Jatketaanko peliä, vai lopetetaanko kesken
        """
        if clicked == "no":
            self._end()
        if clicked == "yes":
            if not self._sudden_death:
                self._rounds -= 1
                if self._rounds > 0:
                    self._next_round()
                else:
                    self._end()
            else:
                self._next_round()

    def _next_round(self):
        """Seuraavan pelikierroksen luominen.
        """
        self.destroy()
        self._initialize()
        self.pack()

    def _end(self):
        """Pelin päättäminen/päättyminen. Messagebox näyttää pelaajan pisteet.
           Kutsutaan pistetilastonäkymää.
        """
        self._game.save_score()
        self._end_box.showinfo("Peli päättyi!",
                               f"Pelaajan {self._game.player_name()} pisteet:\n              {self._game.player_score()}")
        self._handle_score_view()

    def _handle_score_view(self):
        self._handle_show_score_view(self._game)
