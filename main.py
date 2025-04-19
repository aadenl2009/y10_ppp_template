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
        user_hand = draw_card(user_hand)
        user_score = calculate_score(user_hand)
        dealer_hand = draw_card(dealer_hand)
        dealer_score = calculate_score(dealer_hand)

def calculate_score(cards):
    total = 0
    for card in cards:
        # check if it is an integer
        if isinstance(card, int):
            total += card
        else:
            total += 10
    return total

def draw_card(hand):
    added = hand.copy()
    num = randint(1, 13)
    if num == 11:
        added.append("jack")
    elif num == 12:
        added.append("queen")
    elif num == 13:
        added.append("king")
    else:
        added.append(num)
    return added

def game_start():

    global bet
    global user_money

    bet = int(input(f"You currently have {user_money}. Please place your bet:").strip())

    while bet > user_money:
        bet = int(input(f"You currently have {user_money}. Please place your bet:").strip())

    # checks if bet is a whole number
    while str(float(bet))[-1] != "0":
        bet = int(input(f"You currently have {user_money}. Please place your bet:"))
    

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
    
    hit_stand()

def dealer_show():

    global dealer_score
    global user_score
    global user_money
    global dealer_hand
    global bet

    print(f"Dealer hand: {dealer_hand}")
    while dealer_score < 17:
        dealer_hand = draw_card(dealer_hand)
        dealer_score = calculate_score(dealer_hand)
    if dealer_score >= 17:
        print("Drawing cards...")
    sleep(2)
    print(f"Dealer hand: {dealer_hand}")
    print(f"Your hand: {user_hand}")

    # dealer bust
    if dealer_score > 21:
        print("Dealer bust! Congratulations, you win!")
        user_money += bet
        print(f"You now have {user_money}.")

    # dealer higher than user
    if dealer_score > user_score and dealer_score <= 21:
        print("Dealer wins! Better luck next time.")
        user_money -= bet
        print(f"You now have {user_money}.")
    
    # user higher than dealer
    elif dealer_score < user_score and user_score <= 21:
        print("You win! Nice job!")
        user_money += bet
        print(f"You now have {user_money}.")

    # push
    elif dealer_score == user_score and dealer_score <= 21:
        print("Push!")
        print(f"You now have {user_money}.")

def hit_stand():

    global user_hand
    global user_score

    hit_stand = input("Hit or stand?").lower().strip()

    while hit_stand != "hit" and hit_stand != "stand" and user_score < 21:
        hit_stand = input("Hit or stand?")

    while hit_stand == "hit":
        user_hand = draw_card(user_hand)
        user_score = calculate_score(user_hand)
        if user_score > 21:
            print("Bust! Better luck next time!")
        hit_stand = input("Hit or stand?")

        print(f"Your hand: {user_hand}")

    dealer_show()

game_start()