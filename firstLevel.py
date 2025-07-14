import pygame
from gameState import GameState
from Character import Character

def first_level(screen):
    running = True
    clock = pygame.time.Clock()

    player = Character("Characters/teleporto/teleporto_idle.png", 10, 10)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameState.QUIT
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                return GameState.TITLE
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.x -= 10
                if event.key == pygame.K_RIGHT:
                    player.x += 10

        screen.fill((0, 0, 0))

        player.draw(screen)
        pygame.display.update()


        pygame.display.flip()
        clock.tick(60)
