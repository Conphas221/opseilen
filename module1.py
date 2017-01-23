import pygame, math, sys, random, time, string, inputbox, os
from pygame.locals import *

class Game:
    def __init__(self):
        width = 800
        higth = 600
        resolution = (width,higth)
        pygame.init
     
        self.screen = pygame.display.set_mode(resolution)
        
      
        self.font = pygame.font.Font(None, 30)

