import unittest
from unittest.mock import patch

from items import Potato
from main import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player(100, ["Potato", "Tomato"], ["Cow"])

    def test_buy_with_sufficient_funds(self):
        initial_money = self.player._money
        self.player.buy(Potato())
        self.assertEqual(len(self.player.inventory), 3)
        self.assertEqual(self.player._money, initial_money - Potato().cost)

    def test_buy_with_insufficient_funds(self):
        self.player._money = 0
        initial_inventory_length = len(self.player.inventory)
        self.player.buy(Potato())
        self.assertEqual(len(self.player.inventory), initial_inventory_length)

    def test_harvest_crops(self):
        self.player.harvest_crops()
        for plant in self.player.inventory:
            print("Plant:", plant)
        self.assertEqual(len(self.player.inventory), 0)

    def test_save_progress(self):
        with patch("builtins.open", create=True) as mocked_open:
            self.player.save_progress()
            mocked_open.assert_called_once_with("progress.txt", "w")
    

if __name__ == "__main__":
    unittest.main()