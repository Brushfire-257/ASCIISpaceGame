# Contains code to start the game.

from player import Player, Camera
from gameloop import GameLoop
from world import WORLD

player = {}

def main():
    me = Player(1,1,'@','\033[34m')
    return me

player = main()

game = GameLoop(player, WORLD)
game.cmdloop()