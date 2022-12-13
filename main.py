from classes.war import War

"""
1. The goal is to be the first player to win all 52 cards
2. The deck is divided evenly, with each player receiving 26 cards, dealt one at a time, face down. 
   Anyone may deal first. Each player places their stack of cards face down, in front of them.
3. Each player turns up a card at the same time and the player with the higher card, including rank, takes both cards and puts them, face down, on the bottom of their stack.
4. If there is a tie, both players take 3 cards off of the top of their deck and use the 3rd card to play again. Winner get's all 6 cards.
4. Winner is person with all 52 cards
"""

game_of_war = War("Frankie", "Bobby")
game_of_war.deck.shuffle()
game_of_war.deal_war()
game_of_war.play_war()