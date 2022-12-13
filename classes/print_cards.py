def ascii_version_of_card(*cards, return_string=True):
    """
    Instead of a boring text version of the card we render an ASCII image of the card.
    :param cards: One or more card objects
    :param return_string: By default we return the string version of the card, but the dealer hide the 1st card and we
    keep it as a list so that the dealer can add a hidden card in front of the list
    """
    # we will use this to prints the appropriate icons for each card
    suits_symbols = ['♠', '♦', '♥', '♣']
    rank_list = ["None", "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    # create an empty list of list, each sublist is a line
    lines = [[] for i in range(9)]

    for card in cards:
        # "King" should be "K" and "10" should still be "10"
        if card.rank == 10:  # ten is the only one who's rank is 2 char long
            rank = card.rank
            space = ''  # if we write "10" on the card that line will be 1 char to long
        else:
            rank = card.rank  # some have a rank of 'King' this changes that to a simple 'K' ("King" doesn't fit)
            space = ' '  # no "10", we use a blank space to will the void
        # get the cards suit in two steps
        suit = suits_symbols[card.suit]

        # add the individual card on a line by line basis
        lines[0].append('┌─────────┐')
        lines[1].append('│{}{}       │'.format(rank_list[rank], space))  # use two {} one for char, one for space or char
        lines[2].append('│         │')
        lines[3].append('│         │')
        lines[4].append('│    {}    │'.format(suit))
        lines[5].append('│         │')
        lines[6].append('│         │')
        lines[7].append('│       {}{}│'.format(space, rank_list[rank]))
        lines[8].append('└─────────┘')

    result = [''.join(line) for line in lines]

    return '\n'.join(result)