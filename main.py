from random import randint
from time import sleep
import os

os.system('clear')
print("Welcome to BlackJack!\n")

# set var
user_money = 1000
user_hand = []
user_score = 0
dealer_hand = []
dealer_score = 0
user_hand_2 = []
user_score_2 = 0
hand_2 = False
doubled = False
bet = 0

def draw_two_cards(user_score, dealer_score, user_hand, dealer_hand):

    for i in range(2):
        user_hand = draw_card(user_hand)
        user_score = calculate_score(user_hand)
        dealer_hand = draw_card(dealer_hand)
        dealer_score = calculate_score(dealer_hand)

    return user_score, dealer_score, user_hand, dealer_hand

def calculate_score(hand):
    total = 0
    for card in hand:
        # check if it is an integer
        if isinstance(card, int):
            total += card
        elif isinstance(card, str) and card != "ace":
            total += 10
        elif card == "ace" and total <= 10:
            total += 11
        elif card == "ace" and total > 10:
            total += 1
    
    if "ace" in hand and total > 21:
        total -= 10 
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
    elif num == 1:
        added.append("ace")
    else:
        added.append(num)
    return added

def game_start(user_money, user_hand, user_score, dealer_hand, dealer_score, user_hand_2, doubled):

    bet = input(f"You currently have {user_money}. Please place your bet: ").strip()
    
    while not bet.isnumeric() or int(bet) > user_money or int(bet) == 0:
        bet = input(f"Invalid input! You currently have {user_money}. Please place your bet:").strip()

    bet = int(bet)
    
    user_score, dealer_score, user_hand, dealer_hand = draw_two_cards(user_score, dealer_score, user_hand, dealer_hand)

    os.system('clear')

    if user_score == 21:
        print("BlackJack! You win!\n")
        print(f"Your hand: {user_hand}\n")
        print(f"Dealer's hand: {dealer_hand}\n")
        user_money += (bet * 1.5)
        user_money = play_again(user_money)

    elif dealer_score == 21 and user_score < 21:
        print("Dealer BlackJack! Unlucky!\n")
        print(f"Your hand: {user_hand}\n")
        print(f"Dealer's hand: {dealer_hand}\n")
        user_money -= bet
        user_money = play_again(user_money)

    else:
        print(f"Your hand: {user_hand}\n")
        print(f"Dealer's hand: [{dealer_hand[0]}, x]\n")
    
    user_hand, user_hand_2 = split(user_hand, user_score, hand_2, user_hand_2, user_score_2, bet, user_money, doubled)

    if bet * 2 <= user_money:
        user_hand, user_score, doubled = double_down(user_hand, user_score, bet, user_money, dealer_hand, dealer_score, doubled)

    return user_hand, user_score, dealer_hand, dealer_score, bet, doubled

def dealer_show(dealer_score, user_money, dealer_hand, user_hand, user_hand_2, bet, hand_2, user_score, doubled):

    user_hand, user_hand_2 = split(user_hand, user_score, hand_2, user_hand_2, user_score_2, bet, user_money, doubled)

    os.system('clear')

    if dealer_score < 17:
        print("Drawing cards...\n")
    elif dealer_score >= 17 and user_score <= 21 and hand_2 == False:
        print("Showing dealer card...\n")

    while dealer_score < 17:
        dealer_hand = draw_card(dealer_hand)
        dealer_score = calculate_score(dealer_hand)

    sleep(2)
    if hand_2 == False:
        print(f"Your hand: {user_hand}\n")
        print(f"Dealer hand: {dealer_hand}\n")
    else:
        print(f"Hand 1: {user_hand}\n")
        print(f"Hand 2: {user_hand_2}\n")
        print(f"Dealer hand: {dealer_hand}\n")

    return dealer_hand, dealer_score

def hit_stand(hand, score, hand_2, doubled):

    if doubled == False:
        hit_stand = input("Hit or stand?").lower().strip()

        while hit_stand != "hit" and hit_stand != "stand":
            hit_stand = input("Invalid input! Hit or stand?").lower().strip()

        print("\n")

        while hit_stand == "hit":
            hand = draw_card(hand)
            score = calculate_score(hand)
            print(f"Your hand: {hand}")

            if score > 21:
                print("You went over 21!\n")
                break

            hit_stand = input("Hit or stand?").lower().strip()

    if hand_2 == True:
        hand = split(user_hand, user_score, hand_2, user_hand_2, user_score_2, bet, user_money, doubled)

    return hand, score

