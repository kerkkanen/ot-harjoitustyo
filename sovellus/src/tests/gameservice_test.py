import unittest
from services.gameservice import GameService


class TestGame(unittest.TestCase):
    def setUp(self):
        self.service = GameService("Kisu", 5)
