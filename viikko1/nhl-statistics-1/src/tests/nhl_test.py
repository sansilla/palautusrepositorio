import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_player(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")

    def test_team(self):
        team_players = self.stats.team("DET")
        #self.assertEqual(len(team_players), 1)
        self.assertEqual(team_players[0].team, "DET") #"Yzerman")
