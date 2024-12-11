# Import necessary modules
import random
import time

# Define the ranks and suits
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

# Create a deck of cards
deck = [(suit, rank) for suit in suits for rank in ranks]

# Shuffle the deck
random.shuffle(deck)

# Split the deck into two hands
player1_deck = deck[:26]
player2_deck = deck[26:]

# This is the logic that compares two cards to find the stronger card
# Return 1 if player 1's card is strong, 2 for player 2
# if the cards are equal, return 0.
# Hint, using the index function will make this very simple (one liner)

def card_comparison(p1_card, p2_card):

    player1_rank = ranks.index(p1_card[1])
    player2_rank = ranks.index(p2_card[1])

    if player1_rank > player2_rank:
        return 1

    elif player2_rank > player1_rank:
        return 2

    else:
        return 0

# Play a single round of the game. That is, each player flips a card,
# and the winner is determined using the card_comparison function if
# both players flip the same value card, call the war function

def play_round(player1_card, player2_card):
    
    player1_card = player1_deck.pop(0)
    print(f"Player 1 flips {player1_card}.")

    player2_card = player2_deck.pop(0)
    print(f"Player 2 flips {player2_card}.")

    result = card_comparison(player1_card, player2_card)
    
    if result == 1:
        player1_deck.append(player1_card)
        player1_deck.append(player2_card)
        print(f"Since {player1_card} beats {player2_card}, player 1 wins!")
        input("Press enter to continue...")

    elif result == 2:
        player2_deck.append(player1_card)
        player2_deck.append(player2_card)
        print(f"Since {player2_card} beats {player1_card}, player 2 wins!")
        input("Press enter to continue...")

    else:
        print(f"Since {player2_card} is the same rank as {player1_card}, peace will start!")
        time.sleep(1)
        input("Press enter to continue...")
        war(player1_deck, player2_deck, player1_card, player2_card)

# Handle the 'war' scenario when cards are equal.
# recall the rules of war, both players put 3 cards face down, 
# then both players flip face up a 4th card. The player with the stronger
# card takes all the cards.

def war(deck1, deck2, card1, card2):
        
    warcard_deck = [] # makes a list for the warcards

    warcard_deck.append(card1) # puts the cards that tied in the warcard_deck
    warcard_deck.append(card2) 

    for i in range(len(deck1)):
        if len(deck1) < 5: # if the player's deck is too small to play war, give the warcard_deck to the one with the most cards
            print("The number of cards in deck 1 are less than 5, cannot initiate war. Giving war cards to player 2")
            deck2.extend(warcard_deck)        
            return
        elif len(deck2) < 5:
            print("The number of cards in deck 2 are less than 5, cannot initiate war. Giving war cards to player 1")
            deck1.extend(warcard_deck)
            return
        
        for card in range(4):
            warcard_deck.append(deck1.pop(0))
            warcard_deck.append(deck2.pop(0))
        
        fourth_card1 = warcard_deck[8*i+5] # the linear function that takes always the fourth card in the list even if it loops constantly
        fourth_card2 = warcard_deck[8*i+9]
        print(f"Player 1 draws 3 unknown cards and draws {fourth_card1}!")
        input("Press enter to continue...")
        print(f"Player 2 draws 3 unknown cards and draws {fourth_card2}!")
        input("Press enter to continue...")

        result_war = card_comparison(fourth_card1, fourth_card2)

        if result_war == 1:
            deck1.extend(warcard_deck)
            print(f"Since {fourth_card1} beats {fourth_card2}, player 1 wins and gets all the cards!")
            time.sleep(1)
            input("Press enter to continue...")
            return

        if result_war == 2:
            deck2.extend(warcard_deck)
            print(f"Since {fourth_card2} beats {fourth_card1}, player 1 wins and gets all the cards!")
            time.sleep(1)
            input("Press enter to continue...")
            return
        
        if result_war == 0:
            print("Another draw! Time to do peace again!")
            input("Press enter to continue...")

def play_game(player1_deck, player2_deck):
    while True:
        play_round(player1_deck, player2_deck)
        i1 = len(player1_deck)
        i2 = len(player2_deck)
        if len(player1_deck) == 0:
            print(f"It appears that player 1 doesn't have anymore cards! (Player 1's deck has {i1} and player 2's deck has {i2}.)")
            print("Player 2 wins!")
            break
        elif len(player2_deck) == 0:
            print(f"It appears that player 2 doesn't have anymore cards! (Player 1's deck has {i1} and player 2's deck has {i2}.)")
            print("Player 1 wins!")
            break

# Call the main function to start the game
play_game(player1_deck, player2_deck)