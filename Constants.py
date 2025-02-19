from enum import Enum, unique
import pygame as pg

@unique
class Input(int, Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

class PlayerConstants:
    SIZE = (10,10)
    COLOR = (255,255,255)
    MOVE_SPEED = 5
    INVINCIBILITY_TIME = 1000
    KEYMAPS = {
        pg.K_a: Input.LEFT,
        pg.K_d: Input.RIGHT,
        pg.K_w: Input.UP,
        pg.K_s: Input.DOWN
    }

class PhysicsConstants:
    FRICTION = 0.5

class ScreenConstants:
    SIZE = (1280, 720)

class EnemyConstants:
    DEFAULT_SIZE = (10, 10)
    DEFAULT_COLOR = (219,83,83)
    DEFAULT_SHOOT_INTERVAL = 10000
    DEFAULT_SPEED = 5
    DEFAULT_BULLET_SPAWN_RAD = 200
    MOVEMENT_PATTERNS = {
        "linear": "move_linear",
        "circular": "move_circular"
    }

class BulletConstants:
    DEFAULT_SIZE = (5, 5)
    DEFAULT_COLOR = (255, 255, 255)
    DEFAULT_SPEED = 3


