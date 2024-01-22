# import pygame
# from snake import mysnake
# import random
#
# class Food:
#     def __init__(self, x, y, width, length):
#         self.x = x
#         self.y = y
#         self.rect = pygame.Rect(x, y, width, length)
#         self.width = width
#         self.length = length
#         self.rect = pygame.Rect(self.x, self.y, width, length)
#
#     def respawn(self):
#         if self.rect.colliderect(mysnake.rect):
#             self.rect.x = random.randint(0, 1000)
#             self.rect.y = random.randint(0, 600)
#
#
# myfood = Food(50, 50, 20, 20)
