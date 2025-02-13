class PlayerConstants:
    SIZE = (10,10)
    COLOR = (255,255,255)
    MOVE_SPEED = 5
    INVINCIBILITY_TIME = 1000

class Input:
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

class Physics:
    FRICTION = 0.5

class Screen:
    SIZE = (1280, 720)

class EnemyDefaults:
    SIZE = (10, 10)
    COLOR = (219,83,83)
    SHOOT_INTERVAL = 10000
    SPEED = 5
    BULLET_SPAWN_RAD = 20

class BulletDefaults:
    SIZE = (5,5)
    COLOR = (255,255,255)
    SPEED = 3
