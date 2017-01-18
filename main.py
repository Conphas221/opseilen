import pygame, math, sys, random, time, string, inputbox
from pygame.locals import *
pygame.init() # makes pygame work
width = 800
higth = 600
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


#inp = str(inputbox.ask(screen, 'Message'))   input fuction
                  #  print(inp)

mc_sport = ['Welke manier van sport word het meest beoefend in Rotterdam?']
o_sport = ['Hoe heet het centrum voor sport naast de Kuip?']
mc_history = ['Wat was tijdens de Tweede Wereldoorlog de enige weg naar het centrum die de Duitsers probeerden te bereiken?']
o_history = ['Waar staat de afkorting van de krant NRC voor?']
mc_entert = ['Hoe heet de culturele en culinaire ontdekkingstocht door Rotterdam?']
o_entert = ['Welk kunstwerk wordt ook wel de Nederlandse versie van de Sixtijnse Kapel genoemd?']
mc_geo = ['Wat is de oudste brug van Rotterdam?']
o_geo = ['Hoe heten de bekendste huizen van Rotterdam?']
random.shuffle(mc_sport)


ori_mc_sport = [['Welke manier van sport word het meest beoefend in Rotterdam?','A.Fitness']]
ori_o_sport = [['Hoe heet het centrum voor sport naast de Kuip?','Topsportcentrum Rotterdam']]
ori_mc_history = [['Wat was tijdens de Tweede Wereldoorlog de enige weg naar het centrum die de Duitsers probeerden te bereiken?','B.Maasbrug']]
ori_o_history = [['Waar staat de afkorting van de krant NRC voor?','Nieuwe Rotterdamsche Courant']]
ori_mc_entert = [['Hoe heet de culturele en culinaire ontdekkingstocht door Rotterdam?','C.Bike&Bite']]
ori_o_entert = [['Welk kunstwerk wordt ook wel de Nederlandse versie van de Sixtijnse Kapel genoemd?','De Markthal']]
ori_mc_geo = [['Wat is de oudste brug van Rotterdam?','B.De Koninginnebrug']]
ori_o_geo = [['Hoe heten de bekendste huizen van Rotterdam?','De Kubuswoningen']]


ans_mc_sport = [['A.Fitness','B.Voetbal','C.Basketbal']]
ans_o_sport = []
ans_mc_history = [['A.De Nieuwe Binnenweg','B.Maasbrug','C.Koninginnenbrug']]
ans_o_history = []
ans_mc_entert = [['A.Drive&Eat','B.Bicycle Dinner','C.Bike&Bite']]
ans_o_entert = []
ans_mc_geo = [['A.De Willemsbrug','B.De Koninginnebrug','C.De van Briennenoordbrug']]
ans_o_geo = []


given_answers = []







def buttons_menu(): #makes drawing easier
    play_button = pygame.draw.rect(screen,purple,(0.1*width,0.1*higth,0.3*width,25))
    instr_button = pygame.draw.rect(screen,green,(0.1*width,0.2*higth,0.3*width,25))
    quit_button = pygame.draw.rect(screen,blue,(0.1*width,0.3*higth,0.3*width,25))
    dice_button = pygame.draw.rect(screen,red,(0.1*width,0.4*higth,0.3*width,25))

#initializes rectangle coords
play_button = pygame.draw.rect(screen,purple,(0.1*width,0.1*higth,0.3*width,25))
instr_button = pygame.draw.rect(screen,green,(0.1*width,0.2*higth,0.3*width,25))
quit_button = pygame.draw.rect(screen,blue,(0.1*width,0.3*higth,0.3*width,25))
dice_button = pygame.draw.rect(screen,red,(0.1*width,0.4*higth,0.3*width,25))
    


def music(): #start music function   
    pygame.mixer.music.load('background.mp3')#specifies music file
    pygame.mixer.music.play(-1) #loops forever
def stop_music():#stop music function
    pygame.mixer.music.stop()




#dice_result = font.render((random1),1,yellow)
#screen.blit(dice_result,(0.95*width,0.05*higth))
def homescreen():
    running = True
    random1 = ""
    score = int(0)
    while running: #homescreen loop
        screen.fill(black)
        buttons_menu()  
        for event in pygame.event.get(): 
            
            if event.type == pygame.QUIT: #quits the game if you press the red button
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if play_button.collidepoint(pos):
                    print(mc_sport[0])
                    print(ans_mc_sport)
                    answer = str(inputbox.ask(screen, 'Enter a for A, b for B or c for C.'))
                    
                    random1 = str(random.randint(1,6))
                    if answer == "a":
                        score += 100
        score_result = font.render((str(score)),1,yellow)
        screen.blit(score_result,(0.05*width,0.95*higth))
        dice_result = font.render((random1),1,yellow)
        screen.blit(dice_result,(0.95*width,0.05*higth))
        pygame.display.flip()


homescreen()
