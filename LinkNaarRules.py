import pygame
import sys 
import os
from pygame.locals import *

pygame.init()

# Class spelregels openen
class spelregels:
    def open_spelregel(self, open1):
        self.open1 = img1

# Openen spelregels vanuit bestand (Emma's computer)

    img1 = pygame.image.load(os.path.join('/Users/emmadrost/Documents/PROJECT2/opseilen/Project2/spelregels.bmp'))

# W en H zijn juiste groote voor openen document 600-900
    white = (0, 0, 0)
    w = 600
    h = 900
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))
    running = True

# Openen scherm met spelregels
    while running:
        screen.fill((white))
        screen.blit(img1,(0,0))
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

