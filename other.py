import pygame, math, sys, random, time, string, inputbox, os, tower, globalz
from pygame.locals import *
pygame.init() # makes pygame work
width = 1366
higth = 768
resolution = (width,higth)
red = (255,0,0) #configures some colors
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)
purple = (153,0,153)
font = pygame.font.Font(None, 30)
largefont = pygame.font.Font(None, 90)
screen = pygame.display.set_mode(resolution) #sets the screen dimensions
pygame.display.set_caption('Opseilen!')

class Rects():
    
    def __init__(self,game):
        self.Game = game

    def draw(self,screen):
        mc_button = pygame.draw.rect(screen,purple,(0.0*self.Game.width,0.1*self.Game.height,0.3*self.Game.width,25)) # mc question button
        open_button = pygame.draw.rect(screen,green,(0.0*self.Game.width,0.2*self.Game.height,0.3*self.Game.width,25)) #open question button
        quit_button = pygame.draw.rect(screen,blue,(0.0*self.Game.width,0.3*self.Game.height,0.3*self.Game.width,25)) #place to draw quit button (quit doesn't work yet)
        dice_button = pygame.draw.rect(screen,red,(0.0*self.Game.width,0.4*self.Game.height,0.3*self.Game.width,25)) #place to draw button to roll a die
        quest_field = pygame.draw.rect(screen,black,(0.0*self.Game.width,0.6*self.Game.height,0.4*self.Game.width,25)) # place to draw question
        mc_field = pygame.draw.rect(screen,black,(0.0*self.Game.width,0.7*self.Game.height,0.4*self.Game.width,25)) #place to draw mc options
        was_question_correct_rect = pygame.draw.rect(screen,black,(0.0*self.Game.width,0.8*self.Game.height,0.4*self.Game.width,25))  #place to draw "wrong answer' or 'correct' message
    def update():
        
        pos = pygame.mouse.get_pos()
        if  globalz.dice_button.collidepoint(pos):    
            random1 = str(random.randint(1,6))
            print(random1)
