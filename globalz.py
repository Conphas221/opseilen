import pygame, math, sys, random, time, string, inputbox, os, other, tower
from pygame.locals import *
pygame.init() # makes pygame work
width = 1366
higth = 768
resolution = (width,higth)
red = (255, 99, 71) #configures some colors
green = (50, 205, 50) 
blue = (65, 105, 225) 	
white = (255,255,255)
black = (0,0,0)
yellow = (230, 230, 0)
purple = (95,158,160)
font = pygame.font.Font(None, 20)
largefont = pygame.font.Font(None, 90)
screen = pygame.display.set_mode(resolution) #sets the screen dimensions
pygame.display.set_caption('Opseilen!')
#screen == pygame.display.set_mode((1366,768))


#mc_button = pygame.draw.rect(screen,purple,(0.1*width,0.1*higth,0.3*width,25)) # mc question button
#open_button = pygame.draw.rect(screen,green,(0.1*width,0.2*higth,0.3*width,25)) #open question button
#quit_button = pygame.draw.rect(screen,blue,(0.1*width,0.3*higth,0.3*width,25)) #place to draw quit button (quit doesn't work yet)
#dice_button = pygame.draw.rect(screen,red,(0.1*width,0.4*higth,0.3*width,25)) #place to draw button to roll a die
quest_field = pygame.draw.rect(screen,black,(0.0*width,0.0*higth,0.4*width,25)) # place to draw question
mc_field = pygame.draw.rect(screen,black,(0.6*width,0*higth,0.4*width,25)) #place to draw mc options
#was_question_correct_rect = pygame.draw.rect(screen,black,(0.1*width,0.8*higth,0.4*width,25))  #place to draw "wrong answer' or 'correct' message


#all questions
mc_sport = ['Welke manier van sport word het meest beoefend in Rotterdam?']
o_sport = ['Hoe heet het centrum voor sport naast de Kuip?']
mc_history = ['Wat was tijdens de Tweede Wereldoorlog de enige weg naar het centrum die de Duitsers probeerden te bereiken?']
o_history = ['Waar staat de afkorting van de krant NRC voor?']
mc_entert = ['Hoe heet de culturele en culinaire ontdekkingstocht door Rotterdam?']
o_entert = ['Welk kunstwerk wordt ook wel de Nederlandse versie van de Sixtijnse Kapel genoemd?']
mc_geo = ['Wat is de oudste brug van Rotterdam?']
o_geo = ['Hoe heten de bekendste huizen van Rotterdam?']


#question answer pairs to check if the answer is correct
ori_mc_sport = [['Welke manier van sport word het meest beoefend in Rotterdam?','a']]
ori_o_sport = [['Hoe heet het centrum voor sport naast de Kuip?','topsportcentrum rotterdam']]
ori_mc_history = [['Wat was tijdens de Tweede Wereldoorlog de enige weg naar het centrum die de Duitsers probeerden te bereiken?','b']]
ori_o_history = [['Waar staat de afkorting van de krant NRC voor?','nieuwe rotterdamsche courant']]
ori_mc_entert = [['Hoe heet de culturele en culinaire ontdekkingstocht door Rotterdam?','c']]
ori_o_entert = [['Welk kunstwerk wordt ook wel de Nederlandse versie van de Sixtijnse Kapel genoemd?','de markthal']]
ori_mc_geo = [['Wat is de oudste brug van Rotterdam?','b']]
ori_o_geo = [['Hoe heten de bekendste huizen van Rotterdam?','de kubuswoningen']]

#to display the answers
ans_mc_sport = [['A.Fitness','B.Voetbal','C.Basketbal']]
key_o_sport = (['topsportcentrum','topsport','rotterdam','centrum'])
ans_mc_history = [['A.De Nieuwe Binnenweg','B.Maasbrug','C.Koninginnenbrug']]
key_o_history = (['nieuwe','rotterdamsche','rotterdamse','courant'])
ans_mc_entert = [['A.Drive&Eat','B.Bicycle Dinner','C.Bike&Bite']]
key_o_entert = (['markt','hal','markthal'])
ans_mc_geo = [['A.De Willemsbrug','B.De Koninginnebrug','C.De van Briennenoordbrug']]
key_o_geo = (['kubuswoningen', 'woningen', 'kubus'])
