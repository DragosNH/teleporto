import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum

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
