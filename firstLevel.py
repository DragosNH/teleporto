import pygame

def first_level(screen):




    while True:
        mouse_up = False
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONUP and e.button == 1:
                mouse_up = True
        screen.fill((27, 36, 72))


        pygame.display.flip()
