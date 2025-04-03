import random
import colorama
import time
from random import randint
from time import sleep

print("Welcome to BlackJack!")

user_money = 1000

user_hand = []
user_score = 0

dealer_hand = []
dealer_score = 0

def draw_two_cards():

    global user_score
    global dealer_score
    global user_hand
    global dealer_hand

    for i in range(2):
        score, hand =  draw_card(user_hand, user_score)
        user_score += score
        user_hand += hand

        score, hand =  draw_card(dealer_hand, dealer_score)
        dealer_score += score
        dealer_hand += hand

def draw_card(hand, score):

    num = randint(1, 13)
    if num == 11:
        hand.append("jack")
    elif num == 12:
        hand.append("queen")
    elif num == 13:
        hand.append("king")
    
    if num > 10:
        score += 10
    else:
        score += num
        hand.append(num)
    
    return score, hand

def game_start():
 
    global user_money
    bet = input(f"You currently have {user_money}. Please place your bet:").strip()

    # checks if bet is a whole number
    while not bet.isnumeric():
        bet = input(f"You currently have {user_money}. Please place your bet:")
    
    bet = int(bet)

    draw_two_cards()

    if user_score == 21:
        print("BlackJack! You win!")
        user_money += bet * 1.5
        play_again = input((f"You now have {user_money}. Play again? (y/n)"))

        if play_again == "y":
            game_start()
    else:
        print(f"Your hand: {user_hand}")

        print(f"Dealer's hand: [{dealer_hand[0]}, x]")
    
    main()

def dealer_show():

    global dealer_score
    global user_score
    global dealer_hand

    print(f"Dealer hand: {dealer_hand}")
    while dealer_score < 17:
        score, hand =  draw_card(dealer_hand, dealer_score)
        dealer_score += score
        dealer_hand += hand
    print("Drawing cards...")
    sleep(2)
    print(f"Dealer hand: {dealer_hand}")
    if dealer_score > 21:
        print("Dealer bust! Congratulations, you win!")
    if dealer_score > user_score and dealer_score <= 21:
        print("Dealer wins! Better luck next time.")
    elif dealer_score < user_score and user_score <= 21:
        print("You win! Nice job!")
    print(dealer_score)
    print(user_score)

def main():
    hit_stand = input("Hit or stand?").lower().strip()

    while hit_stand != "hit" and hit_stand != "stand" and user_score < 21:
        hit_stand = input("Hit or stand?")

    if hit_stand == "hit":
        draw_card(user_hand, user_score)
        print(print(f"Your hand: {user_hand}"))
    else:
        dealer_show()

game_start()