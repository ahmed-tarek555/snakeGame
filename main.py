import pygame
import sys
from snake import mysnake
from snake import myfood


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

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    #     mysnake.rect.x -= mysnake.speed
    # if keys[pygame.K_RIGHT]:
    #     mysnake.rect.x += mysnake.speed
    # if keys[pygame.K_UP]:
    #     mysnake.rect.y -= mysnake.speed
    # if keys[pygame.K_DOWN]:
    #     mysnake.rect.y += mysnake.speed

    if mysnake.rect.x != myfood.rect.x:
        if mysnake.rect.x < myfood.rect.x:
            mysnake.rect.x += mysnake.speed
        if mysnake.rect.x > myfood.rect.x:
            mysnake.rect.x -= mysnake.speed
    if mysnake.rect.y != myfood.rect.y:
        if mysnake.rect.y < myfood.rect.y:
            mysnake.rect.y += mysnake.speed
        if mysnake.rect.y > myfood.rect.y:
            mysnake.rect.y -= mysnake.speed



    mysnake.eat()
    myfood.respawn()

    pygame.draw.rect(screen, (255, 0, 0), mysnake)
    pygame.draw.rect(screen, (55, 233, 35), myfood)


    pygame.display.update()
    clock.tick(60)