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
        #time.sleep(4)
        input("Press enter to continue...")
        war(player1_deck, player2_deck, player1_card, player2_card)

# Handle the 'war' scenario when cards are equal.
# recall the rules of war, both players put 3 cards face down, 
# then both players flip face up a 4th card. The player with the stronger
# card takes all the cards.

def war(deck1, deck2, card1, card2):
    if len(deck1) < 5 or len(deck2) < 5:
        print("error 101: the number of cards in either decks are less than 5, cannot initiate war")
        player2_deck.append(card1)
        player2_deck.append(card2)

    else:
        player1_card1, player1_card2, player1_card3, player1_card4 = [deck1.pop(0) for card in range(4)]
        print(f"Player 1 draws 3 unknown cards and draws {player1_card4}!")
        input("Press enter to continue...")

        player2_card1, player2_card2, player2_card3, player2_card4 = [deck2.pop(0) for card in range(4)]
        print(f"Player 2 draws 3 unknown cards and draws {player2_card4}!")
        input("Press enter to continue...")

        result_war = card_comparison(player1_card4, player2_card4)

        if result_war == 1:
            deck1.extend([card1, card2, player1_card1, player1_card2, player1_card3, player1_card4, player2_card1, player2_card2, player2_card3, player2_card4])
            print(f"Since {player1_card4} beats {player2_card4}, player 1 wins and gets all the cards!")
            #time.sleep(4)
            input("Press enter to continue...")
        if result_war == 2:
            deck2.extend([card1, card2, player2_card1, player2_card2, player2_card3, player2_card4, player1_card1, player1_card2, player1_card3, player1_card4])
            print(f"Since {player2_card4} beats {player1_card4}, player 2 wins and gets all the cards!")
            #time.sleep(4)
            input("Press enter to continue...")
        if result_war == 0:
            print("Another draw! Time to do peace again!")
            input("Press enter to continue...")
            unassigned_cards = []
            unassigned_cards.extend([card1, card2, player2_card1, player2_card2, player2_card3, player2_card4, player1_card1, player1_card2, player1_card3, player1_card4])

            if len(deck1) < 5 or len(deck2) < 5:
                print("Error 404")

            else:
                player1_card1, player1_card2, player1_card3, player1_card4 = [deck1.pop(0) for card in range(4)]
                print(f"Player 1 draws 3 unknown cards and draws {player1_card4}!")
                input("Press enter to continue...")

                player2_card1, player2_card2, player2_card3, player2_card4 = [deck2.pop(0) for card in range(4)]
                print(f"Player 2 draws 3 unknown cards and draws {player2_card4}!")
                input("Press enter to continue...")

                result_war = card_comparison(player1_card4, player2_card4)
    
                if result_war == 1:
                    deck1.extend([unassigned_cards, player1_card1, player1_card2, player1_card3, player1_card4, player2_card1, player2_card2, player2_card3, player2_card4])
                    print(f"Since {player1_card4} beats {player2_card4}, player 1 wins and gets all the cards!")
                    #time.sleep(4)
                    print(len(deck1))
                    input("Press enter to continue...")

                if result_war == 2:
                    deck2.extend([unassigned_cards, player2_card1, player2_card2, player2_card3, player2_card4, player1_card1, player1_card2, player1_card3, player1_card4])
                    print(f"Since {player2_card4} beats {player1_card4}, player 1 wins and gets all the cards!")
                    #time.sleep(4)
                    print(len(deck2))
                    input("Press enter to continue...")

                if result_war == 0:
                    print("F the peace! Back to war!")
                    input("Press enter to continue...")
                    print("ERROR")

def play_game(player1_deck, player2_deck):
    for i in range(1,1000):
        play_round(player1_deck, player2_deck)
        print(len(player1_deck))
        print(len(player2_deck))
        if len(player1_deck) == 0:
            print("It appears that player 1 doesn't have anymore cards!")
            print("Player 2 wins!")
            break
        elif len(player2_deck) == 0:
            print("It appears that player 2 doesn't have anymore cards!")
            print("Player 1 wins!")
            break

# Call the main function to start the game
play_game(player1_deck, player2_deck)

