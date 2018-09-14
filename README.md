# Memory Game

This is a simple memory game programmed in Python.

## Running the Game

Download memory.py and run "./memory.py" from its location. You can use "python memory.py" as well.

## Rules

The game is pretty straightforward. Pick the number of card pairs you'd like to play with.
Then select the coordinates of pairs of cards you'd like to guess each turn. 
You have a limited number of turns. If you guess incorrectly, you'll get to see what the cards are for a second
before the board resets. If you guess right, the cards stay flipped.

## Design choices

This game is contained in a single file, and uses some pretty long while loops
I decided to keep this format for simplicity. 
I could have put some lines of code into separate functions, 
but I feel like the current code has a logical and chronological flow and is easy to read.

The bulk of information is stored in 2D arrays, which I thought made the most sense since Memory consists of a grid of cards. 
I used numpy to manipulate these arrays, since numpy is really good at that. I also used a few of Python's built-in libraries for various purposes.

## Additional notes

I wrote this game in Python because I really like Python.
