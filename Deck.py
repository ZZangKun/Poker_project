
#The Deck class generates poker cards from 2 to ace of 4 suits
#the shuffle method shuffles the deck of card into random order
#the deal method deals the top card to a player when the method is called
#using a suit tuple, it is easier to give parameter to the Card class in order to generate cards because it is a irritation of 4 different suits with 13 cards
#the pop() method of the list of card removes the dealed card, so it won't repeat
#using append() to add card to the list of card

import Card
import random

class Deck:
    suit = ("clubs", "diamonds", "spades", "hearts")

    def __init__(self):
        self.deck = []
        self.cnt = 0
        for x in Deck.suit:
            for i in range(2, 15):
                self.deck.append(Card.Card(x, i))
                self.cnt += 1

    def get_deck(self):
        return self.deck

    def print_deck(self):
        [print(x) for x in self.deck]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        top_card = self.deck[len(self.deck)-1]
        self.deck.pop()
        return top_card

