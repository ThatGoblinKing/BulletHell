import math
from typing import Tuple, override

import pygame
from pygame import Vector2

from GameEntity import GameEntity
from Constants import BulletConstants as BDef

class Bullet(GameEntity):
    def __init__(self,
                 pos: Tuple[int, int],
                 angle: int,
                 size: Tuple[int, int] = BDef.DEFAULT_SIZE,
                 speed: int = BDef.DEFAULT_SPEED,
                 delta_curve: int = 0):
        super().__init__(pos, size, BDef.DEFAULT_COLOR)
        self.speed = speed
        self.angle = angle
        self.delta_curve = delta_curve

    @override
    def update(self):
        self.angle += self.delta_curve
        self.velocity = Vector2(
            self.speed * math.cos(self.angle),
            self.speed * math.sin(self.angle)
        )
        self.rect.center += self.velocity

    def draw_trajectory(self, screen: pygame.Surface):
        pygame.draw.line(screen, (255,0,0), self.rect.center, self.rect.center + (self.velocity * 10))