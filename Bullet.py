import math
from typing import Tuple, override

from GameEntity import GameEntity
from Constants import BulletDefaults as BDef

class Bullet(GameEntity):
    def __init__(self,
                 pos: Tuple[int, int],
                 angle: int,
                 size: Tuple[int, int] = BDef.SIZE,
                 speed: int = BDef.SPEED,
                 delta_curve: int = 0):
        super().__init__(pos, size, BDef.COLOR)
        self.speed = speed
        self.angle = angle
        self.delta_curve = delta_curve

    @override
    def update(self):
        self.angle += self.delta_curve
        self.move()
        self.rect.center += self.velocity

    def move(self):
        self.velocity.x = self.speed * math.sin(math.radians(-self.angle))
        self.velocity.y = self.speed * math.cos(math.radians(-self.angle))