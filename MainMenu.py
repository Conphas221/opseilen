import pygame, math, sys, random, time, string, os, pygame.font, pygame.event, pygame.draw, string, inputbox, button
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

                self.Rects = Rects(self)


        def draw(self):
            self.screen.fill((212, 212, 212))
            image = pygame.image.load(os.path.join('/Users/emmadrost/Documents/Development/python/euromast1.bmp'))
            self.screen.blit(image,(0, 0))
            self.Rects.draw(self.screen)

            button.draw(self, 32, 32, 100, 32, "banaan", 20, (0, 0, 0), (255,255,255), lambda game: sys.exit())

            pygame.display.flip()

        def update(self):
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


class Rects:
    def __init__(self,mainmenu):
        self.Mainmenu = mainmenu
    def draw(self,screen):
        start_button = pygame.draw.rect(screen,blue,(0.1*self.Mainmenu.width,0.1*self.Mainmenu.height,0.3*self.Mainmenu.width,25)) # start
        highscore_button = pygame.draw.rect(screen,blue,(0.1*self.Mainmenu.width,0.2*self.Mainmenu.height,0.3*self.Mainmenu.width,25)) #high score
        spelregels_button = pygame.draw.rect(screen,blue,(0.1*self.Mainmenu.width,0.3*self.Mainmenu.height,0.3*self.Mainmenu.width,25)) #spelregels
        multiplayer_button = pygame.draw.rect(screen,blue,(0.1*self.Mainmenu.width,0.4*self.Mainmenu.height,0.3*self.Mainmenu.width,25)) #multiplayer
        quit_button = pygame.draw.rect(screen,blue,(0.1*self.Mainmenu.width,0.5*self.Mainmenu.height,0.3*self.Mainmenu.width,25)) # quit
        

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
        return False


# Main game logic
def program():
        mainmenu = MainMenu()
        mainmenu.program_loop()

# Starts program
program()


#CODE TO --> WINDOW CLOSES AND GAME STARTS
#def startGame:
#        if buttonPressed = True:
#                screen.fil(256, 256, 256)
#    else:
#        screen.blit(buttonImage, (x, y)