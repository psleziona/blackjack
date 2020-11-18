import random

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
cards_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10,
                'A': 11}

starting_cards = 4 * cards


def pick_card():
    global starting_cards
    card = starting_cards.pop(random.randint(0, len(starting_cards) - 1))
    return card


def round():
    croupier_cards = []
    player_cards = []
    croupier_status = lambda x: 'Croupier points: {}'.format(count_points(x))
    player_status = lambda x: 'Your points: {}'.format(count_points(x))
    croupier_cards.append(pick_card())
    print(croupier_status(croupier_cards))
    print(player_status(player_cards))
    while True:
        action = input('Choose your action: 1. Take card, 2. Pass\n')
        if action == '1':
            player_cards.append(pick_card())
            print(player_status(player_cards))
            if count_points(player_cards) > 21:
                print('You loose')
                break
            elif count_points(player_cards) == 21:
                print('You won')
                break
        elif action == '2':
            while True:
                if count_points(croupier_cards) <= count_points(player_cards):
                    croupier_cards.append(pick_card())
                    print(croupier_status(croupier_cards))
                if count_points(croupier_cards) > 21:
                    print('Casino loose, player win!')
                    break
                if count_points(player_cards) < count_points(croupier_cards) < 22:
                    print('Casino won')
                    break
            break


def count_points(arr):
    total = 0
    try:
        if (arr[0] == 'A' and (arr[1] == '10' or arr[1] == 'J' or arr[1] == 'Q' or arr[1] == 'K')) or (
                (arr[0] == '10' or arr[0] == 'J' or arr[0] == 'Q' or arr[0] == 'K') and arr[1] == 'A'):
            print('Black jack')
            return 21
    except IndexError:
        pass
    for card in arr:
        if card == 'A':
            if total + cards_values[card] > 21:
                total += 1
                continue
        total += cards_values.get(card)
    return total


def prepare_dec():
    global starting_cards
    starting_cards = 4 * cards


while True:
    print('To start round press 1, to finish press 2, start with new deck press 3')
    action = input()
    if action == '1':
        round()
    elif action == '2':
        break
    elif action == '3':
        prepare_dec()
        round()
