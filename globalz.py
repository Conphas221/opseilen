import pygame, math, sys, random, time, string, inputbox, os, other, tower
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
#screen == pygame.display.set_mode((1366,768))


mc_button = pygame.draw.rect(screen,purple,(0.1*width,0.1*higth,0.3*width,25)) # mc question button
open_button = pygame.draw.rect(screen,green,(0.1*width,0.2*higth,0.3*width,25)) #open question button
quit_button = pygame.draw.rect(screen,blue,(0.1*width,0.3*higth,0.3*width,25)) #place to draw quit button (quit doesn't work yet)
dice_button = pygame.draw.rect(screen,red,(0.1*width,0.4*higth,0.3*width,25)) #place to draw button to roll a die
quest_field = pygame.draw.rect(screen,black,(0.1*width,0.6*higth,0.4*width,25)) # place to draw question
mc_field = pygame.draw.rect(screen,black,(0.1*width,0.7*higth,0.4*width,25)) #place to draw mc options
was_question_correct_rect = pygame.draw.rect(screen,black,(0.1*width,0.8*higth,0.4*width,25))  #place to draw "wrong answer' or 'correct' message
