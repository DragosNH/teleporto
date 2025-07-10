import pygame
from titlescreen import UIElement
from gameState import GameState
from firstLevel import first_level

def title_screen(screen):
    start_btn = UIElement(
        center_position=(540, 300),
        font_size=30,
        bg_rgb=(27, 36, 72),
        text_rgb=(228, 219, 183),
        text="Start Game",
        action=GameState.NEWGAME,
    )
    quit_btn = UIElement(
        center_position=(540, 400),
        font_size=30,
        bg_rgb=(27, 36, 72),
        text_rgb=(228, 219, 183),
        text="Quit",
        action=GameState.QUIT,
    )

    buttons = [start_btn, quit_btn]

    while True:
        mouse_up = False
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return GameState.QUIT
            if e.type == pygame.MOUSEBUTTONUP and e.button == 1:
                mouse_up = True
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    return GameState.QUIT
            if e.type == start_btn:
                return GameState.NEWGAME

        screen.fill((27, 36, 72))

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()


def main():
    pygame.init()
    screen = pygame.display.set_mode((1080, 720))
    pygame.display.set_caption('Teleporto')

    game_state = GameState.TITLE

    while True:
        if game_state == GameState.TITLE:
            game_state = title_screen(screen)

        elif game_state == GameState.NEWGAME:
            game_state = GameState.TITLE

        elif game_state == GameState.QUIT:
            break

    pygame.quit()

if __name__ == "__main__":
    main()
