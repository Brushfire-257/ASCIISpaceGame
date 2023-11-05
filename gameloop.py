# Contains the main game loop. The base for everything else.

from pynput import keyboard
import cmd
from player import Player, Camera
import world
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

length = 0

class GameLoop(cmd.Cmd):
    def __init__(self, me, rooms):
        super().__init__()
        self.me = me
        self.rooms = rooms


    def do_move(self, direction, length):
        # Handle the move command
        if (direction == 'right' and length > 0):
            length = length - 1
        elif (direction == 'left'):
            length = length + 1
        pass

    def on_key_press(self, event):
        key = event.name
        if key == "a":
            self.do_move('left', length)
        elif key == "d":
            self.do_move('right', length)

    def run_game(self):
        keyboard.on_press(self.on_key_press)

        # Runs game loop here, continuously checking for keypresses

        for i in range(length):
            print("#", end="")
        print("@")
        clear()

        keyboard.wait("esc")  # Use a specific key to exit the game?

if __name__ == "__main__":
    print("Run main.py you silly goose.")
