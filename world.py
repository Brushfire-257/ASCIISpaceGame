# Will Contain the entire map for the game in a dictionary.

WORLD = {
    'room1': {
        'map': [
            "#####################",
            "# - - - - - - - - - #",
            "# - - - -.-.- - - - #",
            "# - - - -.-.- - - - #",
            "# - - - - - - - - - #",
            "#####################",
        ],
        'colors': {
            '.': '\x1b[37m',  # Grey color for dots
            '_': '\x1b[34m',  # Blue color for underscores
            '#': '\x1b[33m',  # Green color for walls
            # You can add more mappings for different characters here
        },
        'colisions': {
            '#': 'player',  # Colision layer
            # Other collisions here:
        }
    },
    'room2': {
        'map': [
            "#####",
            "#_#_#",
            "#_#_#",
            "#####",
        ],
        'colors': {
            '#': '\x1b[32m',  # Green color for walls
            '_': '\x1b[34m',  # Blue color for underscores
            # You can add more mappings for different characters here
        }
    },
    # Add more rooms and their map data here
}

GUI = {
    'gui1': {
        'gui': [
            "╔════════╗",
            "║        ║",
            "║        ║",
            "║        ║",
            "║        ║",
            "╚════════╝",
        ],
        'colors': {
            '╚': '\x1b[37m',  # Blue color for gui
            '═': '\x1b[34m',
            '║': '\x1b[34m',
            '╝': '\x1b[34m',
            '╗': '\x1b[34m',
            '╔': '\x1b[34m',
            # You can add more mappings for different characters here
        }
    }
}