import pygame
from titlescreen import UIElement, title_screen
from gameState import GameState
from firstLevel import first_level




def main():
    pygame.init()
    screen = pygame.display.set_mode((1080, 720))
    pygame.display.set_caption('Teleporto')

    game_state = GameState.TITLE

    while True:
        if game_state == GameState.TITLE:
            game_state = title_screen(screen)

        elif game_state == GameState.NEWGAME:
            game_state = first_level(screen)

        elif game_state == GameState.QUIT:
            break

    pygame.quit()

if __name__ == "__main__":
    main()
