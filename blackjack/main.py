import random
from art import logo
from replit import clear

# For simplicity K, Q, J, A are represented by their numerical
# value. Randomization of dealt cards is not reflective of 
# their occurrances in a standard deck and can appear multiple 
# times in a single game.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Generate starting hand for player and dealer
def start_hand():
    global player_hand
    global computer_hand
    player_hand = [random.choice(cards), random.choice(cards)]
    computer_hand = [random.choice(cards)]

def display_hand():
    print(f"Your hand: {player_hand} Total: {calculate_total(player_hand)}")
    print(f"Dealer hand: {computer_hand} Total: {calculate_total(computer_hand)}")

def draw_card(hand):
    hand.append(random.choice(cards))

def calculate_total(hand):
    return sum(hand)

# If hand sum goes over 21 this method converts all high aces (11)
# to a low ace (1)
def hand_is_bust(hand):
    if calculate_total(hand) > 21:
        ace_equals_one(hand)
    if calculate_total(hand) > 21:
        return True
    else:
        return False

# Converts high ace cards (11) to low ace cards (1)
def ace_equals_one(hand):
    for card in range(0, len(hand) - 1):
        if hand[card] == 11:
            hand[card] = 1
            print(card)

# After player's turn. Dealer will draw until hand sum is 17
# or goes over 21
def dealers_turn(hand):
    global game_over

    dealer_total = calculate_total(hand)
    if hand_is_bust(computer_hand):
        display_hand()
        print("Dealer has bust. You win!")
        game_over = True
    elif dealer_total >= 17:
        return dealer_total
    else:
        draw_card(hand)
        dealers_turn(hand)

def check_blackjack(hand):
    if calculate_total(hand) == 21 and len(hand) == 2:
        return True
    else:
        return False

def play_game():
    print(logo)
    start_hand()
    game_over = False   
    continue_draw = True

    if check_blackjack(player_hand) == True:
        print("Blackjack You Win!")
        continue_draw = False
        game_over = True
    
    while continue_draw:
         
        display_hand()
       
        draw_again = input("Would you like to draw again? Type 'yes' or 'no': ")

        if draw_again == 'no':
            continue_draw = False          
        elif draw_again == 'yes':
            draw_card(player_hand)

            if hand_is_bust(player_hand):
                display_hand()
                print("Dealer wins!")
                continue_draw = False
                game_over = True
        else:
            print("Make sure you enter a valid response")
            continue

    dealers_turn(computer_hand)
    if check_blackjack(computer_hand) == True:
        print("Dealer has a Blackjack. Dealer Wins")
        game_over = True

    if game_over == False:
        
        dealer_total = calculate_total(computer_hand)
        player_total = calculate_total(player_hand)
        
        if dealer_total < player_total:
            display_hand()
            print("You win!")
        elif dealer_total == player_total:
            display_hand()
            print("This round is a draw")
        else:
            display_hand()
            print("Dealer wins")

keep_playing = True

while keep_playing:
   
    play_game()
    
    if input("would you like to play another game? Type 'yes' or 'no' ") != 'yes':
        keep_playing = False
   
    clear()

    







































