import pygame
from pygame import Vector2

from Enemies.Enemy import Enemy
from Player import Player
from Constants import ScreenConstants, PlayerConstants

from ShootPatterns.FlowerShoot import FlowerShoot
from ShootPatterns.FireworkShoot import FireworkShoot
from ShootPatterns.ShootPattern import ShootPattern

pygame.init()
pygame.display.set_caption("Bullet Hell!")
screen = pygame.display.set_mode(ScreenConstants.SIZE)
screen.fill((0,0,0))
clock = pygame.time.Clock()
gameover = False

player = Player(Vector2(ScreenConstants.SIZE[0] // 2, ScreenConstants.SIZE[1] // 2))
test_enemy = Enemy((300, 300), movement_pattern="linear", shoot_pattern=FireworkShoot(20))

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
                test_enemy.shoot(bullet_sprites)

    bullet_sprites.update()
    player.update(events=[event for event in game_events
                          if event.type in (pygame.KEYDOWN, pygame.KEYUP)
                          and event.key in PlayerConstants.KEYMAPS])
    test_enemy.update()
    screen.fill((0,0,0))
    for bullet in bullet_sprites:
        bullet.draw_trajectory(screen)
    bullet_sprites.draw(screen)
    all_sprites.draw(screen)

    pygame.display.flip()

else:
    pygame.quit()