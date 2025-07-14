import pygame
from gameState import GameState
from Character import Character

def first_level(screen):
    running = True
    clock = pygame.time.Clock()

    player = Character("Characters/teleporto/teleporto_idle.png", 100, 100)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameState.QUIT
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                return GameState.TITLE

        screen.fill((0, 0, 0))

        player.draw(screen)
        pygame.display.update()


        pygame.display.flip()
        clock.tick(60)
