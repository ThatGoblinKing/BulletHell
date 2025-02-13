import math
import random
from typing import Tuple, override
from pygame import Vector2
import pygame as pg
from Constants import Screen, EnemyDefaults as EnDefault
from GameEntity import GameEntity

class Enemy(GameEntity):
    LIN_MOVE: int = 0
    CIRC_MOVE: int = 1

    _CIRCLE_RAD: int = 200

    def __init__(self,
                 pos: Vector2 | Tuple[int, int],
                 movement_pattern: int,
                 size: Tuple[int, int] = EnDefault.SIZE,
                 color: Tuple[int, int, int] = EnDefault.COLOR,
                 shoot_interval: int = EnDefault.SHOOT_INTERVAL,
                 speed: int = EnDefault.SPEED):
        super().__init__(pos, size, color)
        self.shoot_interval = shoot_interval
        self.last_shot_time = 0
        self.speed = speed
        self.angle = 0
        self.bullets = []
        match movement_pattern:
            case self.LIN_MOVE:
                self.movement_pattern = self.move_linear
            case self.CIRC_MOVE:
                self.movement_pattern = self.move_circular

    @override
    def update(self, *args, **kwargs) -> None:
        super().update(*args, **kwargs)
        self.movement_pattern()
        self.velocity.x = self.speed * math.sin(math.radians(-self.angle))
        self.velocity.y = self.speed * math.cos(math.radians(-self.angle))
        self.rect.center += self.velocity


    def shoot(self, bullet_group: pg.sprite.Group) -> None:
        raise NotImplementedError('Enemy "shoot" method intended to be overridden.')

    def move_linear(self):
        if self.rect.left < 0 or self.rect.right > Screen.SIZE[0] or self.rect.top < 0 or self.rect.bottom > Screen.SIZE[1]:
            self.angle += 180
            self.angle %= 360
        self.clamp_within_screen(self.rect)

    def clamp_within_screen(self, rect: pg.Rect):
        rect.y = int(pg.math.clamp(self.rect.y, 0, Screen.SIZE[1] - rect.size[1]))
        rect.x = int(pg.math.clamp(self.rect.x, 0, Screen.SIZE[0] - rect.size[0]))

    def move_circular(self):
        self.angle += self.speed / self._CIRCLE_RAD