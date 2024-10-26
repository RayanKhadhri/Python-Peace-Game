import random 
# Defining the ranks and suits

ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A") 
suits = ("Clubs", "Diamonds", "Hearts", "Spades")

# Creating the deck  

deck = [(rank,suit) for rank in ranks for suit in suits]

# Shuffling the deck

random.shuffle(deck) 

# Splitting the deck into two Hands

half_of_deck = len(deck) // 2
p1_hand = deck[:half_of_deck]
p2_hand = deck[half_of_deck:] 

# Comparing Cards function
# If p1 card stronger return 1 if p2 stronger return 2
#If tie return 0

def card_comparison(p1_card, p2_card):
    p1_rank_index = ranks.index(p1_card[0])
    p2_rank_index = ranks.index(p2_card[0])
    if p2_rank_index > p1_rank_index:
        return 2
    elif p1_rank_index > p2_rank_index:
        return 1
    else:
        return 0

# Playing a single round of the game

def play_round(p1_hand, p2_hand):
    if not p1_hand or not p2_hand:
        return
    p1_card = p1_hand.pop(0)
    p2_card = p2_hand.pop(0)
    print(f"Player 1 has played: {p1_card}! Player 2 has played: {p2_card}! ")

# This checks the outcome to see what will happen
# Either one of the Players will win or if tied it will go to peace!  
# If somebody wins both cards will go to the bottom of their deck using extend() 

    outcome = card_comparison(p1_card, p2_card)
    if outcome == 1:
        p1_hand.extend([p1_card, p2_card])
        print(" Player 1 has the strongest card and has won this round!")
    elif outcome == 2:
        p2_hand.extend([p1_card, p2_card]) 
        print(" Player 2 has the strongest card and has won this round!")
    else:
        print(" We have a tie, it is time for peace!")
        peace(p1_hand, p2_hand, [p1_card], [p2_card])

# This makes it so everything doesn't run really fast

    input("Press Enter to continue...")

# This is what happens when we have a tie and must make peace
 
def peace(p1_hand, p2_hand, p1_cards, p2_cards):

# Check if they have enough card to make peace 
# Need at least 4 cards to do so
# Declare a winner if there is a player with less 4 cards
# Winning player claims other players cards and loser has their hand cleared

    if len(p1_hand) < 4 or len(p2_hand) < 4:
        if len(p1_hand) < 4:
            print("Player 2 has won because Player 1 was not ready to make peace!")
            p2_hand.extend(p1_hand)
            p1_hand.clear() 
        else:
            print("Player 1 has won because Player 2 was not ready to make peace!")
            p1_hand.extend(p2_hand)
            p2_hand.clear()
        return
    
# Loop that runs 3 times for the cards that need to be played face down

    for _ in range(3):
        p1_cards.append(p1_hand.pop(0))
        p2_cards.append(p1_hand.pop(0))
    p1_card = p1_hand.pop(0)
    p2_card = p2_hand.pop(0)
    print(f"Player 1 has played: {p1_card}! Player 2 has played: {p2_card}! ")

# Check who makes peace

    outcome = card_comparison(p1_card, p2_card)
    if outcome == 1:
        p1_hand.extend(p1_cards + p2_cards + [p1_card, p2_card])
        print(" Player 1 has made peace!")
    elif outcome == 2:
        p2_hand.extend(p1_cards + p2_cards + [p1_card, p2_card]) 
        print(" Player 2 has made peace!")

# Makes it so peace will continue if it is still tie

    else:
        print(" We have a tie, we have to make more peace!")
        peace(p1_hand, p2_hand, p1_cards + [p1_card], p2_cards + [p2_card])

# The function that runs the game
# While loop is used to continue game as long as both players have cards

def play_game(): 
    while p1_hand and p2_hand:
        play_round(p1_hand, p2_hand)

# This looks at the length of both
# Since it continues as long as somebody has a hand it means somebody does not have a hand if we"ve reached here
# Whoever has a length longer than the other wins the game

    if len(p1_hand) > len(p2_hand):
        print("Player 1 has won, congrats!")
    elif len(p2_hand) > len(p1_hand):
        print("Player 2 has won, congrats!")

# This calls the function to paly the game

play_game() 

