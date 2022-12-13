class Card:
    suit_list = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_list = ["None", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit = 0, rank = 2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """
        Prints card as type string.
        """
        return (self.rank_list[self.rank] + " of " + self.suit_list[self.suit])

    # Need to use string literals to delay evaluation of the type
    def __eq__(self, __o: 'Card'):
        """
        Checks whether the cards are equal.
        __o is of type "Card".
        """
        return (self.rank == __o.rank)

    def __gt__ (self, __o: 'Card'):
        """
        Check whether card being compared to another Card class is Greater Than (gt).
        __o is of type "Card".
        """
        if self.rank > __o.rank:
            return True
        return False