import pygame
h, w = 500, 500
pygame.display.set_caption("First Game")
win = pygame.display.set_mode(size=(h, w))
### default size = (0, 0) (full screen)
### type = pygame.Surface

input()
pygame.quit()
# while True:
#     win.fill((0, 0, 0))
#     pygame.draw.rect(win, (100, 100, 255), pygame.Rect(10, 10, 100, 100))
#     pygame.display.update()