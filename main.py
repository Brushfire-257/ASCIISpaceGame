#!/bin/env python3
# Contains code to start the game.

from player import Player, Camera
from gameloop import GameLoop
from world import WORLD

import sys
import termios # Does not work on windows. 

player = {}

def main():
    me = Player(1,1,'@','\x1b[32m', {'bean': {
        'name': 'Bean',
        'id': 1,
        'color': '\x1b[34m',
        'quantity': 1,
        'description': 'A test item.',
        'price': 3,
        'bought_price': 3,
    }})
    return me

# Hide user input to the terminal / thanks Mr.GPT (Not necessary for game function, but looks nicer.)
fd = sys.stdin.fileno()
original_attributes = termios.tcgetattr(fd)
new_attributes = termios.tcgetattr(fd)
new_attributes[3] = new_attributes[3] & ~termios.ECHO  # Turn off echo
termios.tcsetattr(fd, termios.TCSANOW, new_attributes)


player = main()
camera = Camera(1,1,10,6)

game = GameLoop(player, camera, WORLD)
game.run_game()

# User is Exiting game:
    
termios.tcsetattr(sys.stdin.fileno(), termios.TCSANOW, original_attributes)