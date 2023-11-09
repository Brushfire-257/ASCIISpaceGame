#!/bin/env python3
# Contains code to start the game.

from player import Player, Camera
from gameloop import GameLoop
from world import WORLD

player = {}

def main():
    me = Player(1,1,'@','\x1b[33m')
    return me

player = main()
camera = Camera(1,1,10,6)

game = GameLoop(player, camera, WORLD)
game.run_game()