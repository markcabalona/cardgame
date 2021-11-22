from dataclasses import dataclass, field
from enum import Enum
from typing import List, Tuple
from cardgame.deck import BaccaratDeck, Card, Hand


def main():
    baccarat_game = BaccaratCardGame()
    baccarat_game.deal()
    baccarat_game.check_bet()

    print("Player's Hand",baccarat_game.player_hand)
    print("Banker's Hand",baccarat_game.banker_hand)

    print("Player FaceCount: ", baccarat_game.player_face_count)
    print("Banker FaceCount: ", baccarat_game.banker_face_count)

    print("Player Points: ", baccarat_game.player_points)
    print("Banker Points: ", baccarat_game.banker_points)
    

    if not baccarat_game.isTie:
        print(baccarat_game.mainbet, "wins the main bet!")
    else:
        print("tie")



@dataclass
class BaccaratCardGame:
    deck = BaccaratDeck()
    player_hand: Hand = field(default_factory=lambda: [])
    banker_hand: Hand = field(default_factory=lambda: [])

    player_face_count: int = field(default_factory=lambda: 0)
    banker_face_count: int = field(default_factory=lambda: 0)

    player_points: int = field(default_factory=lambda: 0)
    banker_points: int = field(default_factory=lambda: 0)

    mainbet = str
    sidebet = str
    isTie = False

    def deal(self) -> None:
        self.deck.shuffle_deck()
        self.player_hand = [self.deck.draw() for _ in range(3)]
        self.banker_hand = [self.deck.draw() for _ in range(3)]

    def check_bet(self) -> None:

        self.count_points()
        self.count_faces()

        if self.player_face_count == self.banker_face_count:
            if self.player_points == self.banker_points:
                self.isTie = True
            else:
                self.mainbet = (
                    "player" if self.player_points > self.banker_points else "banker"
                )
            return

        self.mainbet = (
            "player" if self.player_face_count > self.banker_face_count else "banker"
        )

    def count_points(self) -> None:

        for card in self.player_hand:
            self.player_points += card.value if card.value < 10 else 0

        for card in self.banker_hand:
            self.banker_points += card.value if card.value < 10 else 0

        self.player_points = self.player_points % 10
        self.banker_points = self.banker_points % 10

    def count_faces(self) -> None:

        for card in self.player_hand:
            if card.value in range(11, 14):
                self.player_face_count += 1

        for card in self.banker_hand:
            if card.value in range(11, 14):
                self.banker_face_count += 1








if __name__ == "__main__":
    main()
