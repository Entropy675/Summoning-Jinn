
# Define all constants in this file, for organizations sake
# Avoid creating constants in other files, try to define them here then use them elsewhere after including this file

from enum import Enum

# Define screen enums
class Screen(Enum):
    LOADING = 0
    MAIN = 1
    PAUSE = 2
    DEATH = 3

WIDTH = 1280
HEIGHT = 756
PLR_SPEED = 6
PLR_SPEED_BASE_LIMIT = 16;
PLR_MAX_HEALTH = 100;
PLR_MAX_MANA = 100;


FPS = 120 #pref
# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
