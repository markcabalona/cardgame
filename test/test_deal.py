import unittest
import sys
sys.path.append('/home/schmosby/python_dev/cardgame')


from bacarrat import BaccaratCardGame


class TestBaccaratCardGame(unittest.TestCase):
    game = BaccaratCardGame()

    def test_deal(self):
        deck_count = len(self.game.deck.deck)
        self.game.deal()
        self.assertEqual(len(self.game.deck.deck), deck_count-6)
    

if __name__ == "__main__":
    unittest.main()
        
