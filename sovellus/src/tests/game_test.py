import unittest
from entities.game import Game
from entities.player import Player


class TestGame(unittest.TestCase):
    def setUp(self):
        player = Player("Kisuli")
        self.game = Game(player, 5)

    def test_capital_is_set_correctly(self):
        self.game.country = "Suomi"
        self.assertEqual(self.game.capital, "Helsinki")

    def test_right_number_of_options(self):
        self.game.create_question()
        number = len(self.game.other_capitals())
        self.assertEqual(number, 5)

    def test_country_is_selected(self):
        self.game.country = "Suomi"
        self.game.create_question()
        self.assertNotEqual(self.game.country, "Suomi")

    def test_right_answer_is_returned(self):
        self.game.country = "Suomi"
        self.game.capital = "Helsinki"
        self.assertTrue(self.game.check_capital("Helsinki"))
