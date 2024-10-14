#Capstone Project (Black jack game)
import random

card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

def deal_card():
    cards = list(card_values.keys())
    return random.choice(cards)

def calculate_hand_value(hand):
    return sum([card_values[card] for card in hand])


def play_game():
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    print("Your hand:", player_hand)
    print("Dealer's up card:", dealer_hand[0])

    # Player's turn
    while True:
        action = input("Do you want to 'hit' or 'stand'? ")
        if action.lower() == 'hit':
            player_hand.append(deal_card())
            print("Your hand:", player_hand)
            if calculate_hand_value(player_hand) > 21:
                print("You bust! Dealer wins.")
                return
        elif action.lower() == 'stand':
            break
        else:
            print("Invalid input. Please enter 'hit' or 'stand'.")

    # Dealer's turn
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card())

    print("Dealer's hand:", dealer_hand)

    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if dealer_value > 21:
        print("Dealer busts! You win.")
    elif player_value > dealer_value:
        print("You win!")
    elif player_value < dealer_value:
        print("Dealer wins.")
    else:
        print("Push. It's a tie.")

