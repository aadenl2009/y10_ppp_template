# testing some more

# and some more


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

        num = randint(1, 13)
        if num == 11:
            x.append("jack")
        elif num == 12:
            x.append("queen")
        elif num == 13:
            x.append("king")
        
        if num > 10:
            y += 10
        else:
            y += num
            x.append(num)

def game_start():
    bet = input(f"You currently have {user_money}. Please place your bet:")

    if user_score == 21:
        print("BlackJack! You win!")
        user_money += bet * 1.5
        play_again = input((f"You now have {user_money}. Play again? (y/n)"))

        if play_again == "y":
            game_start()

    else:
        draw_two_cards(user_hand, user_score)
        print(f"Your hand: {user_hand}")

        draw_two_cards(dealer_hand, dealer_score)
        print(f"Dealer's hand: {dealer_hand[0]}, x")

def draw_cards():
    hit_stand = input("Hit or stand? (y/n)")

game_start()