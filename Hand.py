
#The Hand class generates a hand of 5 cards for a player, where the cards are sorted in descending order
#the rank method takes many small decomposed methods to determine the rank of the 5 poker cards in the hand according to the poker rules
#Compare methods considers different situations and compares who wins if two hands of cards are compared
#Using sort() method, the hand sorts the card in descending order


import Deck
import Card

def sort_value(n):
    return n.value

class Hand:

    def __init__(self):
        self.hand = []
        self.rank_level = -1
        self.high_value = -1
        self.high_straight_value = -1
        self.high_pair_value = [-1, -1, -1] #the first two index indicate the value of two pairs, the last index indicates the highest of single value

    def get_hand(self):
        return self.hand

    def print_hand(self):
        [print(x) for x in self.hand]

    def add_card(self, add: Card):
        self.hand.append(add)
        self.hand.sort(key=sort_value, reverse=True)

    def is_flush(self):
        for i in range(len(self.hand)):
            if not self.hand[i].suit == self.hand[1].suit:
                return False
        return True

    def is_straight(self):
        straight = True
        for i in range(len(self.hand)):
            if not self.hand[1].value-self.hand[1].value == i:
                straight = False
        if straight:
            if self.hand[0].value == 14 and self.hand[1].value == 5:
                self.high_straight_value = 5
            else:
                self.high_straight_value = self.hand[0].value
        return straight

    def is_three_pair(self):
        for i in range(len(self.hand)-2):
            if self.hand[i].value == self.hand[i+2].value:
                self.high_value = self.hand[i].value
                return True
        return False

    def num_pair(self):
        cnt = 0
        for i in range(len(self.hand)-1):
            if self.hand[i].value == self.hand[i+1].value:
                self.high_pair_value[cnt] = self.hand[i].value
                cnt += 1
        for i in range(len(self.hand)-1):
            if not self.hand[i].value == self.high_pair_value[0] and not self.hand[i].value == self.high_pair_value[1]:
                self.high_pair_value[2] = self.hand[i].value

        return cnt

    def is_four_of_kind(self):
        for i in range(len(self.hand)-3):
            if self.hand[i].value == self.hand[i+3].value:
                self.high_value = self.hand[i].value
                return True
        return False

    def compare_highest(self, at_hand):
        sum1 = 0
        sum2 = 0
        i = 0
        while sum1 == sum2:
            sum1 += self.hand[i].value
            sum2 += at_hand.hand[i].value
            if sum1 > sum2:
                return 1
            elif sum1 < sum2:
                return -1
            i += 1
        return 0

    def rank(self):
        if self.is_straight() and self.is_flush() and self.hand[0].value == 14:
            self.rank_level = 9
            return self.rank_level
        elif self.is_straight() and self.is_flush():
            self.rank_level = 8
            return self.rank_level
        elif self.is_four_of_kind():
            self.rank_level = 7
            return self.rank_level
        elif self.is_three_pair() and self.num_pair() == 3:
            self.rank_level = 6
            return self.rank_level
        elif self.is_flush():
            self.rank_level = 5
            return self.rank_level
        elif self.is_straight():
            self.rank_level = 4
            return self.rank_level
        elif self.is_three_pair():
            self.rank_level = 3
            return self.rank_level
        elif self.num_pair() == 2:
            self.rank_level = 2
            return self.rank_level
        elif self.num_pair() == 1:
            self.rank_level = 1
            return self.rank_level
        else:
            self.rank_level = 0
            return self.rank_level

    def get_rank_type(self):
        if self.rank_level == 9:
            return "Royal Flush"
        elif self.rank_level == 8:
            return "Straight Flush"
        elif self.rank_level == 7:
            return "Four-of-a-kind"
        elif self.rank_level == 6:
            return "Full House"
        elif self.rank_level == 5:
            return "Flush"
        elif self.rank_level == 4:
            return "Straight"
        elif self.rank_level == 3:
            return "Three-of-a-kind"
        elif self.rank_level == 2:
            return "Two Pair"
        elif self.rank_level == 1:
            return "One Pair"
        elif self.rank_level == 0:
            return "High Card"
        else:
            return""

    def compare(self, at_hand):
        if self.rank_level > at_hand.rank_level:
            return 1
        elif self.rank_level < at_hand.rank_level:
            return -1

        if self.rank_level == 9 and at_hand.rank_level == 9:
            return 0
        elif self.rank_level == 8 and at_hand.rank_level == 8:
            return self.compare_highest(at_hand)
        elif self.rank_level == 7 and at_hand.rank_level == 7:
            if self.high_value < at_hand.high_value:
                return 1
            else: #cannot tie in 4-of-kind
                return -1
        elif self.rank_level == 6 and at_hand.rank_level == 6:
            if self.high_value < at_hand.high_value:
                return 1
            else: # cannot tie in full house
                return -1
        elif self.rank_level == 5 and at_hand.rank_level == 5:
            return self.compare_highest(at_hand)
        elif self.rank_level == 4 and at_hand.rank_level == 4:
            if self.high_straight_value > at_hand.high_straight_value:
                return 1
            elif self.high_straight_value < at_hand.high_straight_value:
                return -1
            else:
                return 0
        elif self.rank_level == 3 and at_hand.rank_level == 3:
            if self.high_value > at_hand.high_value:
                return 1
            elif self.high_value < at_hand.high_value:
                return -1
            else:
                return 0
        elif self.rank_level == 2 and at_hand.rank_level == 2:
            if self.high_pair_value[0] > at_hand.high_pair_value[0]:
                return 1
            elif self.high_pair_value[0] < at_hand.high_pair_value[0]:
                return -1
            elif self.high_pair_value[1] > at_hand.high_pair_value[1]:
                return 1
            elif self.high_pair_value[1] < at_hand.high_pair_value[1]:
                return -1
            else:
                return 0
        elif self.rank_level == 1 and at_hand.rank_level == 1:
            if self.high_pair_value[0] > at_hand.high_pair_value[0]:
                return 1
            elif self.high_pair_value[0] < at_hand.high_pair_value[0]:
                return -1
            elif self.high_pair_value[2] > at_hand.high_pair_value[2]:
                return 1
            elif self.high_pair_value[2] < at_hand.high_pair_value[2]:
                return -1
            else:
                return 0
        elif self.rank_level == 0 and at_hand.rank_level == 0:
            return self.compare_highest(at_hand)
