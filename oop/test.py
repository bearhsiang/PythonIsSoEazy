import pygame

class Ball:

    def __init__(self, pos_x, pos_y, v_x, v_y, r):

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.v_x = v_x
        self.v_y = v_y
        self.r = r

    def update(self):

        self.pos_x += self.v_x
        self.pos_y += self.v_y

    def draw(self, canvas):
        w, h = canvas.get_size()
        pygame.draw.circle(canvas, (100, 100, 255), (self.pos_x, h-self.pos_y), self.r)

w = 500
h = 200

pygame.display.set_caption("First Game")
win = pygame.display.set_mode(size=(w, h))
clock = pygame.time.Clock()

while True:
    x, y = 100, 100
    for i in range(10):
        win.fill((0, 0, 0))
        pygame.draw.circle(win, (100, 100, 255), (x, y), 50)
        x += 30
        pygame.display.update()
        clock.tick(10)

input()
pygame.quit()