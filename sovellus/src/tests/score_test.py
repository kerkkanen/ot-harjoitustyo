import unittest
from services.gameservice import GameService
from repositories.player_repository import player_repository


class TestScore(unittest.TestCase):
    def setUp(self):
        player_repository.delete_all()
        self.normal_game = GameService(6, "Märssy", "Maailma", False)
        self.sudden_death = GameService(3, "Maussi", "Eurooppa", True)

    def test_normal_scores_are_saved(self):
        self.normal_game.create_question()
        capital = self.normal_game.capital()
        self.normal_game.check_capital(capital, 6)

        self.normal_game.create_question()
        capital = self.normal_game.capital()
        self.normal_game.check_capital(capital, 1.2)

        self.normal_game.create_question()
        capital = self.normal_game.capital()
        self.normal_game.check_capital(capital, 3)
        self.assertEqual(self.normal_game._player.score(), 170)

    def test_scores_add_correctly(self):
        self.normal_game._player.add_score(1, False)
        self.normal_game._player.add_score(2, False)
        self.normal_game._player.add_score(4, False)
        self.normal_game._player.add_score(5, False)
        self.assertEqual(self.normal_game._player.score(), 255)

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

    def test_normal_scorelist_not_empty_when_played_normal(self):
        self.normal_game.create_question()
        capital = self.normal_game.capital()
        self.normal_game.check_capital(capital, 3)
        self.normal_game.save_score()
        scores = self.normal_game.get_normal_highscores()
        self.assertNotEqual(self.sudden_death.get_score(scores), "TYHJÄ")

    def test_sudden_death_scorelist_appears_correctly(self):
        for i in range(4):
            self.sudden_death.create_question()
            capital = self.sudden_death.capital()
            self.sudden_death.check_capital(capital, 3)
        self.sudden_death.save_score()
        scores = self.sudden_death.get_normal_highscores()
        self.assertNotEqual(self.normal_game.get_score(scores), 3)

    def test_scores_appear_in_right_order(self):
        self.normal_game.create_question()
        capital = self.normal_game.capital()
        self.normal_game.check_capital(capital, 3)
        self.normal_game.save_score()

        other_game = GameService(2, "Sisseli", "Maailma", False)
        other_game.create_question()
        capital = other_game.capital()
        other_game.check_capital(capital, 5)
        other_game.save_score()

        scores = self.normal_game.get_normal_highscores()
        self.assertTrue(scores[0][3] >= scores[1][3])

    def test_wrong_answer_does_now_give_points(self):
        self.sudden_death.create_question()
        self.sudden_death.check_capital("Pukkila", 4)
        self.assertEqual(self.sudden_death.player_score(), 0)
