# testing

# blackjack

import random
import colorama
from random import randint

print ("Welcome to BlackJack!\n🟥🟧🟨🟩🟦🟪🟫⬛⬜")

user_money = 1000

user_hand = []
user_score = 0

dealer_hand = []
dealer_score = 0

def draw_two_cards(x, y):
    for i in range(2):
        x.append(randint(1, 13))
        if x[i] == 11:
            x.append("jack")
        elif x[i] == 12:
            x.append("queen")
        elif x[i] == 13:
            x.append("king")
        
        if x[i] == "jack" or "queen" or "king":
            y += 10
        else:
            y += x[i]
    
    print(x)
    print(y)

def first_two_cards():
    bet = input(f"You currently have {user_money}. Please place your bet:")
    
    # draw the cards
    
        
        # repeat for the dealer     

    print(user_hand)
    print(user_score)

first_two_cards()
draw_two_cards(user_hand, user_score)