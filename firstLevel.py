import pygame
from gameState import GameState

def first_level(screen):
    running = True
    clock = pygame.time.Clock()



    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameState.QUIT
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                return GameState.TITLE

        screen.fill((0, 0, 0))




        pygame.display.flip()
        clock.tick(60)
