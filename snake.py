import pygame
import random

sizeGained = 5
sizeLost = 5

screen = pygame.display.set_mode((1000, 600))

def follow(object, objectFollowed, speed):
    if object.x < objectFollowed.x + 20:
        object.x += speed
    if object.x > objectFollowed.x + 20:
        object.x -= speed
    if object.y < objectFollowed.y + 20:
        object.y += speed
    if object.y > objectFollowed.y + 20:
        object.y -= speed

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
        self.tail = []
        self.numberOfSegments = 0

    def eat(self):
        if self.rect.colliderect(myfood):
            self.tail.append(pygame.Rect(self.rect.x, self.rect.y, 20, 20))
            self.tail.append(pygame.Rect(self.tail[-1].x, self.tail[-1].y, 20, 20))
            self.numberOfSegments += 1
        if self.numberOfSegments > 0:
            counter = 0
            while counter < self.numberOfSegments:
                pygame.draw.rect(screen, (255, 0, 0), self.tail[counter])
                counter += 1

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

        if self.numberOfSegments > 0:
            follow(self.tail[0], self.rect, self.speed)
            counter = 1
            while counter < self.numberOfSegments:
                follow(self.tail[counter], self.tail[counter - 1], self.speed)
                counter += 1

        # self.update_tail()

    # def update_tail(self):
    #     if self.numberOfSegments > 0:
    #         # Move the last segment to the position of the snake's head
    #         self.tail[-1].topleft = (self.rect.x, self.rect.y)
    #         # Iterate through the segments starting from the second to last
    #         for i in range(self.numberOfSegments - 1, 0, -1):
    #             # Move each segment to the position of the segment in front of it
    #             self.tail[i].topleft = (self.tail[i - 1].x, self.tail[i - 1].y)
    #         # Move the first segment to the previous position of the snake's head
    #         self.tail[0].topleft = (self.rect.x, self.rect.y)

    def collisions(self):
        counter = 0
        while counter < numberOfObstacles:
            if self.rect.colliderect(Obstacle.instances[counter].rect):
                changeDirection(self)
                self.numberOfSegments -= 1
            counter += 1
        if self.rect.width < 15:
            self.rect.width = 15
            self.rect.height = 15


mysnake = Snake(100, 100, 20, 20, 2, "RIGHT")
myfood = Food(50, 50, 20, 20)