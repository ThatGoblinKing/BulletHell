from typing import Tuple

from Constants import ScreenConstants

import pygame as pg
from pygame import Vector2, Rect
from pygame.sprite import Sprite

class GameEntity(Sprite):
    def __init__(self, pos: Vector2 | Tuple[int, int], size: Tuple[int, int], color: Tuple[int, int, int]):
        # Sprite Init -----------------------------------------------
        super().__init__()
        self.image = pg.Surface(size)
        self.image.fill(color)
        pg.draw.rect(self.image,
                         color,
                         pg.Rect(pos, size))
        # Physics ---------------------------------------------------
        self.rect: Rect = self.image.get_rect()
        self.rect.center = pos
        self.velocity: Vector2 = Vector2(0, 0)

    def clamp_within_screen(self) -> bool:
        start_rect_pos = self.rect.center
        self.rect = self.rect.clamp(Rect((0,0), ScreenConstants.SIZE))
        return not start_rect_pos == self.rect.center
