"""Testit statistics_service-luokalle"""
import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    """Pieni testilista"""
    def get_players(self):
        """Palautetaan testilista"""
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    """Statistiikkapalvelun testaus"""
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_etsi_pelaaja(self):
        """Testataan pelaajan haku, pitäisi palauttaa pelaajan tiedot tekstimuodossa"""
        pelaaja = self.stats
        self.assertAlmostEqual(str(pelaaja.search("Gretzky")), "Gretzky EDM 35 + 89 = 124")
    
    def test_etsi_olematon_pelaaja(self):
        """Testataan pelaajan haku ilman tulosta"""
        pelaaja = self.stats
        self.assertEqual(str(pelaaja.search("Kissa")), 'None')

    def test_etsi_joukkue(self):
        """Testataan joukkueen haku, tarkistetaan listan jäsenet tekstimuodossa"""
        pelaaja = self.stats
        self.assertEqual(str(pelaaja.team("EDM")[0]), "Semenko EDM 4 + 12 = 16")
        self.assertEqual(str(pelaaja.team("EDM")[1]), "Kurri EDM 37 + 53 = 90")
        self.assertEqual(str(pelaaja.team("EDM")[2]), "Gretzky EDM 35 + 89 = 124")

    def test_etsi_parhaat(self):
        """Testataan toplistaus, tarkistetaan listan jäsenet tekstimuodossa"""
        pelaaja = self.stats
        self.assertEqual(str(pelaaja.top(3)[0]), "Gretzky EDM 35 + 89 = 124")
