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
                print('esc pressed.')
                self.exit_game()
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
        
    def exit_game(self):
        return

    def run_game(self):
        print('\033[?25l', end="") # Hides the Cursor!
    # Runs game loop here, continuously checking for keypresses
        while True:
            print("\r", end="")
            for i in range(self.length):
                print("#", end="")
            print("@ ", end="")

    def draw_map_layer(self, room_name, camera):
        room = WORLD.get(room_name, {})
        map_rows = room.get('map', [])
        colors = room.get('colors', {})

        rendered_area = []

        for y in range(camera.y - (camera.screen_height // 2), camera.y + (camera.screen_height // 2)):
            row = []
            for x in range(camera.x - (camera.screen_width // 2), camera.x + (camera.screen_width // 2)):
                if 0 <= y < len(map_rows) and 0 <= x < len(map_rows[y]):
                    char = map_rows[y][x]
                    color = colors.get(char, '\033[0m')  # Default color if character not found
                    row.append(f"{color}{char}{camera.reset_color}")
                else:
                    row.append(' ')  # Display empty space for areas outside the map
            rendered_area.append(''.join(row))
        return rendered_area
    
    def draw_player_layer(self, camera, player, rendered_area): # GPT made function (note: fix this later...)
        camera_player_x = player.x - camera.x + (camera.screen_width // 2)
        camera_player_y = player.y - camera.y + (camera.screen_height // 2)

        # Ensure the player is within the visible area
        if 0 <= camera_player_y < len(rendered_area) and 0 <= camera_player_x < len(rendered_area[camera_player_y]):
            rendered_area[camera_player_y] = (
                rendered_area[camera_player_y][:camera_player_x] + 
                f"{player.color}{player.char}{camera.reset_color}" + 
                rendered_area[camera_player_y][camera_player_x + 1:]
            )

        return rendered_area
    
    def get_visible_screen(self, camera, player, room_name):
        return self.draw_player_layer(Camera, Player, (self.draw_map_layer(room_name, Camera)))
    
    def player_movement(self, direction, camera, player):
        if(direction == 'up'):
            player.y += -1
            print(player.x)
            print(player.y)
            print(self.draw_map_layer('room1', self.camera))
            print(self.draw_player_layer(self.camera,self.player,self.draw_map_layer('room1',self.camera)))
            return
        elif(direction == 'down'):
            player.y += 1
            print(player.x)
            print(player.y)
            print(self.draw_map_layer('room1', self.camera))
            print(self.draw_player_layer(self.camera,self.player,self.draw_map_layer('room1',self.camera)))
            return
        elif(direction == 'right'):
            player.x += -1
            print(player.x)
            print(player.y)
            print(self.draw_map_layer('room1', self.camera))
            print(self.draw_player_layer(self.camera,self.player,self.draw_map_layer('room1',self.camera)))
            return
        elif(direction == 'left'):
            player.x += 1
            print(player.x)
            print(player.y)
            print(self.draw_map_layer('room1', self.camera))
            print(self.draw_player_layer(self.camera,self.player,self.draw_map_layer('room1',self.camera)))
            return
        
        return

if __name__ == "__main__":
    print("Run main.py you silly goose.")
