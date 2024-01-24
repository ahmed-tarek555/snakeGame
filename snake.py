import pygame
import random

sizeGained = 5
sizeLost = 5


def changeDirection(object):
    if object.direction == "LEFT":
        object.direction = "RIGHT"
    elif object.direction == "RIGHT":
        object.direction = "LEFT"
    elif object.direction == "UP":
        object.direction = "DOWN"
    elif object.direction == "DOWN":
        object.direction = "UP"


class Obstacle:
    instances = []

    def __init__(self, x, y, width, height):
        Obstacle.instances.append(self)
        self.rect = pygame.Rect(x, y, width, height)


obstacleLeft = Obstacle(0, 0, 10, 600)
obstacleRight = Obstacle(990, 0, 10, 600)
obstacleUp = Obstacle(0, 0, 1000, 10)
obstacleDown = Obstacle(0, 590, 1000, 10)

numberOfObstacles = len(Obstacle.instances)


class Food:
    def __init__(self, x, y, width, length):
        self.rect = pygame.Rect(x, y, width, length)

    def respawn(self):
        if self.rect.colliderect(mysnake.rect):
            self.rect.x = random.randint(50, 950)
            self.rect.y = random.randint(50, 550)


class Snake:
    def __init__(self, x, y, width, height, speed, direction):
        self.speed = speed
        self.direction = direction
        self.rect = pygame.Rect(x, y, width, height)

    def eat(self):
        if self.rect.colliderect(myfood.rect):
            self.rect.width += sizeGained
            self.rect.height += sizeGained

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction = "LEFT"
        if keys[pygame.K_RIGHT]:
            self.direction = "RIGHT"
        if keys[pygame.K_UP]:
            self.direction = "UP"
        if keys[pygame.K_DOWN]:
            self.direction = "DOWN"

        if self.direction == "LEFT":
            self.rect.x -= self.speed
        elif self.direction == "RIGHT":
            self.rect.x += self.speed
        elif self.direction == "UP":
            self.rect.y -= self.speed
        elif self.direction == "DOWN":
            self.rect.y += self.speed

    def collisions(self):
        counter = 0
        while counter < numberOfObstacles:
            if self.rect.colliderect(Obstacle.instances[counter].rect):
                changeDirection(self)
                self.rect.width -= sizeLost
                self.rect.height -= sizeLost
            counter += 1
        if self.rect.width < 15:
            self.rect.width = 15
            self.rect.height = 15


mysnake = Snake(100, 100, 30, 30, 2, "RIGHT")
myfood = Food(50, 50, 20, 20)
