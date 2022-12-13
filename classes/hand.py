from typing import List
from classes.deck import Deck
from classes.card import Card

class Hand(Deck):
    def __init__(self, name):
        self.cards:List[Card] = []
        self.stash:List[Card] = []
        self.name = name

    def add_card(self, card:Card):
        self.cards.append(card)
    
    # Remove the top card and return it. For drawing in a round of war.
    def draw_top_card(self):
        card = self.cards.pop(0)
        return card

    def add_won_cards(self, cards:List[Card]):
        for card in cards:
            self.cards.append(card)

    def __str__(self):
        s = "Hand " + self.name
        if self.is_empty():
            return s + " is empty"
        s += " contians \n" + Deck.__str__(self)
        return s