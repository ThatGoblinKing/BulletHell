from typing import Tuple, override

from pygame.sprite import Sprite
from pygame import Vector2, Rect
import pygame as pg

from Constants import Input, PhysicsConstants, ScreenConstants, PlayerConstants
from GameEntity import GameEntity


class Player(GameEntity):
    def __init__(self, pos: Vector2 | Tuple[int, int]):
        # Sprite Init -----------------------------------------------
        super().__init__(pos, PlayerConstants.SIZE, PlayerConstants.COLOR)
        # Inputs ----------------------------------------------------
        self.pressed_keys: list[bool] = [False, False, False, False]
        self.move_dir: Vector2 = Vector2(0, 0)
        self.input_x: int = 0
        self.input_y: int = 0
        # Conditions ------------------------------------------------
        self.is_invulnerable: bool = False
        # Stats -----------------------------------------------------
        self.health: int = 3

    @override
    def update(self, events: list[pg.event.Event]):
        super().update()

        # Inputs ----------------------------------------------------
        for event in events:
                self.pressed_keys[PlayerConstants.KEYMAPS[event.key]] = event.type == pg.KEYDOWN

        self.move_dir += self.get_move_vector(self.pressed_keys)
        if self.move_dir.magnitude() > 0:
            self.move_dir.clamp_magnitude_ip(PlayerConstants.MOVE_SPEED)

        self.rect.center += Vector2(self.velocity.x + self.move_dir.x, self.velocity.y + self.move_dir.y)
        self.clamp_within_screen()

    def get_move_vector(self, inputs: list[bool]) -> Vector2:
        input_x = 0 if inputs[Input.LEFT] == inputs[Input.RIGHT] \
            else -1 if inputs[Input.LEFT] \
            else 1
        input_y = 0 if inputs[Input.UP] == inputs[Input.DOWN] \
            else -1 if inputs[Input.UP] \
            else 1
        return Vector2((input_x * PlayerConstants.MOVE_SPEED) - (self.move_dir.x * PhysicsConstants.FRICTION),
                       (input_y * PlayerConstants.MOVE_SPEED) - (self.move_dir.y * PhysicsConstants.FRICTION))