import pygame
from pygame import Vector2

from Enemies.Enemy import Enemy
from Player import Player
from Constants import Screen

pygame.init()
pygame.display.set_caption("Bullet Hell!")
screen = pygame.display.set_mode(Screen.SIZE)
screen.fill((0,0,0))
clock = pygame.time.Clock()
gameover = False

player = Player(Vector2(Screen.SIZE[0] // 2, Screen.SIZE[1] // 2))
test_enemy = Enemy((300, 300), movement_pattern=Enemy.CIRC_MOVE)

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(test_enemy)


while not gameover:
    clock.tick(60)
    game_events = pygame.event.get()
    for event in game_events:
        if event.type == pygame.QUIT:
            gameover = True

    player.update(events=game_events)
    test_enemy.update()

    screen.fill((0,0,0))
    all_sprites.draw(screen)

    pygame.display.flip()

else:
    pygame.quit()