def play_again(user_money):

    if user_money > 0:
        play = input((f"You now have {user_money}. Play again? (y/n) ")).strip().lower()
        while play != "y" and play != "n":
            play = input((f"Invalid input! Play again? (y/n) "))

        print("\n")
        
        if play.lower() == "y":
            os.system('clear')
            main(user_hand, user_score, dealer_hand, dealer_score, user_money, bet, doubled)
        else:
            print("Thanks for playing!")
    else:
        print("Game over!")
    quit()

def double_down(user_hand, user_score, bet, user_money, dealer_hand, dealer_score, doubled):

    double_down = input("Double down? (y/n) ").strip().lower()

    while double_down != "y" and double_down != "n":
        double_down = input("Invalid input! Double down? (y/n) ").strip().lower()

    if double_down == "y":
        doubled = True
        bet *= 2
        user_hand = draw_card(user_hand)
        user_score = calculate_score(user_hand)
        dealer_hand, dealer_score = dealer_show(dealer_score, user_money, dealer_hand, user_hand, user_hand_2, bet, hand_2, user_score, doubled)

    return user_hand, user_score, doubled

def split(user_hand, user_score, hand_2, user_hand_2, user_score_2, bet, user_money, doubled):

    if user_hand[0] == user_hand [1] and hand_2 == False and bet * 2 <= user_money:
        split_choice = input("Split? (y/n)").lower().strip()
        if split_choice == "y" and hand_2 == False:
            for i in range(2):
                print("\n")
                user_hand = draw_card(user_hand[:1])
                user_hand_2 = draw_card(user_hand[1:])
            user_score = calculate_score(user_hand)       
            user_score_2 = calculate_score(user_hand_2)
            print(f"Hand 1: {user_hand}\n")
            hand_2 = True
            user_hand, user_score = hit_stand(user_hand, user_score, hand_2, doubled)
    if hand_2 == True:
        print(f"Hand 2: {user_hand_2}\n")
        hand_2 = False
        user_hand_2, user_score_2 = hit_stand(user_hand_2, user_score_2, hand_2, doubled)

    return user_hand, user_hand_2

def game_outcome(user_money, user_score, dealer_score, bet):

    outcome = False

    # user bust
    if user_score > 21 and dealer_score > 21:
        print("Push!\n")

    else:
        if user_score > 21:
            print("You bust! Better luck next time!\n")
        
        # dealer bust
        elif dealer_score > 21:
            print("Dealer bust! Congratulations, you win!\n")
            outcome = True
        
        # user higher than dealer
        elif dealer_score < user_score and user_score <= 21:
            print("You win! Nice job!\n")
            outcome = True
        
        # dealer higher than user
        elif dealer_score > user_score:
            print("Dealer wins! Better luck next time.\n")

    if outcome == False:
        # push
        if dealer_score == user_score and dealer_score <= 21:
            print("Push!\n")
        # double bust
        elif user_score > 21 and dealer_score > 21:
            print("Double bust! Push!\n")
        else:
            print("You lost.\n")
            user_money -= bet
    else:
        user_money += bet

    return user_money

def main(user_hand, user_score, dealer_hand, dealer_score, user_money, bet, doubled):

    user_hand, user_score, dealer_hand, dealer_score, bet, doubled = game_start(user_money, user_hand, user_score, dealer_hand, dealer_score, user_hand_2, doubled)
    user_hand, user_score = hit_stand(user_hand, user_score, hand_2, doubled)
    dealer_hand, dealer_score = dealer_show(dealer_score, user_money, dealer_hand, user_hand, user_hand_2, bet, hand_2, user_score, doubled)
    user_money = game_outcome(user_money, user_score, dealer_score, bet)
    play_again(user_money)

main(user_hand, user_score, dealer_hand, dealer_score, user_money, bet, doubled)