import pygame
import sys
from pygame.locals import *

class Character:
    def __init__(self, image, x, y, width, height):
        original_image = pygame.image.load(image)
        self.image = pygame.transform.scale(original_image, (width, height))
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
