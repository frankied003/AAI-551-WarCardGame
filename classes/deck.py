import random
from classes.card import Card

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def __str__(self):
        """
        print the contents of the deck so that each card is indented one space more than the previous card.
        """
        s = ""
        for i in range(len(self.cards)):
            s += i * " " + str(self.cards[i]) + "\n"
        return s

    def shuffle(self):
        n_cards = len(self.cards)
        for i in range(n_cards):
            j = random.randrange(0, n_cards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def pop_card(self):
        return self.cards.pop()

    def is_empty(self):
        return len(self.cards) == 0

    def deal(self, players, numOfCards = 52):
        n_players = len(players)
        if(numOfCards > len(self.cards)):
            return "Un-able to deal more cards than deck"
        for i in range(numOfCards):
            if self.is_empty():
                break
            card = self.pop_card()
            current_player = i % n_players
            players[current_player].add_card(card)