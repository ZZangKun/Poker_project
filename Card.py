
#The Card class takes the attributes of suit and value to creat a poker card with the correponding suit and value
#The major method of the class is the image_file_name(), which generates the name of the image file of the poker cards that help to open the image.

class Card:

    card_name = ["", "", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{Card.card_name[self.value]} of {self.suit}"

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit

    def image_file_name(self):
        if self.value < 11:
            return f"{self.value}_of_{self.suit}.png"
        else:
            return f"{Card.card_name[self.value]}_of_{self.suit}.png"
