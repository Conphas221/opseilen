import pygame
import sys
import os
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600, 600))

# zorgt dat quit makkelijker kan worden opgeroepen
def quitgame():
    pygame.quit()
    quit()

class Empty:
        def __init__(self):
                self.IsEmpty = True
empty = Empty()


class Node:
        def __init__(self, value, tail):
                self.IsEmpty = False
                self.Value = value
                self.Tail = tail

#Main menu screen
class MainMenu:

    hovered = False
    
    def __init__(self, text, pos, screen, callback):
        
        self.text = text
        self.pos = pos
        self.set_rect()
        self.callback = callback
        
        self.screen = screen
        
        self.caption = pygame.display.set_caption('MAIN MENU')

        self.font = pygame.font.Font(None, 30)
        
        #slaat background foto op
        self.image = pygame.image.load(os.path.join('/Users/emmadrost/Documents/PROJECT2/opseilen/project2/euromast1.bmp'))


    def draw(self):
        self.set_rend()
        self.screen.blit(self.rend, self.rect)

    def set_rend(self):
        self.rend = (pygame.font.Font(None, 30)).render(self.text, 1, self.get_color())
        
    def get_color(self):
        if self.hovered:
            return (255, 255, 0)
        else:
            return (130, 130, 130)
        
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

    #positie van muis op de buttons, zodat op alle delen van woorden te klikken is
    def click(self, pos):
        if pos[0] >= self.pos[0] and pos[0] <= self.pos[0] + 130:
            if pos[1] >= self.pos[1] and pos[1] <= self.pos[1] + 20: 
                self.callback()

    def update(self):
        pass

# Buttons pressed
def OnStartPressed():
    print("open game")
    import main
    import game
    import globalz
    import math
    main
    # scherm dat aantal spelers input opend.... # game.Game()
    pass

def OnHighscorePressed():
    print("open highscore")
    pass

def OnSpelregelsPressed():
    print("open spelregels")
    import LinkNaarRules
    #while True:
     #  for LinkNaarRules in MainMenu:
      #     if 
       # if MainMenu:
        #    mainmenu_draw
        #else:
           # LinkNaarRules
    
    pass

def OnQuitPressed():
    print("stop game")
    quit()
    pass 

game_options = [MainMenu("START GAME", (50, 80), screen, OnStartPressed), 
                    MainMenu("HIGH SCORE", (50, 160), screen, OnHighscorePressed),
                    MainMenu("SPELREGLES", (50, 240), screen, OnSpelregelsPressed), 
                    MainMenu("QUIT GAME", (50, 320), screen, OnQuitPressed)]

def mainmenu_draw():
    for option in game_options:
        if option.rect.collidepoint(event.pos):
            option.hovered = True
        else:
            option.hovered = False
        option.draw()


while True:
    pygame.event.pump()
    screen.fill((0,0,0))    
    #roept background op while true
    screen.blit(pygame.image.load(os.path.join('/Users/emmadrost/Documents/PROJECT2/opseilen/project2/euromast1.bmp')),(0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for option in game_options:
                    option.click(event.pos)
        elif event.type == pygame.MOUSEMOTION:
            mainmenu_draw()
            pygame.display.update()
            pygame.display.flip()


def program():
    mainmenu = MainMenu()
    mainmenu.program_loop()

program()




