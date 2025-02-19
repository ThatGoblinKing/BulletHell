import math
import random
from functools import partial
from math import degrees
from typing import Tuple, override
from unittest import case

from pygame import Vector2
import pygame as pg

from Bullet import Bullet
from Constants import ScreenConstants, EnemyConstants
from GameEntity import GameEntity
from ShootPatterns.FlowerShoot import FlowerShoot
from ShootPatterns.ShootPattern import ShootPattern

class Enemy(GameEntity):



    _CIRCLE_RAD: int = 400

    def __init__(self,
                 pos: Vector2 | Tuple[int, int],
                 movement_pattern: str,
                 shoot_pattern: ShootPattern,
                 start_angle: int = 0,
                 size: Tuple[int, int] = EnemyConstants.DEFAULT_SIZE,
                 color: Tuple[int, int, int] = EnemyConstants.DEFAULT_COLOR,
                 shoot_interval: int = EnemyConstants.DEFAULT_SHOOT_INTERVAL,
                 speed: int = EnemyConstants.DEFAULT_SPEED):
        super().__init__(pos, size, color)
        self.shoot_interval = shoot_interval
        self.last_shot_time = 0
        self.speed = speed
        self.angle = start_angle
        self._movement_key = movement_pattern
        self._shoot_pattern = partial(shoot_pattern.shoot)

    @property
    def movement_pattern(self):
        method_name = EnemyConstants.MOVEMENT_PATTERNS.get(self._movement_key, "move_linear")
        return getattr(self, method_name, self.move_linear)

    @override
    def update(self, *args, **kwargs) -> None:
        super().update(*args, **kwargs)
        self.movement_pattern()
        self.velocity.x = self.speed * math.sin(math.radians(-self.angle))
        self.velocity.y = self.speed * math.cos(math.radians(-self.angle))
        self.rect.center += self.velocity

    @override
    def __str__(self):
        return f"""<enemy({self.rect.x}, {self.rect.y}, {self._movement_key}, {self.speed}, {self.angle}deg)>"""

    def shoot(self, bullet_group: pg.sprite.Group) -> None:
        self._shoot_pattern(self.rect.centerx, self.rect.centery, bullet_group)

    def move_linear(self):
        if self.clamp_within_screen():
            self.angle += 180
            self.angle %= 360

    def move_circular(self):
        self.angle += self.speed / self._CIRCLE_RAD * 360
        self.angle %= 360
        self.clamp_within_screen()

