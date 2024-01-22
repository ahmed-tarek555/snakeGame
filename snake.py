import pygame
import random


class Snake:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def eat(self):
        if self.rect.colliderect(myfood.rect):
            if self.rect.width < 400:
                self.rect.width += 50
                self.rect.height += 50
            else:
                self.rect.width -= 50
                self.rect.height -= 50


class Food:
    def __init__(self, x, y, width, length):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, width, length)
        self.width = width
        self.length = length
        self.rect = pygame.Rect(self.x, self.y, width, length)

    def respawn(self):
        if self.rect.colliderect(mysnake.rect):
            self.rect.x = random.randint(0, 1000)
            self.rect.y = random.randint(0, 600)

mysnake = Snake(100, 100, 30, 30, 10)
myfood = Food(50, 50, 20, 20)
