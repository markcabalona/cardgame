import unittest
import sys

sys.path.append("/home/schmosby/python_dev/cardgame")

from cardgame.deck import BaccaratDeck


class TestDeck(unittest.TestCase):
    deck = BaccaratDeck()

    def test_draw(self):
        deck_count = len(self.deck.deck)
        card = self.deck.draw()
        self.assertEqual(len(self.deck.deck), deck_count - 1)
        self.assertEqual(self.deck.deck.count(card), 7)


if __name__ == "__main__":
    unittest.main()
