import random
import os 



def save_game_state(filename, pile, initial_hands):
    with open(filename, 'w') as file:
        file.write(','.join(pile) + '\n')
        for player, cards in initial_hands.items():
            file.write(f'{player},{",".join(cards)}\n')

def load_game_state(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            pile = lines[0].strip().split(',')
            initial_hands = {}
            for line in lines[1:]:
                player, *cards = line.strip().split(',')
                initial_hands[player] = cards
            return pile, initial_hands
    except FileNotFoundError:
        raise

def display_game_state(pile, initial_hands):
    print("\nCURRENT GAME STATE")
    print("PILE:", pile)
    for player, cards in initial_hands.items():
        print(f"{player}: {cards}")


initial_hands = {}

print("Welcome to:\n\n| |  | | | \ | |  / __ \   | |\n| |  | | |  \| | | |  | |  | |\n| |  | | | . ` | | |  | |  | |\n| |__| | | |\  | | |__| |  |_|\n \____/  |_| \_|  \____/   (_)")
try:
    menu = input("\nMENU\nPick 1, 2, or 3\n\n1. Start Game\n2. Load State\n3. Exit\nYour choice: ")
    if not menu.isdigit() or int(menu) not in [1, 2, 3]:
        raise ValueError("Invalid option. Please choose 1, 2, or 3.")
    menu = int(menu)
except ValueError as ve:
    print(f"Error: {ve}")
    print("Please enter a valid number.")
    exit()
if menu == 1:
    player1 = input("Enter player 1's name: ")
    player2 = input("Enter player 2's name: ")

    colors = ["red", "yellow", "green", "blue"]
    values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    deck = []

    for color in colors:
        for value in values:
            card = color + " " + value
            deck.append(card)

    random.shuffle(deck)

    initial_hands = {player1: [], player2: []}
    for i in range(7):
        for player in initial_hands:
            card = deck.pop()
            initial_hands[player].append(card)

    pile = [deck.pop()]
    random.shuffle(deck)  
    
    topofpile = pile[-1]

    print(f"Pile: {topofpile}")
    

    while True:
        for currentplayer in [player1, player2]:
            cardvalidator = False
            print(f"\nCurrent player: {currentplayer}")
            print(f"{currentplayer}'s hand: {initial_hands[currentplayer]}")
            topofpilecolor = topofpile.split()[0]
            topofpilenumber = topofpile.split()[1]
            playershand = initial_hands[currentplayer]

            has_playable_card = False

            for card in playershand:
                        card_color = card.split()[0]
                        card_number = card.split()[1]
                        if card_color == topofpilecolor or card_number == topofpilenumber:
                            has_playable_card = True
                            break

            if not has_playable_card:
                while not has_playable_card and deck:
                    newcard = deck.pop()
                    initial_hands[currentplayer].append(newcard)
                    print(f"No matching cards available in your hand. You picked a card from the deck. Your new card is {newcard}. ")
                    print(f"{currentplayer}'s hand: {initial_hands[currentplayer]}")

                    card_color = newcard.split()[0]
                    card_number = newcard.split()[1]

                    if card_color == topofpilecolor or card_number == topofpilenumber:
                        has_playable_card = True
                        break

            while cardvalidator == False:
                chosencard = input(f"{currentplayer}, choose a card to play: ").lower()
                if chosencard == 'exit':
                    print("Goodbye! Thanks for playing.")
                    exit()
                if chosencard == 'save game':
                    filename = input("Enter the filename to save: ")
                    save_game_state(filename, pile ,initial_hands) 
                    print("Game state saved successfully.")
                    exit()

                chosencardcolor = chosencard.split()[0] 
                chosencardnumber = chosencard.split()[1]                    
                try:
                    if chosencard not in initial_hands[currentplayer]:
                        raise ValueError("Invalid card. Please choose one of the cards in your hand.")
                except ValueError as ve:
                    print(f"Error: {ve}")
                if chosencardcolor == topofpilecolor:
                    cardvalidator = True
                if chosencardnumber == topofpilenumber:
                    cardvalidator = True
                
                if cardvalidator == True:
                    if chosencard in initial_hands[currentplayer]:
                        initial_hands[currentplayer].remove(chosencard)
                        topofpile = chosencard
                        print(f"{currentplayer} played {chosencard}")

                    if not initial_hands[currentplayer]:
                        print(f"{currentplayer} wins!")
                        break
        
                else:
                    print("Invalid card. Try again.")
                    print(f"Pile: {topofpile}")

            if not initial_hands[player1] or not initial_hands[player2]:
                print("Game over!")
                exit()

elif menu == 2:
    filename = input("Enter the filename of the game state to load: ")
    try:
        pile, initial_hands = load_game_state(filename)
        print("\nGAME STATE LOADED SUCCESSFULLY")
        display_game_state(pile, initial_hands)
    except FileNotFoundError as fnfe:
        print(f"Error: {fnfe}")
        print("Please enter a valid filename.")
    else:
        print("\nPress Enter to start playing or type 'save game' and press Enter to save the current game state.")
        start_input = input().lower()
        if start_input == 'save game':
            filename = input("Enter the filename to save: ")
            save_game_state(filename, pile ,initial_hands) 
            print("Game state saved successfully.")
        elif start_input == '':
            print("\nGAME RESUMED")
    player1 = input()
    player2 = input()

    colors = ["red", "yellow", "green", "blue"]
    values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    deck = []

    for color in colors:
        for value in values:
            card = color + " " + value
            deck.append(card)

    

    initial_hands = {player1: [], player2: []}
    for i in range(7):
        for player in initial_hands:
            card = deck.pop()
            initial_hands[player].append(card)

    pile = [deck.pop()]
    random.shuffle(deck)  
    
    topofpile = pile[-1]

    print(f"Pile: {topofpile}")
    

    while True:
        for currentplayer in [player1, player2]:
            cardvalidator = False
            print(f"\nCurrent player: {currentplayer}")
            print(f"{currentplayer}'s hand: {initial_hands[currentplayer]}")
            topofpilecolor = topofpile.split()[0]
            topofpilenumber = topofpile.split()[1]
            playershand = initial_hands[currentplayer]

            has_playable_card = False

            for card in playershand:
                        card_color = card.split()[0]
                        card_number = card.split()[1]
                        if card_color == topofpilecolor or card_number == topofpilenumber:
                            has_playable_card = True
                            break

            if not has_playable_card:
                while not has_playable_card and deck:
                    newcard = deck.pop()
                    initial_hands[currentplayer].append(newcard)
                    print(f"No matching cards available in your hand. You picked a card from the deck. Your new card is {newcard}. ")
                    print(f"{currentplayer}'s hand: {initial_hands[currentplayer]}")

                    card_color = newcard.split()[0]
                    card_number = newcard.split()[1]

                    if card_color == topofpilecolor or card_number == topofpilenumber:
                        has_playable_card = True
                        break

            while cardvalidator == False:
                chosencard = input(f"{currentplayer}, choose a card to play: ").lower()
                if chosencard == 'exit':
                    print("Goodbye! Thanks for playing.")
                    exit()
                if chosencard == 'save game':
                    filename = input("Enter the filename to save: ")
                    save_game_state(filename, pile ,initial_hands) 
                    print("Game state saved successfully.")
                    exit()

                chosencardcolor = chosencard.split()[0] 
                chosencardnumber = chosencard.split()[1]                    
                try:
                    if chosencard not in initial_hands[currentplayer]:
                        raise ValueError("Invalid card. Please choose one of the cards in your hand.")
                except ValueError as ve:
                    print(f"Error: {ve}")
                if chosencardcolor == topofpilecolor:
                    cardvalidator = True
                if chosencardnumber == topofpilenumber:
                    cardvalidator = True
                
                if cardvalidator == True:
                    if chosencard in initial_hands[currentplayer]:
                        initial_hands[currentplayer].remove(chosencard)
                        topofpile = chosencard
                        print(f"{currentplayer} played {chosencard}")

                    if not initial_hands[currentplayer]:
                        print(f"{currentplayer} wins!")
                        break
        
                else:
                    print("Invalid card. Try again.")
                    print(f"Pile: {topofpile}")

            if not initial_hands[player1] or not initial_hands[player2]:
                print("Game over!")
                exit()

    


        
        else:
            print("Invalid input. Please try again.")
        ###
        

elif menu == 3:
    print("Goodbye! Hope you want to play soon!")

else:
    print("Error: That is not a valid option. Please choose 1, 2, or 3.")