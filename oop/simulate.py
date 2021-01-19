import pygame
import random

a_x = 0
a_y = -10

rate = 24

class Ball:

    def __init__(self, pos_x, pos_y, v_x, v_y, r):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.v_x = v_x
        self.v_y = v_y
        self.r = r

    def update(self, canvas):

        w, h = canvas.get_size()

        self.pos_x += self.v_x
        self.pos_y += self.v_y

        if self.pos_x < 0:
            self.pos_x *= -1
            self.v_x *= -1

        if self.pos_x >= w:
            self.pos_x = 2*w-self.pos_x
            self.v_x *= -1

        if self.pos_y < 0:
            self.pos_y *= -1
            self.v_y *= -1
        
        if self.pos_y >= h:
            self.pos_y = 2*h-self.pos_y
            self.v_y *= -1


        # if self.pos_y < self.r:
        #     self.v_y *= -1
        #     self.pos_y = self.r

        # self.v_x += a_x
        # self.v_y += a_y

    def draw(self, canvas):
        w, h = canvas.get_size()
        pygame.draw.circle(canvas, (100, 100, 255), (self.pos_x, self.pos_y), self.r)


if __name__ == '__main__':
    h, w = 500, 500     
    win = pygame.display.set_mode(size=(h, w))
    b_list = []
    # for i in range(10):
    #     x = random.random()*w
    #     y = random.random()*h
    #     v_x = (random.random()-0.5) * 100
    #     v_y = (random.random()-0.5) * 100
    #     radius = random.random()*100
    #     b_list.append(Ball(x, y, v_x, v_y, radius))
    clock = pygame.time.Clock()
    r = 0
    pressed = False
    finish = False
    while not finish:
        clock.tick(rate)

        for ball in b_list:
            ball.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed = True
                    print('space is pressed')
                elif event.key == pygame.K_q:
                    finish = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    b_list.append(Ball(100, 100, (random.random()-0.5)*100, (random.random()-0.5)*100, r))
                    r = 0
                    pressed = False
        if pressed:
            r += 1

        win.fill((0, 0, 0))
        for ball in b_list:
            ball.draw(win)
        pygame.draw.circle(win, (100, 100, 255), (100, 100), r)
        pygame.display.update()

pygame.quit()