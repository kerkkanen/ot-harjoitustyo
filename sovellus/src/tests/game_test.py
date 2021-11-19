import unittest
from game import Game
from player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        player = Player("Kisuli")
        self.game = Game(player, 5)

    def test_capital_is_correct(self):
        self.game.country = "Suomi"
        self.assertEqual(self.game.capital, "Helsinki")