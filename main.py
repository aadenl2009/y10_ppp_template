from random import randint
from time import sleep

print("Welcome to BlackJack!")

user_money = 1000
user_hand = []
user_score = 0
dealer_hand = []
dealer_score = 0
user_hand_2 = 0
user_score_2 = 0
hand_2 = False
bet = 0

def draw_two_cards(user_score, dealer_score, user_hand, dealer_hand):

    for i in range(2):
        u_hand = draw_card(user_hand)
        user_score = calculate_score(user_hand)
        dealer_hand = draw_card(dealer_hand)
        dealer_score = calculate_score(dealer_hand)

    return user_score, dealer_score, user_hand, dealer_hand

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
        elif card == "ace" and total > 10:
            total += 1
    
    if "ace" in cards and total > 21:
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

def game_start(bet, user_money, user_hand, user_score, dealer_hand, dealer_score):

    bet = input(f"You currently have {user_money}. Please place your bet:").strip()
    
    while not bet.isnumeric() or int(bet) > user_money:
        bet = input(f"Invalid input! You currently have {user_money}. Please place your bet:").strip()

    bet = int(bet)
    
    user_score, dealer_score, user_hand, dealer_hand = draw_two_cards(user_score, dealer_score, user_hand, dealer_hand)

    if user_score == 21:
        print("BlackJack! You win!")
        print(f"Your hand: {user_hand}")
        print(f"Dealer's hand: {dealer_hand}")
        user_money += (bet * 1.5)
        play_again()

    elif dealer_score == 21 and user_score < 21:
        print("Dealer BlackJack! Unlucky!")
        print(f"Your hand: {user_hand}")
        print(f"Dealer's hand: {dealer_hand}")
        user_money -= bet
        play_again()

    else:
        print(f"Your hand: {user_hand}")
        print(f"Dealer's hand: [{dealer_hand[0]}, x]")
    
    split(user_hand, user_score, hand_2, user_hand_2, user_score_2, bet, user_money)

    if bet * 2 <= user_money:
        double_down()
    
    hit_stand(user_hand, user_score)

def dealer_show(hand, score):

    global dealer_score
    global user_money
    global dealer_hand
    global user_hand_2
    global bet
    global hand_2

    if hand_2 == True:
        split(user_hand, user_score, hand_2, user_hand_2, user_score_2, bet, user_money)

    if dealer_score < 17:
        print("Drawing cards...")
    elif dealer_score >= 17 and score <= 21 and hand_2 == False:
        print("Showing dealer card...")

    while dealer_score < 17:
        dealer_hand = draw_card(dealer_hand)
        dealer_score = calculate_score(dealer_hand)

    sleep(2)
    if hand_2 == False:
        print(f"Your hand: {hand}")
        print(f"Dealer hand: {dealer_hand}")
    else:
        print(f"Hand 1: {hand}")
        print(f"Hand 2: {user_hand_2}")
        print(f"Dealer hand: {dealer_hand}")

    game_outcome()

    play_again()

def hit_stand(hand, score):

    global bet
    global user_money

    hit_stand = input("Hit or stand?").lower().strip()
    while hit_stand != "hit" and hit_stand != "stand":
        hit_stand = input("Invalid input! Hit or stand?").lower().strip()

    while hit_stand == "hit":
        hand = draw_card(hand)
        score = calculate_score(hand)
        print(f"Your hand: {hand}")

        if score > 21 and "ace" not in hand:
            print("You went over 21!")
            break

        hit_stand = input("Hit or stand?")
    dealer_show(hand, score)

def play_again():

    global user_money

    if user_money > 0:
        play = input((f"You now have {user_money}. Play again? (y/n)"))
        if play.lower() == "y":
            game_start()
        else:
            print("Thanks for playing!")
    else:
        print("Game over!")
    quit()

def double_down():

    global user_hand
    global user_score
    global bet
    global user_money

    double_choice = False
    double_down = input("Double down? (y/n)").strip().lower()

    while double_down != "y" and double_down != "n":
        double_down = input("Invalid input! Double down? (y/n)").strip().lower()

    if double_down == "y":
        double_choice = True
        bet *= 2
        user_hand = draw_card(user_hand)
        user_score = calculate_score(user_hand)
        dealer_show(user_hand, user_score)
    
    return double_choice

def split(user_hand, user_score, hand_2, user_hand_2, user_score_2, bet, user_money):

    if user_hand[0] == user_hand [1] and hand_2 == False and bet * 2 <= user_money:
        split_choice = input("Split? (y/n)").lower().strip()
        if split_choice == "y" and hand_2 == False:
            for i in range(2):
                user_hand = draw_card(user_hand[:1])
                user_hand_2 = draw_card(user_hand[1:])
            user_score = calculate_score(user_hand)       
            user_score_2 = calculate_score(user_hand_2)
            print(f"Hand 1: {user_hand}")
            hand_2 = True
            hit_stand(user_hand, user_score)
    if hand_2 == True:
        print(f"Hand 2: {user_hand_2}")
        hand_2 = False
        hit_stand(user_hand_2, user_score_2)

def game_outcome():

    global user_money
    global user_score
    global dealer_score
    global bet

    outcome = False

    # user bust
    if user_score > 21:
        print("You bust! Better luck next time!")

    # dealer bust
    elif dealer_score > 21:
        print("Dealer bust! Congratulations, you win!")
        outcome = True

    # user higher than dealer
    elif dealer_score < user_score and user_score <= 21:
        print("You win! Nice job!")
        outcome = True
    
    # dealer higher than user
    elif dealer_score > user_score:
        print("Dealer wins! Better luck next time.")
    
    if outcome == False:
        # push
        if dealer_score == user_score and dealer_score <= 21:
            print("Push!")
        # double bust
        elif user_score > 21 and dealer_score > 21:
            print("Double bust! Push!")
        else:
            user_money -= bet
    else:
        user_money += bet

game_start(bet, user_money, user_hand, user_score, dealer_hand, dealer_score)