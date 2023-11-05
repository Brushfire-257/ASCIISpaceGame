# Contains the main game loop. The base for everything else.

from pynput import keyboard
import cmd
from player import Player, Camera
import world
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

class GameLoop():
    def __init__(self, me, rooms):
        super().__init__()
        self.me = me
        self.rooms = rooms
        self.length = 0
        keyboard.Listener(on_press=self.on_key_press, on_release=lambda _: None).start()

    def do_move(self, direction, length):
        # Handle the move command
        if (direction == 'right' and length > 0):
            self.length = self.length - 1
        elif (direction == 'left'):
            self.length = self.length + 1
        pass

    def on_key_press(self, key):
        # Special key handling
        if not hasattr(key, "char"):
            if key == keyboard.Key.esc:
                # something
                print('esc pressed.')
            return
        # Regular key handling
        if key.char == "a":
            # something
            self.do_move('right', self.length)
        elif key.char == "d":
            self.do_move('left', self.length)

    def run_game(self):
        print('\033[?25l', end="") # Hides the Cursor!
    # Runs game loop here, continuously checking for keypresses
        while True:
            print("\r", end="")
            for i in range(self.length):
                print("#", end="")
            print("@ ", end="")


if __name__ == "__main__":
    print("Run main.py you silly goose.")
