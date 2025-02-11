import pygame
from pygame.sprite import Sprite
from pygame import Vector2, Rect
import pygame as pg

from Constants import PlayerConstants as PConst


class Player(Sprite):
    def __init__(self, pos: Vector2):
        # Sprite Init -----------------------------------------------
        super().__init__()
        self.image = pg.Surface(PConst.SIZE)
        self.image.fill(PConst.COLOR)
        pg.draw.rect(self.image,
                         PConst.COLOR,
                         pg.Rect(pos, PConst.SIZE))
        # Physics ---------------------------------------------------
        self.rect: Rect = self.image.get_rect()
        self.velocity: Vector2 = Vector2(0, 0)
        self.pressed_keys: list[bool] = [False, False, False, False]
        self.input: Vector2 = Vector2(0, 0)
        self.move_dir: Vector2 = Vector2(0, 0)
        # Conditions ------------------------------------------------
        self.is_invuln: bool = False
        # Stats -----------------------------------------------------
        self.health: int = 3

    def update(self, events: list[pg.event.Event]):
        TIME = pg.time.get_ticks()

        # Inputs ----------------------------------------------------
        for event in events:
            if event.type == pg.KEYDOWN:
                match event.key:
                    case pg.K_a:
                        self.pressed_keys[0] = True
                    case pg.K_d:
                        pass
                    case pg.K_w:
                        pass
                    case pg.K_s:
