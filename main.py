import pygame
import random

width1 = 40
height1 = 300
x = 136.5
y = 0
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color("black"))
pygame.display.set_caption("Нажми на экран")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            coord = event.pos
            pygame.draw.ellipse(screen, pygame.Color("yellow"),
                                (coord[0], coord[1], random.choice(range(1, 100)), random.choice(range(1, 100))))
    pygame.display.flip()
pygame.quit()
