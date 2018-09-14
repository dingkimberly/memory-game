import numpy as np
import math
import os
import re
import time

#-------------------------------------------------------------------------------------------------
# Starting input

while True: 
    try:
        text = input("Enter the number of card pairs you'd like to play with (min 5, max 20): ")
        num_pairs = int(text)
    except ValueError:
        print("Please enter an integer.")
        continue
    else:
        if (num_pairs < 0):
            print("Please enter a positive integer.")
            continue
        elif (num_pairs < 5):
            print("That's less than 5. I'm just going to pretend that you typed 5.")
            num_pairs = 5
            break;
        elif (num_pairs > 20):
            print("That's more than 20. I'm just going to pretend that you typed 20.")
            num_pairs = 20
            break
        else:
            break
            
#-------------------------------------------------------------------------------------------------
# Card setup

np.random.seed(0) # REMOVE THIS LATER!!!!

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

pairs = np.random.choice(alphabet, size=num_pairs, replace=False)
cards = np.repeat(pairs, 2)
np.random.shuffle(cards)
num_cards = 2 * num_pairs

# I want to arrange the cards in a visually pleasing manner.
# So I'm going to make the arrangement as square as possible.

# Finds the first factor of n that's less than or equal to sqrt(n).
def find_squarelike_factor(n):
    top_bound = int(math.sqrt(n))
    if math.sqrt(n).is_integer():
        return top_bound
    else:
        for i in range(top_bound, 0, -1):
            if n % i == 0:
                return i
            
y_cards = find_squarelike_factor(num_cards)
x_cards = num_cards // y_cards

# The answer key. 
card_rows = np.reshape(cards, (y_cards, x_cards))
board = np.full((y_cards, x_cards), '?')

def format_board(board):
    os.system('clear')
    print()
    print("   ", end='')
    
    # print some letters
    for x in range(len(board[0])):
        print(chr(x + 97) + "  ", end='')
    print()
    
    # print numbers + board
    for i in range(len(board)):
        print(str(i+1) + "  ", end='')
        for j in range(len(board[0])):
            
            print(board[i][j] + "  ", end='')
        print()
    print()
    
#-------------------------------------------------------------------------------------------------
# Gameplay

format_board(board)

moves = 3 * num_pairs
num_guessed = 0
    
while (moves > 0 and num_guessed < num_pairs): 
    print("You have %d moves remaining." % moves)
    
    while True: 
        text = input("Enter the coordinates of two cards separated by a space (such as \"a2 b1\"): ")
        text = text.lower().strip()

        pattern = re.compile("^[a-z][0-9](\s)+[a-z][0-9]$")
        if not pattern.match(text):
            print("That doesn't seem to be a valid pair of coordinates. Try again.")
            continue
        else:
            coords = text.split()
            if (coords[0] == coords[1]):
                print("For some reason, you just picked the same card twice. Try again.")
                continue

            x1 = ord(coords[0][0]) - 97
            y1 = int(coords[0][1]) - 1
            x2 = ord(coords[1][0]) - 97
            y2 = int(coords[1][1]) - 1

            if ((not x1 in range(0, x_cards)) or (not y1 in range(0, y_cards)) or
               (not x2 in range(0, x_cards)) or (not y2 in range(0, y_cards))):
                print("That doesn't seem to be a valid pair of coordinates. Try again.")
                continue
            
            if (board[y1][x1] != '?' or board[y2][x2] != '?'):
                print("At least one of those cards has been flipped already! What are you doing? Try again.")
                continue
            
            # finally we have some valid coordinates
            board[y1][x1] = card_rows[y1][x1]
            board[y2][x2] = card_rows[y2][x2]
            
            format_board(board)
            
            if (board[y1][x1] == board[y2][x2]):
                print("It's a match!")
                num_guessed += 1
                time.sleep(1)
                format_board(board)
            else:
                print("Oh no, it's not a match.")
                board[y1][x1] = '?'
                board[y2][x2] = '?'
                time.sleep(1)
                format_board(board)
                
            moves -= 1
            
            break
    continue
    
if (moves == 0):
    print("Oh no, you lost the game.")
else:
    print("Hooray, you won the game.")
    
print()