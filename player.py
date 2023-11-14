# Will contain a class for all the player atributes. Changing to contain more classes...

class Player:
    def __init__(self, x, y, char, color, inventory = {}):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.inventory = inventory

class Camera:
    def __init__(self, x, y, screen_width, screen_height):
        self.x = x
        self.y = y
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.reset_color = "\x1b[0;30m" # White ANSI color code

class Chests:
    def __init__(self, character, color, world_data = {}):
        self.character = character
        self.color = color
        self.world_data = world_data

    def add_item(self, room, chest, item): # Fairly obvious
        if item.Get('name') in self.chests[room][chest]:
            self.world_data[room]['chest'][chest]['items'][item.Get('name')] += item.Get('quantity')
        else:
            self.world_data[room]['chest'][chest]['items'][item.Get('name')] = item.Get('quantity')

    def remove_item(self, room, chest, item):
        if item.Get('name') in self.chests[room][chest]['items']:
            if self.world_data[room]['chest'][chest]['items'][item.Get('name')] >= item.Get('quantity'):
                self.world_data[room]['chest'][chest]['items'][item.Get('name')] -= item.Get('quantity')
                if self.world_data[room]['chest'][chest]['items'][item.Get('name')] == 0:
                    del self.world_data[room]['chest'][chest]['items'][item.Get('name')]