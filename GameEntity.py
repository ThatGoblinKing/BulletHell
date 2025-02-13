from typing import Tuple

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