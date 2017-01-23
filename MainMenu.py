import pygame, math, sys, random, time, string, os
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
        mc_button = pygame.draw.rect(screen,blue,(0.1*self.Mainmenu.width,0.1*self.Mainmenu.height,0.3*self.Mainmenu.width,25)) # mc question button
        open_button = pygame.draw.rect(screen,blue,(0.1*self.Mainmenu.width,0.2*self.Mainmenu.height,0.3*self.Mainmenu.width,25)) #open question button
        quit_button = pygame.draw.rect(screen,blue,(0.1*self.Mainmenu.width,0.3*self.Mainmenu.height,0.3*self.Mainmenu.width,25)) #place to draw quit button (quit doesn't work yet)
        dice_button = pygame.draw.rect(screen,blue,(0.1*self.Mainmenu.width,0.4*self.Mainmenu.height,0.3*self.Mainmenu.width,25)) #place to draw button to roll a die
        quest_field = pygame.draw.rect(screen,blue,(0.1*self.Mainmenu.width,0.6*self.Mainmenu.height,0.4*self.Mainmenu.width,25)) # place to draw question
        mc_field = pygame.draw.rect(screen,blue,(0.1*self.Mainmenu.width,0.7*self.Mainmenu.height,0.4*self.Mainmenu.width,25)) #place to draw mc options
        rules_button = pygame.draw.rect(screen,blue,(0.1*self.Mainmenu.width,0.8*self.Mainmenu.height,0.3*self.Mainmenu.width,25))
        was_question_correct_rect = pygame.draw.rect(screen,black,(0.1*self.Mainmenu.width,0.8*self.Mainmenu.height,0.4*self.Mainmenu.width,25))  #place to draw "wrong answer' or 'correct' message
        

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





        
