import pygame
import sys
import os
import main
import game

#from pygame.locals import *

#NO GGLOBAL VARIABLES

class Button:
    def __init__(self, text, x, y, action):
        self.X = x
        self.Y = y
        self.DefaultText = text
        self.Color = (130, 130, 130)
        self.Action = action

        self.Text = (pygame.font.Font(None, 30)).render(text, 1, self.Color)
        self.Rect = self.Text.get_rect()
        self.Rect.topleft = (x, y)

    def Update(self, events):
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                if self.Rect.collidepoint(event.pos):                    
                    self.Text = (pygame.font.Font(None, 30)).render(self.DefaultText, 1, (255,255,0))            
                else:
                    self.Text = (pygame.font.Font(None, 30)).render(self.DefaultText, 1, (130, 130, 130))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.Rect.collidepoint(event.pos):                    
                    return self.Action()
        return self
        
    def Draw(self, screen):
        screen.blit(self.Text, self.Rect)
        
class InstructionMenu:
    def __init__(self, width, height):
        self.Width = width
        self.Height = height        
        self.Image = pygame.image.load(os.path.join('/Users/emmadrost/Desktop/opseilen-Working-menu-2NEW/Project2/spelregels.bmp'))

        self.Buttons = [Button("Back", 10, 90, lambda : MainMenu(width, height))]
    def Update(self):
        events = pygame.event.get()
        for event in events:            
            if event.type == pygame.QUIT:
              sys.exit()
        for button in self.Buttons:
            res = button.Update(events)
            if (res != button):
                return res
        return self

    def Draw(self, screen):
        screen.blit(self.Image,(150, 50))
        for button in self.Buttons:
            button.Draw(screen)

class MainMenu:
    def __init__(self, width, height):
        self.Width = width
        self.Height = height        
        self.Image = pygame.image.load(os.path.join('/Users/emmadrost/Desktop/opseilen-Working-menu-2NEW/Project2/euromast1.bmp'))
        self.Buttons = [Button("Play", 10, 10, lambda : game.Game().program_loop()),
                        Button("Instructions", 10, 50, lambda : InstructionMenu(width, height)),
                        Button("Quit", 10, 90, lambda : sys.exit())]
    def Update(self):
        events = pygame.event.get()
        for event in events:            
            if event.type == pygame.QUIT:
              sys.exit()
        for button in self.Buttons:
            res = button.Update(events)
            if (res != button):
                return res
        return self

    def Draw(self, screen):
        screen.blit(self.Image,(150, 50))
        for button in self.Buttons:
            button.Draw(screen)



pygame.init()
width = 700
height = 800
screen = pygame.display.set_mode((width, height))
scene = MainMenu(width, height)
while True:
    pygame.event.pump()
    screen.fill((255,255,255))    

    scene = scene.Update()
    scene.Draw(screen)

    pygame.display.flip()


def program():
    mainmenu = MainMenuNew()
    mainmenu.program_loop()

program()
