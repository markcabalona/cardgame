from typing import Tuple
from cardgame.deck import Deck, Hand


def main():
    game = BaccaratCardGame()
    game.deal()


class BaccaratCardGame:
    deck = Deck()

    def deal(self) -> Tuple[Hand, Hand]:
        self.deck.shuffle_deck()
        player = [self.deck.draw() for _ in range(3)]
        dealer = [self.deck.draw() for _ in range(3)]

        return player, dealer


if __name__ == "__main__":
    main()
