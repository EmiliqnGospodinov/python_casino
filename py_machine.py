
#OS functions
#import os
#show files in current folder
#print(os.listdir())
#make dirs in folder
#os.makedirs('folder_name/folder_name2/...')


import random
from wallet_functions import show_wallet_balance as show_balance, withdraw_wallet as withdraw, deposit_wallet as deposit, credits_balance as credits
import blackjack as bjack


#variables
shuffable_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J','Q','K','A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J','Q','K','A'] #ints and strings
full_deck = {2, 3, 4, 5, 6, 7, 8, 9, 10, 'J','Q','K','A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J','Q','K','A'} # Set - no dublicates
full_deck2 = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J','Q','K','A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J','Q','K','A') # Tuple - not edittable

def logged_mssg(username):
    """Display welcome message"""
    return f'Hello, {username}! You have {credits} credits.'


def draw_hand(i):
    """draw hand with 'i' cards"""
    return random.sample(shuffable_deck, k = i)

#review decks
def show_decks(*deck):
    print(f'Deck before shuffle {full_deck2}')
    print(f'Deck contains this {deck}')

#Login page w/o database
print('Welcome to the casino! Please login with your username: ')

users = ['Strahil','Dimitur','Petur','Todor','Georgi']
user_name = random.choice(users)#, k = 1)
print(logged_mssg(user_name))
#balance commands
#show_balance()
#withdraw(100)
#show_balance()
#deposit(1000)
#show_balance()

#add Joker into deck after all other
#joker = 'Joker'
#shuffable_deck.insert(len(shuffable_deck), joker)
#print(deck)

#show if Joker is in the deck
#print('Joker' in deck)


#check what cards the deck has //////////////////////////////////////////////////////////////

#hand with x random cards
#print(f'{draw_hand(5)}')

#min_bet = 10


#print(round(3.753, 1))

#Random hands and deck

#shuffle deck
random.shuffle(shuffable_deck)

#blackjack with popped values

popped_card = shuffable_deck.pop(random.randint(0, len(shuffable_deck) - 1))
points = popped_card # FIX DRAW VALUES
#print(f'You drew {popped_card}, you now have {points} points.')
#show_decks(*shuffable_deck)


