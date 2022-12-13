from typing import List
from classes.deck import Deck
from classes.hand import Hand

class War:
   def __init__(self, player1:str, player2:str):
      self.deck = Deck()
      self.deck.shuffle()
      self.players = [Hand(player1), Hand(player2)]

   def remove_player(self, player:Hand):
      self.players.remove(player)

   # Want to deal all the cards in war.
   def deal_war(self):
      self.deck.deal(self.players, len(self.deck.cards))

   # Find the winning hand for a 1 to 1 card ratio.
   def find_winning_hand(self, stash1, stash2):
   
      # Checking what card is higher or if it's a tie.
      if stash1[-1].__gt__(stash2[-1]):
         print(self.players[0].name, "won!")
         return self.players[0]
      elif stash2[-1].__gt__(stash1[-1]):
         print(self.players[1].name, "won!")
         return self.players[1]
      elif stash2[-1].__eq__(stash1[-1]):
         print("It's a tie")

         # Try catch here because of out of bounds / indexing error.
         try:
            for i in range(3):
               new_card = self.players[0].draw_top_card()
               self.players[0].stash.append(new_card)
            for i in range(3):
               new_card = self.players[1].draw_top_card()
               self.players[1].stash.append(new_card)
            return self.find_winning_hand(self.players[0].stash, self.players[1].stash)
         except IndexError:
            # Means the losing player doesn't have three cards so winner goes to person with higher # of cards
            if len(self.players[0].cards) > len(self.players[1].cards):
               return self.players[0]
            else:
               return self.players[1]

   # Playing one round.
   def play_round(self):
          
      # Check whether there are any other cards to play from either players first.
      for player in self.players:
         if player.is_empty():
            self.remove_player(player)
            return

      # Loop through each players hand and draw a card and append it their stash.
      for player in self.players:
         drawn_card = player.draw_top_card()
         print(drawn_card, "was drawn by", player.name, "who has", len(player.cards), "left")
         player.stash.append(drawn_card)

      # Call winning hand, which will calculate who get's the card or if they should draw 3 from a tie.
      winning_hand = self.find_winning_hand(self.players[0].stash, self.players[1].stash)
         
      # Add all cards to the bottom of the winners pile, and reset the stash.
      cards_won = self.players[0].stash + self.players[1].stash
      winning_hand.add_won_cards(cards_won)
      self.players[0].stash = []
      self.players[1].stash = []

   # Playing an entire game until someone wins.
   def play_war(self):
      while(len(self.players) > 1):
         self.play_round()
      
      print("The winner is", self.players[0].name)


