# Contains the main game loop. The base for everything else.

from pynput import keyboard
import cmd
from player import Player, Camera
from world import *
import os

def clear():
    # os.system('cls' if os.name=='nt' else 'clear')
    print("\033[%d;%dH" % (0, 0), end="")


class GameLoop():
    def __init__(self, player, camera, rooms):
        super().__init__()
        self.player = player
        self.camera = camera
        self.rooms = rooms
        self.exit_game = 0
        self.gui_open = 0
        self.player_inventory_gui_open = 0
        self.chest_inventory_gui_open = 0
        keyboard.Listener(on_press=self.on_key_press, on_release=self.on_key_release).start()
    
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
        if key.char == "a" and not self.gui_open:
            self.player_movement('right')
        elif key.char == "d" and not self.gui_open:
            self.player_movement('left')
        elif key.char == 'w' and not self.gui_open:
            self.player_movement('up')
        elif key.char == 's' and not self.gui_open:
            self.player_movement('down')
        elif key.char == 'i':
            if self.gui_open == 0 and not self.player_inventory_gui_open:
                self.gui_open = 1
                self.player_inventory_gui_open = 1
            else:
                self.gui_open = 0
                self.player_inventory_gui_open = 0
        elif key.char == 'p':
            if self.gui_open == 0 and not self.chest_inventory_gui_open:
                self.gui_open = 1
                self.chest_inventory_gui_open = 1
            else:
                self.gui_open = 0
                self.chest_inventory_gui_open = 0

    def run_game(self):
        print('\x1b[?25l', end="") # Hides the Cursor!
    # Runs game loop here, continuously checking for keypresses
        while True:
            if self.exit_game == 1:
                os.system('cls' if os.name=='nt' else 'clear')
                break
            self.print_screen()

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
                    color = colors.get(char, '\x1b[0m')  # Default color if character not found
                    row.append(f"{color}{char}{self.camera.reset_color}")
                else:
                    row.append('0')  # Display character for areas outside the map
            rendered_area.append(row)
        return rendered_area
    
    def draw_player_layer(self, rendered_area): # No longer GPT yippie.
        camera_player_x = self.player.x - self.camera.x + (self.camera.screen_width // 2)
        camera_player_y = self.player.y - self.camera.y + (self.camera.screen_height // 2)

        # Ensure the player is within the visible area
        if 0 <= camera_player_y < len(rendered_area) and 0 <= camera_player_x < len(rendered_area[camera_player_y]):
            rendered_area[camera_player_y][camera_player_x] = f"{self.player.color}{self.player.char}{self.camera.reset_color}"

        return rendered_area
    
    def get_visible_screen(self, room_name):
        return self.draw_player_layer(self.draw_map_layer(room_name))
    
    def camera_controller(self):
        camera_player_x = self.player.x - self.camera.x + (self.camera.screen_width // 2)
        camera_player_y = self.player.y - self.camera.y + (self.camera.screen_height // 2)

        # debug
        #print(f"{camera_player_x=} {self.player.x=} {self.camera.x=}")
        #print(f"{camera_player_y=} {self.player.y=} {self.camera.y=}")

        if camera_player_x < (self.camera.screen_width // 2):
            self.camera.x += -1
        elif camera_player_x > (self.camera.screen_width // 2):
            self.camera.x += 1
        if camera_player_y < (self.camera.screen_height // 2):
            self.camera.y += -1
        elif camera_player_y > (self.camera.screen_height // 2):
            self.camera.y += 1

        return

    def overwrite_render(self, rendered_area, with_what):
        overwrite = GUI.get(with_what, {})
        overwrite_rows = overwrite.get('gui', [])
        colors = overwrite.get('colors', {})

        new_rendered_area = []

        for y in range(self.camera.screen_height):
            row = []
            for x in range(self.camera.screen_width):
                if 0 <= y < len(overwrite_rows) and 0 <= x < len(overwrite_rows[y]):
                    char = overwrite_rows[y][x]
                    color = colors.get(char, '\x1b[0m')  # Default color if character not found
                    if char == ' ':
                        row.append(rendered_area[y][x])
                    else:
                        row.append(f"{color}{char}{self.camera.reset_color}")
            #rendered_area.append(row)
            new_rendered_area.append(row)
        return new_rendered_area

    def print_screen(self):
        clear()
        if self.gui_open == 0:
            for row in self.overwrite_render(self.draw_player_layer(self.draw_map_layer("room1")), 'gui1'):
            #for row in self.draw_player_layer(self.draw_map_layer("room1")):
                print("".join(row))
        clear()
        # If there is a gui open, check what it is and render it.
        if self.player_inventory_gui_open == 1:
            for row in self.player_inventory_renderer():
            #for row in self.draw_player_layer(self.draw_map_layer("room1")):
                print("".join(row))
        if self.chest_inventory_gui_open == 1:
            for row in self.chest_inventory_renderer():
                print("".join(row))
        return

    def render_gui_base(self, gui_name): # Similar to the map render function, just without camera movement.
        gui_info = GUI.get(gui_name, {})
        gui = gui_info.get('gui', [])
        gui_colors = gui_info.get('colors', {})

        rendered_area = []

        for y in range(self.camera.screen_height):
            row = []
            for x in range(self.camera.screen_width):
                if 0 <= y < len(gui) and 0 <= x < len(gui[y]):
                    char = gui[y][x]
                    color = gui_colors.get(char, '\x1b[0m')  # Default color if character not found
                    row.append(f"{color}{char}{self.camera.reset_color}")
                else:
                    row.append(' ')  # Display empty space for areas outside the gui
            rendered_area.append(row)
        return rendered_area
    
    def remove_dictionary(self, main_dictionary, id): # Removes a dictionary from a dictionary
        new_dictionary = [i for i in main_dictionary if not (i['id'] == id)]
        return new_dictionary
    
    def overwrite_gui(self, input_gui, x, y, overwrite_string):
        # Enture coordinates are within the gui
        if 0 <= y < len(input_gui) and 0 <= x < len(input_gui[y]):
            # Check that the string can fit in the area
            if x + len(overwrite_string) <= len(input_gui[y]):
                input_gui[y][x:x + len(overwrite_string)] = list(overwrite_string)
        return input_gui
    
    def player_inventory_renderer(self):
        gui_base = self.render_gui_base('player_inventory')

        i = 0
        for items in self.player.inventory:
            gui_base = self.overwrite_gui(gui_base, 1, i+1, self.player.inventory[items]['name'])
            i += 1
        return gui_base
    
    def chest_inventory_renderer(self):
        gui_base = self.render_gui_base('chest_gui')

        i = 0
        for items in self.player.inventory:
            gui_base = self.overwrite_gui(gui_base, 20, i+1, self.player.inventory[items]['name'])
            i += 1
        i = 0
        return gui_base

    def put_item_in_chest(self, item, chest_x, chest_y):
        item_in_question = self.player.inventory.get(item)
        if item_in_question:
            if (chest_x, chest_y) in self.rooms[self.player.room]['chests']:
                chest = self.rooms[self.player.room]['chests'][(chest_x, chest_y)]
                if item in chest['items']:
                    chest['items'][item]['quantity'] += item['quantity']
                else:
                    chest['items'][item] = item.copy()
                del self.player.inventory[item]
        return
    
    def item_from_chest_to_player(self, item, chest_x, chest_y):
        if (chest_x, chest_y) in self.rooms[self.player.room]['chests']:
            item_in_quesion = self.rooms[self.player.room]['chests'][(chest_x, chest_y)][item]
            if item_in_quesion:
                if item in self.player.inventory:
                    self.player.inventory['quantity'] += self.rooms[self.player.room]['chests'][(chest_x, chest_y)][item]['quantity']
                else:
                    self.player.inventory.append(self.rooms[self.player.room]['chests'][(chest_x, chest_y)][item])
                self.rooms[self.player.room]['chests'][(chest_x, chest_y)].pop(item)
        return
    
    def player_movement(self, direction):
        if(direction == 'up'):
            move_by = (0, -1)
        elif(direction == 'down'):
            move_by = (0, 1)
        elif(direction == 'right'):
            move_by = (1, 0)
        elif(direction == 'left'):
            move_by = (-1, 0)

        #init but butter
        room = WORLD.get("room1", {})
        map = room.get('map', [])
        collisions = room.get('collisions', [])

        # check for collisions
        char = map[self.player.y + move_by[1]][self.player.x - move_by[0]]
        if collisions.get(char) == 'player':
            return

        # debug
        #print(map[player.y + move_by[1]][player.x - move_by[0]])

        # if no collisions than:
        self.player.x -= move_by[0]
        self.player.y += move_by[1]

        self.camera_controller()
        
        return

if __name__ == "__main__":
    print("Run main.py you silly goose.")
