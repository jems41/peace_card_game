# Import necessary modules
import random

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

def card_comparison(p1_card, p2_card):
    
    player1_rank = ranks.index(p1_card[1])
    player2_rank = ranks.index(p2_card[1]) 
    
    if player1_rank > player2_rank:
        return 1
    
    elif player2_rank > player1_rank:
        return 2
    
    else:
        return 0 

def play_round(player1_hand, player2_hand):
    """Play a single round of the game.
		That is, each player flips a card, and the winner is determined using the card_comparison function
		if both players flip the same value card, call the war function
	"""
    player1_card = player1_deck.pop(0)
    player2_card = player2_deck.pop(0)
    
    result = card_comparison(player1_card, player2_card)
    
    if len(player1_deck) == 0 or len(player2_deck) == 0:
        return 3
 
def war(player1_hand, player2_hand):
    """Handle the 'war' scenario when cards are equal.
		recall the rules of war, both players put 3 cards face down, 
		then both players flip face up a 4th card. The player with the stronger
		card takes all the cards.		
	"""
    # Your code here

def play_game():
    """Main function to run the game."""
    for i in range(1,26):
        play_round(player1_deck, player2_deck)
        if 

# Call the main function to start the game
play_game()
