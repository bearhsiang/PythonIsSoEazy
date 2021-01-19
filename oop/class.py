import pygame
h, w = 500, 500
pygame.display.set_caption("First Game")
win = pygame.display.set_mode(size=(h, w))
clock = pygame.time.Clock()

x = 10
for i in range(10):
    win.fill((0, 0, 0))
    pygame.draw.circle(win, (100, 100, 255), (x, 250), 50)
    pygame.display.update()
    x += 50
    clock.tick(1000)

input()
pygame.quit()