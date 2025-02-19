from abc import abstractmethod

from Constants import EnemyConstants
from math import cos, sin, radians
from pygame import sprite

class ShootPattern:
    """Base class for shooting behaviors"""

    def __init__(self, bullet_count: int, spawn_rad: int = EnemyConstants.DEFAULT_BULLET_SPAWN_RAD):
        self.bullet_count = bullet_count
        self.spawn_rad = spawn_rad

    @abstractmethod
    def shoot(self, x: int, y: int, bullet_group: sprite.Group) -> None:
        """A method that instantiates {bullet_group} objects, subclasses must implement this."""
        pass

    @staticmethod
    def _get_bullet_pos_around(x: int,
                               y: int,
                               bullet_count: int,
                               spawn_rad: int) -> list[tuple[int, int, float]]:
        """Spawns {bullet_count} number of bullets in a circle of radius {spawn_rad} around the point {x, y}"""
        pos_list = []
        angle_step = radians(360) / bullet_count
        for i in range(bullet_count):
            angle = (angle_step * i)
            pos_list.append((
                cos(angle) * spawn_rad + x,
                sin(angle) * spawn_rad + y))
        return pos_list