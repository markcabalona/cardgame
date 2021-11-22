from typing import List, Tuple
from dataclasses import dataclass, field
from itertools import product
from random import shuffle


@dataclass
class Card:
    value: int
    suit: str


@dataclass
class DeckSpecs:
    values: List[int] = field(default_factory=lambda: list(range(1, 14)))
    suits: List[str] = field(
        default_factory=lambda: ["Hearts", "Diamonds", "Clubs", "Spades"]
    )

    # TODO: build deck, n_deck, draw, deal
    def _build_deck(self) -> List[Card]:
        return [Card(value, suit) for value, suit in product(self.values, self.suits)]

    def n_deck(self, n: int = 8):
        return [card for card in self._build_deck() for _ in range(n)]


@dataclass
class Deck:
    deck: List[Card] = field(default_factory=lambda: DeckSpecs().n_deck(8))

    def shuffle_deck(self) -> None:
        shuffle(self.deck)

    def draw(self, n: int = 8) -> Card:
        _card = self.deck[0]
        self.deck.remove(_card)
        return _card


Hand = List[Card]
