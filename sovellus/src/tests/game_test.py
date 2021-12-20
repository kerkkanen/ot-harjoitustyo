import unittest
from services.gameservice import GameService


class TestGame(unittest.TestCase):
    def setUp(self):
        self.normal_game = GameService(6, "Maussi", "Maailma", False)

    def test_question_creation_works(self):
        self.normal_game.create_question()
        self.assertNotEqual(self.normal_game._question, None)

    def test_option_creation_works(self):
        self.normal_game.create_question()
        option = self.normal_game.option()
        self.assertNotEqual(len(option), 0)

    def test_options_are_different(self):
        self.normal_game.create_question()
        self.assertNotEqual(self.normal_game.option(),
                            self.normal_game.option())
        self.assertNotEqual(self.normal_game.option(),
                            self.normal_game.option())
        self.assertNotEqual(self.normal_game.option(),
                            self.normal_game.option())

    def test_capital_check_works(self):
        self.normal_game.create_question()
        capital = self.normal_game.capital()
        self.assertTrue(self.normal_game.check_capital(capital, 3))

    def test_player_name_is_correct(self):
        self.assertEqual(self.normal_game.player_name(), "Maussi")
