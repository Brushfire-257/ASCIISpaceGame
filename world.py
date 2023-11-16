# Contains the entire map for the game in a dictionary. Also contains the GUI elements for the game.

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
            # More mappings for different characters here:
        },
        'collisions': {
            '#': 'player',  # Collision layer
            # Other collisions here:
        },
        'chests': {
            (5,4): {
                'items': {'butter': {
        'name': 'Butter',
        'color': '\x1b[33m',
        'quantity': 1,
        'description': 'Another test item.',
        'price': 4,
        'bought_price': 4,},
            }
            },
            # Another chest here:
        },
    },
    'room2': {
        'map': [
            "#####",
            "#_#_#",
            "#___#",
            "#####",
        ],
        'colors': {
            '#': '\x1b[32m',  # Green color for walls
            '_': '\x1b[34m',  # Blue color for underscores
            # You can add more mappings for different characters here
        },
        'colisions': {
            '#': 'player',  # Colision layer
            # Other collisions here:
        }
    },
    # Add more rooms and their map data here:
}

GUI = {
    'gui1': {
        'gui': [
            "╔═══════════════════════════════════╗",
            "║                                   ║",
            "║                                   ║",
            "║                                   ║",
            "║                                   ║",
            "║                                   ║",
            "║                                   ║",
            "║                                   ║",
            "║                                   ║",
            "║                                   ║",
            "║                                   ║",
            "╚═══════════════════════════════════╝",
        ],
        'colors': {
            '╚': '\x1b[34m',  # Blue color for gui
            '═': '\x1b[34m',
            '║': '\x1b[34m',
            '╝': '\x1b[34m',
            '╗': '\x1b[34m',
            '╔': '\x1b[34m',
            # More mappings for different characters here
        }
    },
    'player_inventory': {
        'gui': [
            "╔═PLAYER═INVENTORY══════════════════╗",
            "║                                   ║",
            "║                                   ║",
            "║                                   ║",
            "║                                   ║",
            "║                                   ║",
            "║                                   ║",
            "║                                   ║",
            "║                                   ║",
            "║                                   ║",
            "║                                   ║",
            "╚═══════════════════════════════════╝",
        ],
        'colors': {
            '╚': '\x1b[37m',  # Blue color for gui
            '═': '\x1b[37m',
            '║': '\x1b[37m',
            '╝': '\x1b[37m',
            '╗': '\x1b[37m',
            '╔': '\x1b[37m',
            # More mappings for different characters here
        }
    },
    'chest_gui': {
        'gui': [
            "╔═CHEST════════════╦═YOU════════════╗",
            "║                  ║                ║",
            "║                  ║                ║",
            "║                  ║                ║",
            "║                  ║                ║",
            "║                  ║                ║",
            "║                  ║                ║",
            "║                  ║                ║",
            "║                  ║                ║",
            "║                  ║                ║",
            "║                  ║                ║",
            "╚══════════════════╩════════════════╝",
        ],
        'colors': {
            '╚': '\x1b[37m',  # Blue color for gui
            '═': '\x1b[37m',
            '║': '\x1b[37m',
            '╝': '\x1b[37m',
            '╗': '\x1b[37m',
            '╔': '\x1b[37m',
            # More mappings for different characters here
        }
    },
}