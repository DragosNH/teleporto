import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from gameState import GameState

# Title Screen buttons
def create_surface(text, font_size, text_rgb, bg_rgb):
    font = pygame.freetype.SysFont("Courier", font_size, bold = True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()

class UIElement(Sprite):
    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None):
        super().__init__()
        self.mouse_over = False

        self.default_image = create_surface(text, font_size, text_rgb, bg_rgb)
        self.hover_image = create_surface(text, int(font_size * 1.5), text_rgb, bg_rgb)

        self.default_rect = self.default_image.get_rect(center=center_position)
        self.hover_rect = self.hover_image.get_rect(center=center_position)
        self.action = action

    @property
    def image(self):
        return self.hover_image if self.mouse_over else self.default_image

    @property
    def rect(self):
        return self.hover_rect if self.mouse_over else self.default_rect

    def update(self, mouse_pos, mouse_up):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else: 
            self.mouse_over = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)

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
