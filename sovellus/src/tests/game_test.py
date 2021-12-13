import unittest
from services.gameservice import GameService


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = GameService(6, "Kisu")

    def test_question_creation_works(self):
        self.game.create_question()
        self.assertNotEqual(self.game._question, None)

    def test_option_creation_works(self):
        self.game.create_question()
        option = self.game.option()
        self.assertNotEqual(len(option), 0)

    def test_options_are_different(self):
        self.game.create_question()
        self.assertNotEqual(self.game.option(), self.game.option())
        self.assertNotEqual(self.game.option(), self.game.option())
        self.assertNotEqual(self.game.option(), self.game.option())

    def test_capital_check_works(self):
        self.game.create_question()
        capital = self.game.capital()
        self.assertTrue(self.game.check_capital(capital, 3))

    def test_player_name_is_correct(self):
        self.assertEqual(self.game.player_name(), "Kisu")
