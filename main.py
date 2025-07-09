import pygame
from titlescreen import UIElement
from gameState import GameState

def main():
    pygame.init()
    # Screen size
    screen = pygame.display.set_mode((1080, 720))
    # Game Title
    pygame.display.set_caption('Teleporto')

    quit_btn = UIElement(
        center_position = (540, 400),
        font_size = 30,
        bg_rgb = (27, 36, 72),
        text_rgb = (228, 219, 183),
        text = "Quit",
        action=GameState.QUIT,
    )   


    while True:
        mouse_up = False
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONUP and e.button == 1:
                mouse_up = True
        screen.fill((27, 36, 72))

        ui_action = quit_btn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return
        quit_btn.draw(screen)
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
