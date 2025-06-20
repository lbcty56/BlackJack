import art
import random

def create_deck():
    deck = []
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    symbols = ["♤", "♡", "♧", "♢"]
    for number in cards:
        for symbol in symbols:
            deck.append(symbol+number)
    random.shuffle(deck)
    return deck

def deal_card(deck):
    return deck.pop(0)

def first_round_deal(deck_list, player_hand, computer_hand):
    for i in range(4):
        if i % 2 == 0:
            computer_hand.append(deal_card(deck_list))
        else:
            player_hand.append(deal_card(deck_list))

def print_hand(player_hand, computer_hand):
    player_hand_string = " ".join(player_hand)
    print(f"Player Hand: {player_hand_string}")
    computer_hide_hand = " ".join(computer_hand[1:])
    print(f"Computer Hand: X {computer_hide_hand}")

def evaluate_hand(boundary_list):
    diff = boundary_list[1] - boundary_list[0]
    possible_values = int(diff / 10 + 1)
    possible_values_list = []
    for i in range(0, possible_values):
        possible_values_list.append(boundary_list[0] + 10 * i)
    return possible_values_list

def find_closest_value_to_21(values_list):
    if values_list[0] > 21:
        return values_list[0]
    closest_value = 0
    for i in values_list:
        if i <= 21:
            closest_value = i
        else:
            break
    return closest_value

def sum_hand(hand):
    upper_bound = 0
    lower_bound = 0
    for card in hand:
        try:
            upper_bound += int(card[1:])
            lower_bound += int(card[1:])
        except ValueError:
            if card[1] == "A":
                upper_bound += 11
                lower_bound += 1
            else:
                upper_bound += 10
                lower_bound += 10
    return [lower_bound, upper_bound]

def compare_value(player_value, computer_value):
    if player_value > 21:
        return "Lose"
    elif computer_value > 21:
        return "Win"
    else:
        if player_value == computer_value:
            return "Tie"
        elif player_value > computer_value:
            return "Win"
        elif player_value < computer_value:
            return "Lose"


def handle_hand(hand_list):
    boundaries = sum_hand(hand_list)
    hand_values_list = evaluate_hand(boundaries)
    closest_value_to_21 = find_closest_value_to_21(hand_values_list)
    return closest_value_to_21

def player_logic(deck, player_hand, computer_hand):
    player_closest_value = handle_hand(player_hand)
    print_hand(player_hand, computer_hand)
    while player_closest_value < 21:
        get_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if get_card == "y" or get_card == "yes":
            player_hand.append(deal_card(deck))
            player_closest_value = handle_hand(player_hand)
            print_hand(player_hand, computer_hand)
        elif get_card == "n" or get_card == "no":
            break
        else:
            continue
    return player_closest_value

def computer_logic(deck, computer_hand):
    computer_closest_value = handle_hand(computer_hand)
    while computer_closest_value < 17:
        computer_hand.append(deal_card(deck))
        computer_closest_value = handle_hand(computer_hand)
    return computer_closest_value

def start_game():
    while True:
        start_choice = input("Do you want to play a game of BlackJack? ").lower()
        if start_choice == "n" or start_choice == "no":
            print("Good Bye")
            break
        elif start_choice == "y" or start_choice == "yes":
            player_hand = []
            computer_hand = []

            print(art.logo)

            current_deck = create_deck()
            first_round_deal(current_deck, player_hand, computer_hand)

            player_closest_value = player_logic(current_deck, player_hand, computer_hand)

            computer_closest_value = computer_logic(current_deck, computer_hand)

            end_msg = compare_value(player_closest_value, computer_closest_value)
            player_hand_string = " ".join(player_hand)
            computer_hand_string = " ".join(computer_hand)
            print(f"Player Hand: {player_hand_string}")
            print(f"Computer Hand: {computer_hand_string}")
            print(end_msg)

start_game()
