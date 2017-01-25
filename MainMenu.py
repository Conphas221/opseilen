import pygame
import math 
import sys
import random 
import string
import os 
import button
from pygame.locals import *

white = (255,255,255)
blue = (0, 0, 255)
black = (0, 0, 0)

class Empty:
        def __init__(self):
                self.IsEmpty = True
empty = Empty()


class Node:
        def __init__(self, value, tail):
                self.IsEmpty = False
                self.Value = value
                self.Tail = tail 


class MainMenu:
        def __init__(self):
                # Resolution
                self.width = 800
                self.height = 600
                self.resolution = (self.width,self.height)
                #self.fullscreen = pygame.FULLSCREEN

                pygame.init() # Makes pygame work

                # Set the resolution
                self.screen = pygame.display.set_mode(self.resolution)

                # Set Title
                self.caption = pygame.display.set_caption('Main Menu')

                # Set default font
                self.font = pygame.font.Font(None, 30)

                self.image = pygame.image.load(os.path.join('/Users/emmadrost/Documents/PROJECT2/opseilen/project2/euromast1.bmp'))

                
        def draw(self):
                self.screen.fill((212, 212, 212))
                
                self.screen.blit(self.image,(0, 0))


# draw's the buttons for main menu

                button.draw(self, 35, 40, 550, 35, "MAIN MENU", 28, (0, 0, 0), (255, 255, 255), lambda x: sys.exit())
                button.draw(self, 35, 120, 200, 35, "Start Game", 28, (0, 0, 255), (255, 255, 255), lambda x: sys.exit())
                button.draw(self, 35, 200, 200, 35, "High Score", 28, (0, 0, 255), (255, 255, 255), lambda x: sys.exit())
                button.draw(self, 35, 280, 200, 35, "Spelregels", 28, (0, 0, 255), (255, 255, 255), lambda x: sys.exit())
                button.draw(self, 35, 360, 200, 35, "Multiplayer", 28, (0, 0, 255), (255, 255, 255), lambda x: sys.exit())
                button.draw(self, 35, 440, 200, 35, "Quit Game", 28, (0, 0, 255), (255, 255, 255), lambda x: sys.exit())

                pygame.display.flip()


        def update(self):
            button.update(self)
            pass

        def program_loop(self):
                while not process_events():
                        self.update()
                        self.draw()
              
class Side:
        def __init__(self, color):
                self.Color = color
        def draw(self, screen, x1, y1, x2, y2):
                pygame.draw.rect(screen, self.Color, (int(x1), int(y1), int(x2), int(y2)))

class frontlayer1:
        def __init__(self, x1, y1, x2, y2):
                self.x1 = x1
                self.y1 = y1
                self.x2 = x2
                self.y2 = y2


        def update(self):
                return True

        def draw(self, screen):
                pygame.draw.rect(screen, white, (int(self.x1), int(self.y1), int(self.x2), int(self.y2)))

class frontlayer2:
        def __init__(self, x1, y1, x2, y2):
                self.x1 = x1
                self.y1 = y1
                self.x2 = x2
                self.y2 = y2

        def update(self):
                return True

        def draw(self, screen):
                pygame.draw.rect(screen, white, (int(self.x1), int(self.y1), int(self.x2), int(self.y2)))


def process_events():
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        sys.exit()
                elif event.type == pygame.MOUSEMOTION:
                        return False

# Main game logic
def program():
        mainmenu = MainMenu()
        mainmenu.program_loop()

# Starts program
program()

