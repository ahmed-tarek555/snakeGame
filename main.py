import pygame
import sys
from snake import mysnake
from snake import myfood
from snake import obstacleLeft
from snake import obstacleRight
from snake import obstacleUp
from snake import obstacleDown


running = True
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()

while running:
    screen.fill((128, 128, 128))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    mysnake.move()
    mysnake.eat()
    mysnake.collisions()
    myfood.respawn()

    pygame.draw.rect(screen, (28, 28, 28), obstacleLeft)
    pygame.draw.rect(screen, (28, 28, 28), obstacleRight)
    pygame.draw.rect(screen, (28, 28, 28), obstacleUp)
    pygame.draw.rect(screen, (28, 28, 28), obstacleDown)
    pygame.draw.rect(screen, (255, 0, 0), mysnake)
    pygame.draw.rect(screen, (55, 233, 35), myfood)

    pygame.display.update()
    clock.tick(60)
