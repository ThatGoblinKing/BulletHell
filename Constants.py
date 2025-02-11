from enum import Enum

class PlayerConstants:
    SIZE = (50,50)
    COLOR = (255,255,255)
    MOVE_SPEED = 4
    INVINCIBILITY_TIME = 1000

class Input(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3