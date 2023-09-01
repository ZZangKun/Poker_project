import Card
import Deck
import Hand
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def make_row(img1, img2, img3, img4, img5):
    row = Image.new('RGB', (img1.width*6+35, img1.height))
    row.paste(img1, (0, 0))
    row.paste(img2, (img1.width, 0))
    row.paste(img3, (img1.width+img2.width, 0))
    row.paste(img4, (img1.width + img2.width+img3.width, 0))
    row.paste(img5, (img1.width + img2.width+img3.width+img4.width, 0))
    return row

def make_column(img1, img2, img3, img4):
    col = Image.new('RGB', (img1.width, img1.height*4))
    col.paste(img1, (0, 0))
    col.paste(img2, (0, img1.height))
    col.paste(img3, (0, img1.height+img2.height))
    col.paste(img4, (0, img1.height + img2.height+img3.height))
    return col


if __name__ == '__main__':
    Deck1 = Deck.Deck()
    Deck1.shuffle()

    #create a list of hands
    poker_game = []
    winner = []
    for i in range(4):
        poker_game.append(Hand.Hand())
        winner.append(0)

    #add cards to the hands
    for i in range(5):
        for j in range(len(poker_game)):
            poker_game[j].add_card(Deck1.deal_card())

    #rank each hand
    for i in range(len(poker_game)):
        poker_game[i].rank()

    #find winners
    current_winner = 0
    is_tie = True
    for i in range(1, len(poker_game)):
        if poker_game[i].compare(poker_game[current_winner]) == 1:
            current_winner = i
            is_tie = False
        if current_winner == 0:
            is_tie = False

    #create image
    hand1 = make_row(Image.open('Poker Images/' + poker_game[0].hand[0].image_file_name()),
                     Image.open('Poker Images/' + poker_game[0].hand[1].image_file_name()),
                     Image.open('Poker Images/' + poker_game[0].hand[2].image_file_name()),
                     Image.open('Poker Images/' + poker_game[0].hand[3].image_file_name()),
                     Image.open('Poker Images/' + poker_game[0].hand[4].image_file_name()))
    hand2 = make_row(Image.open('Poker Images/' + poker_game[1].hand[0].image_file_name()),
                     Image.open('Poker Images/' + poker_game[1].hand[1].image_file_name()),
                     Image.open('Poker Images/' + poker_game[1].hand[2].image_file_name()),
                     Image.open('Poker Images/' + poker_game[1].hand[3].image_file_name()),
                     Image.open('Poker Images/' + poker_game[1].hand[4].image_file_name()))
    hand3 = make_row(Image.open('Poker Images/' + poker_game[2].hand[0].image_file_name()),
                     Image.open('Poker Images/' + poker_game[2].hand[1].image_file_name()),
                     Image.open('Poker Images/' + poker_game[2].hand[2].image_file_name()),
                     Image.open('Poker Images/' + poker_game[2].hand[3].image_file_name()),
                     Image.open('Poker Images/' + poker_game[2].hand[4].image_file_name()))
    hand4 = make_row(Image.open('Poker Images/' + poker_game[3].hand[0].image_file_name()),
                     Image.open('Poker Images/' + poker_game[3].hand[1].image_file_name()),
                     Image.open('Poker Images/' + poker_game[3].hand[2].image_file_name()),
                     Image.open('Poker Images/' + poker_game[3].hand[3].image_file_name()),
                     Image.open('Poker Images/' + poker_game[3].hand[4].image_file_name()))

    img = make_column(hand1, hand2, hand3, hand4)

    I1 = ImageDraw.Draw(img)
    card_font = ImageFont.truetype('Arial', 15)
    winner_font = ImageFont.truetype('Arial', 18)
    text_y_axis = (70, 200, 350, 500)
    for i in range(len(poker_game)):
        I1.text((img.width - 120, text_y_axis[i]), poker_game[i].get_rank_type(), font=card_font, fill=(255, 255, 255))

    if is_tie:
        print("Tie:")
        for i in range(0, len(poker_game)):
            if poker_game[i].compare(poker_game[current_winner]) == 0:
                winner[i] += 1
                poker_game[i].print_hand()
    else:
        I1.text((img.width - 120, text_y_axis[current_winner]+30), "Winner!", font=winner_font, fill=(255, 0, 0))

    img.show()

    #text( (x, y), "text content", font, fill=(r,g,b)  )
