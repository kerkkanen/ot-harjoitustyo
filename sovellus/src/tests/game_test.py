import unittest
from services.gameservice import GameService


class TestGame(unittest.TestCase):
    def setUp(self):
        self.normal_game = GameService("Maussi", 6, 10, "Maailma", False)
        self.sudden_death = GameService("Maussi", 2, 10, "Eurooppa", True)

    def test_question_creation_works(self):
        self.normal_game.create_question()
        self.assertNotEqual(self.normal_game._question, None)

    def test_option_creation_works(self):
        self.normal_game.create_question()
        option = self.normal_game.option()
        self.assertNotEqual(len(option), 0)

    def test_options_are_different(self):
        options = []
        self.normal_game.create_question()
        for i in range(6):
            options.append(self.normal_game.option())
        counter = 0
        for i in options:
            counter += options.count(i)
        self.assertTrue(counter == 6)

    def test_capital_check_works(self):
        self.normal_game.create_question()
        capital = self.normal_game.capital()
        self.assertTrue(self.normal_game.check_capital(capital, 3))

    def test_player_name_is_correct(self):
        self.assertEqual(self.normal_game.player_name(), "Maussi")

    def test_rounds_left_returns_false_when_no_countries_left(self):
        for i in range(47):
            self.sudden_death.create_question()
            capital = self.sudden_death.capital()
            self.sudden_death.check_capital(capital, 3)
        self.assertFalse(self.sudden_death.rounds_left())
