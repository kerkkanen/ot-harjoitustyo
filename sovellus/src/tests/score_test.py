import unittest
from services.gameservice import GameService


class TestScore(unittest.TestCase):
    def setUp(self):
        self.normal_game = GameService(6, "Maussi", "Maailma", False)
        self.sudden_death = GameService(3, "Sisseli", "Eurooppa", True)

    def test_normal_scores_are_saved(self):
        self.normal_game.create_question()
        capital = self.normal_game.capital()
        self.normal_game.check_capital(capital, 8)

        self.normal_game.create_question()
        capital = self.normal_game.capital()
        self.normal_game.check_capital(capital, 0.5)

        self.normal_game.create_question()
        capital = self.normal_game.capital()
        self.normal_game.check_capital(capital, 10)
        self.assertEqual(self.normal_game._player.score(), 130)

    def test_sudden_death_scores_are_saved(self):
        self.sudden_death.create_question()
        capital = self.sudden_death.capital()
        self.sudden_death.check_capital(capital, 8)
        self.assertEqual(self.sudden_death._player.score(), 1)

    def test_normal_score_list_is_created(self):
        self.assertNotEqual(self.normal_game.get_normal_highscores(), [])

    def test_sudden_death_score_list_is_created(self):
        self.assertNotEqual(
            self.sudden_death.get_sudden_death_highscores(), [])

    def test_scorelist_not_empty_when_played_normal(self):
        self.normal_game.create_question()
        capital = self.normal_game.capital()
        self.normal_game.check_capital(capital, 3)
        self.normal_game.save_score()
        scores = self.normal_game.get_normal_highscores()
        self.assertNotEqual(self.normal_game.get_score(scores), "TYHJÄ")

    def test_scores_appear_in_right_order(self):
        self.normal_game.create_question()
        capital = self.normal_game.capital()
        self.normal_game.check_capital(capital, 3)
        self.normal_game.save_score()

        other_game = GameService(2, "Sissu", "Maailma", False)
        other_game.create_question()
        capital = other_game.capital()
        other_game.check_capital(capital, 5)
        other_game.save_score()

        scores = self.normal_game.get_normal_highscores()
        self.assertTrue(scores[0][3] >= scores[1][3])
