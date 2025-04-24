from random import randint
from time import sleep

print("Welcome to BlackJack!")

user_money = 1000

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
        elif isinstance(card, str) and card != "ace":
            total += 10
        elif card == "ace" and total <= 10:
            total += 11
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

def game_start():

    global bet
    global user_money
    global user_hand
    global user_score
    global dealer_hand
    global dealer_score

    user_hand = []
    user_score = 0
    dealer_hand = []
    dealer_score = 0

    bet = int(input(f"You currently have {user_money}. Please place your bet:").strip())
    
    while bet > user_money:
        bet = int(input(f"You currently have {user_money}. Please place your bet:").strip())

    draw_two_cards()

    if user_score == 21:
        print("BlackJack! You win!")
        print(f"Your hand: {user_hand}")
        print(f"Dealer's hand: {dealer_hand}")
        user_money += (bet * 1.5).ceil()
        play_again()
    if dealer_score == 21 and user_score < 21:
        print("Dealer BlackJack! Unlucky!")
        print(f"Your hand: {user_hand}")
        print(f"Dealer's hand: {dealer_hand}")
        user_money -= bet
        play_again()
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

    if dealer_score < 17:
        print(f"Dealer hand: {dealer_hand}")
        print("Drawing cards...")
    elif dealer_score >= 17 and user_score >= 21:
        print("Showing dealer card...")

    while dealer_score < 17:
        dealer_hand = draw_card(dealer_hand)
        dealer_score = calculate_score(dealer_hand)
        if "ace" in dealer_hand and dealer_score <= 10:
            dealer_score += 10

    sleep(2)
    print(f"Your hand: {user_hand}")
    print(f"Dealer hand: {dealer_hand}")

    game_outcome(False)

def hit_stand():

    global bet
    global user_hand
    global user_score
    global user_money

    hit_stand = input("Hit or stand?")

    if "ace" in user_hand and user_score <= 10:
            user_score += 10

    while hit_stand == "hit":
        user_hand = draw_card(user_hand)
        user_score = calculate_score(user_hand)
        print(f"Your hand: {user_hand}")

        if user_score >= 21:
            break

        hit_stand = input("Hit or stand?")
    dealer_show()

def play_again():
    play = input((f"You now have {user_money}. Play again? (y/n)"))
    if play.lower() == "y":
        game_start()

def game_outcome(outcome):

    global user_money
    global user_score
    global dealer_score
    global bet

    # user bust
    if user_score > 21:
        print("You bust! Better luck next time!")
        outcome = False

    # dealer bust
    elif dealer_score > 21:
        print("Dealer bust! Congratulations, you win!")
        outcome = True
    
    # dealer higher than user
    elif dealer_score > user_score:
        print("Dealer wins! Better luck next time.")
        outcome = False

    # user higher than dealer
    elif dealer_score < user_score and user_score <= 21:
        print("You win! Nice job!")
        outcome = True
    
    if outcome == False:
        # push
        if dealer_score == user_score and dealer_score <= 21:
            print("Push!")
        else:
            user_money -= bet
    else:
        user_money += bet
    

game_start()