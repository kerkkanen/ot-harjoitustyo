import unittest
from services.gameservice import GameService


class TestScore(unittest.TestCase):
    def setUp(self):
        self.game = GameService(6, "Kisu", "Maailma")

    def test_scores_are_saved(self):
        self.game.create_question()
        capital = self.game.capital()
        self.game.check_capital(capital, 8)
        self.assertEqual(self.game._player.score(), 20)

    def test_score_list_is_created(self):
        self.assertNotEqual(self.game.get_highscores(), [])

    def test_scorelist_not_empty_when_played(self):
        self.game.create_question()
        capital = self.game.capital()
        self.game.check_capital(capital, 3)
        self.game.save_score()
        scores = self.game.get_highscores()
        self.assertNotEqual(self.game.get_score(scores), "TYHJÄ")

    def test_scores_appear_in_right_order(self):
        self.game.create_question()
        capital = self.game.capital()
        self.game.check_capital(capital, 3)
        self.game.save_score()

        other_game = GameService(2, "Sissu", "Maailma")
        other_game.create_question()
        capital = other_game.capital()
        other_game.check_capital(capital, 5)
        other_game.save_score()

        scores = self.game.get_highscores()
        self.assertTrue(scores[0][3] >= scores[1][3])
