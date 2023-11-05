# Will Contain the entire map for the game in a dictionary.

WORLD = {
    'room1': {
        'map': [
            "___.._",
            "___.._",
            "___.._"
        ],
        'colors': {
            '.': '\033[37m',  # Grey color for dots
            '_': '\033[34m',  # Blue color for underscores
            # You can add more mappings for different characters here
        }
    },
    'room2': {
        'map': [
            "#####",
            "#_#_#",
            "#_#_#",
            "#####"
        ],
        'colors': {
            '#': '\033[32m',  # Green color for walls
            '_': '\033[34m',  # Blue color for underscores
            # You can add more mappings for different characters here
        }
    },
    # Add more rooms and their map data here
}