import pygame

SCREEN_SIZE = (1280, 720)
pygame.init()
pygame.display.set_caption("Bullet Hell!")
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill((0,0,0))
clock = pygame.time.Clock()
gameover = False
while not gameover:
    clock.tick(60)
    game_events = pygame.event.get()
    for event in game_events:
        if event.type == pygame.QUIT:
            gameover = True
else:
    pygame.quit()