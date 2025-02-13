import math
import random
from math import degrees
from typing import Tuple, override
from unittest import case

from pygame import Vector2
import pygame as pg

from Bullet import Bullet
from Constants import Screen, EnemyDefaults as EnDefault
from GameEntity import GameEntity

class Enemy(GameEntity):

    LIN_MOVE: int = 0
    CIRC_MOVE: int = 1
    SQUARE_SHOOT: int = 0
    FLOWER_SHOOT: int = 1
    FIREWORK_SHOOT: int = 2

    _CIRCLE_RAD: int = 400

    def __init__(self,
                 pos: Vector2 | Tuple[int, int],
                 movement_pattern: int,
                 shoot_pattern: int,
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

        match shoot_pattern:
            case self.FLOWER_SHOOT:
                self.shoot_pattern = self.shoot_flower
            case self.FIREWORK_SHOOT:
                self.shoot_pattern = self.shoot_firework

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
        self.angle += self.speed / self._CIRCLE_RAD * 360
        self.angle %= 360

    def shoot_firework(self, bullet_count: int, bullet_group: pg.sprite.Group, spawn_rad: int = EnDefault.BULLET_SPAWN_RAD):
        bullet_pos = self.get_bullet_pos(bullet_count)
        angle_step = 360 / bullet_count

        for i in range(len(bullet_pos)):
            angle = angle_step * i
            self.bullets.append(Bullet(bullet_pos[i], angle))
            bullet_group.add(self.bullets[-1])


    def shoot_flower(self, bullet_count: int, bullet_group: pg.sprite.Group, spawn_rad: int = EnDefault.BULLET_SPAWN_RAD):
        bullet_pos = self.get_bullet_pos(bullet_count)
        angle_step = 360 / bullet_count

        for i in range(len(bullet_pos)):
            angle = angle_step * i
            self.bullets.append(Bullet(bullet_pos[i], angle, delta_curve=1))
            bullet_group.add(self.bullets[-1])

    def get_bullet_pos(self, bullet_count: int, spawn_rad: int = EnDefault.BULLET_SPAWN_RAD) -> list[tuple[int, int]]:
        pos_list = []
        angle_step = (2 * math.pi)/(bullet_count)
        for i in range(bullet_count):
            pos_list.append((
                int(math.cos(i * angle_step) * spawn_rad + self.rect.x),
                int(math.sin(i * angle_step) * spawn_rad + self.rect.y)))
        return pos_list