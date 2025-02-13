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
test_enemy = Enemy((300, 300), movement_pattern=Enemy.CIRC_MOVE, shoot_pattern=Enemy.FLOWER_SHOOT)

bullet_sprites = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(test_enemy)


while not gameover:
    clock.tick(60)
    game_events = pygame.event.get()
    for event in game_events:
        if event.type == pygame.QUIT:
            gameover = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                test_enemy.shoot_flower(8, bullet_sprites)

    bullet_sprites.update()
    player.update(events=game_events)
    test_enemy.update()

    screen.fill((0,0,0))
    bullet_sprites.draw(screen)
    all_sprites.draw(screen)

    pygame.display.flip()

else:
    pygame.quit()