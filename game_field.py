import pygame
import sys

pygame.init()

width = height = 10
margin = 1
pixel_color = (167, 240, 50)

wx = 800
yx = 600
size = ((wx + margin), (yx + margin))

pixel = wx // (width + margin)
print(pixel)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Game field')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    for column in range(pixel):
        for row in range(pixel):
            x = column * width + (column + 1) * margin
            y = row * height + (row + 1) * margin
            pygame.draw.rect(screen, pixel_color, (x, y, width, height))
    pygame.display.update()
