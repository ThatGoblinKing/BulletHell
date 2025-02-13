from typing import Tuple, override

from pygame.sprite import Sprite
from pygame import Vector2, Rect
import pygame as pg

from Constants import Input, Physics, Screen, PlayerConstants as PConst
from GameEntity import GameEntity


class Player(GameEntity):
    def __init__(self, pos: Vector2 | Tuple[int, int]):
        # Sprite Init -----------------------------------------------
        super().__init__(pos, PConst.SIZE, PConst.COLOR)
        # Inputs ----------------------------------------------------
        self.pressed_keys: list[bool] = [False, False, False, False]
        self.move_dir: Vector2 = Vector2(0, 0)
        self.input_x: int = 0
        self.input_y: int = 0
        # Conditions ------------------------------------------------
        self.is_invuln: bool = False
        # Stats -----------------------------------------------------
        self.health: int = 3

    @override
    def update(self, events: list[pg.event.Event]):
        super().update()

        # Inputs ----------------------------------------------------
        for event in events:
            if event.type == pg.KEYDOWN:
                match event.key:
                    case pg.K_a:
                        self.pressed_keys[Input.LEFT] = True
                    case pg.K_d:
                        self.pressed_keys[Input.RIGHT] = True
                    case pg.K_w:
                        self.pressed_keys[Input.UP] = True
                    case pg.K_s:
                        self.pressed_keys[Input.DOWN] = True
            if event.type == pg.KEYUP:
                match event.key:
                    case pg.K_a:
                        self.pressed_keys[Input.LEFT] = False
                    case pg.K_d:
                        self.pressed_keys[Input.RIGHT] = False
                    case pg.K_w:
                        self.pressed_keys[Input.UP] = False
                    case pg.K_s:
                        self.pressed_keys[Input.DOWN] = False

        self.move_dir += self.get_move_vector(self.pressed_keys)
        if self.move_dir.magnitude() > 0:
            self.move_dir.clamp_magnitude_ip(PConst.MOVE_SPEED)

        self.rect.center += Vector2(self.velocity.x + self.move_dir.x, self.velocity.y + self.move_dir.y)

        # Clamp within screen bounds
        self.rect.y = int(pg.math.clamp(self.rect.y, 0, Screen.SIZE[1] - PConst.SIZE[1]))
        self.rect.x = int(pg.math.clamp(self.rect.x, 0, Screen.SIZE[0] - PConst.SIZE[0]))

    def get_move_vector(self, inputs: list[bool]) -> Vector2:
        input_x = 0 if inputs[Input.LEFT] == inputs[Input.RIGHT] \
            else -1 if inputs[Input.LEFT] \
            else 1
        input_y = 0 if inputs[Input.UP] == inputs[Input.DOWN] \
            else -1 if inputs[Input.UP] \
            else 1
        return Vector2((input_x * PConst.MOVE_SPEED) - (self.move_dir.x * Physics.FRICTION),
                       (input_y * PConst.MOVE_SPEED) - (self.move_dir.y * Physics.FRICTION))