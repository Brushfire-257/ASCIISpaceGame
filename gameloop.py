# Contains the main game loop. The base for everything else.

from pynput import keyboard
import cmd
from player import Player, Camera
from world import WORLD
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

class GameLoop():
    def __init__(self, player, camera, rooms):
        super().__init__()
        self.player = player
        self.camera = camera
        self.rooms = rooms
        self.length = 0
        self.exit_game = 0
        keyboard.Listener(on_press=self.on_key_press, on_release=self.on_key_release).start()

    def do_move(self, direction, length):
        # Handle the move command
        if (direction == 'right' and length > 0):
            self.length = self.length - 1
        elif (direction == 'left'):
            self.length = self.length + 1
        pass
    
    def on_key_release(self, key):
        #print(key.char + " key released!")
        return

    def on_key_press(self, key):
        # Special key handling
        if not hasattr(key, "char"):
            if key == keyboard.Key.esc:
                print('Exiting...')
                self.exit_game = 1
            return
        # Regular key handling
        if key.char == "a":
            self.do_move('right', self.length)
            self.player_movement('right', Camera, self.player)
        elif key.char == "d":
            self.do_move('left', self.length)
            self.player_movement('left', Camera, self.player)
        elif key.char == 'w':
            self.player_movement('up', Camera, self.player)
        elif key.char == 's':
            self.player_movement('down', Camera, self.player)

    def run_game(self):
        print('\033[?25l', end="") # Hides the Cursor!
    # Runs game loop here, continuously checking for keypresses
        while True:
            if self.exit_game == 1:
                break
            print("\r", end="")
            for i in range(self.length):
                print("#", end="")
            print("@ ", end="")

    def draw_map_layer(self, room_name):
        room = WORLD.get(room_name, {})
        map_rows = room.get('map', [])
        colors = room.get('colors', {})

        rendered_area = []

        for y in range(self.camera.y - (self.camera.screen_height // 2), self.camera.y + (self.camera.screen_height // 2)):
            row = []
            for x in range(self.camera.x - (self.camera.screen_width // 2), self.camera.x + (self.camera.screen_width // 2)):
                if 0 <= y < len(map_rows) and 0 <= x < len(map_rows[y]):
                    char = map_rows[y][x]
                    color = colors.get(char, '\033[0m')  # Default color if character not found
                    row.append(f"{color}{char}{self.camera.reset_color}")
                else:
                    row.append(' ')  # Display empty space for areas outside the map
            rendered_area.append(''.join(row))
        return rendered_area
    
    def draw_player_layer(self, rendered_area): # GPT made function (note: fix this later...)
        camera_player_x = self.player.x - self.camera.x + (self.camera.screen_width // 2)
        camera_player_y = self.player.y - self.camera.y + (self.camera.screen_height // 2)

        # Ensure the player is within the visible area
        if 0 <= camera_player_y < len(rendered_area) and 0 <= camera_player_x < len(rendered_area[camera_player_y]):
            rendered_area[camera_player_y] = (
                rendered_area[camera_player_y][:camera_player_x] + 
                f"{self.player.color}{self.player.char}{self.camera.reset_color}" + 
                rendered_area[camera_player_y][camera_player_x + 1:]
            )

        return rendered_area
    
    def get_visible_screen(self, room_name):
        return self.draw_player_layer(self.draw_map_layer(room_name))
    
    def camera_controller(self):
        camera_player_x = self.player.x - self.camera.x + (self.camera.screen_width // 2)
        camera_player_y = self.player.y - self.camera.y + (self.camera.screen_height // 2)

        if camera_player_x < self.camera.screen_width // 2:
            self.camera.x += -1
        elif camera_player_x > self.camera.screen_width // 2:
            self.camera.x += 1
        if camera_player_y < self.camera.screen_height // 2:
            self.camera.y += -1
        elif camera_player_y > self.camera.screen_height // 2:
            self.camera.y += 1
        return
    
    def player_movement(self, direction, camera, player):
        if(direction == 'up'):
            player.y += -1
            self.camera_controller()
            print(player.x)
            print(player.y)
            print(self.draw_map_layer('room1'))
            print(self.draw_player_layer(self.draw_map_layer('room1')))
            return
        elif(direction == 'down'):
            player.y += 1
            self.camera_controller()
            print(player.x)
            print(player.y)
            print(self.draw_map_layer('room1'))
            print(self.draw_player_layer(self.draw_map_layer('room1')))
            return
        elif(direction == 'right'):
            player.x += -1
            self.camera_controller()
            print(player.x)
            print(player.y)
            print(self.draw_map_layer('room1'))
            print(self.draw_player_layer(self.draw_map_layer('room1')))
            return
        elif(direction == 'left'):
            player.x += 1
            self.camera_controller()
            print(player.x)
            print(player.y)
            print(self.draw_map_layer('room1'))
            print(self.draw_player_layer(self.draw_map_layer('room1')))
            return
        
        return

if __name__ == "__main__":
    print("Run main.py you silly goose.")
