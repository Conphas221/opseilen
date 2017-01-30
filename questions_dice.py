import pygame, math, sys, random, time, string, inputbox, os
from pygame.locals import *
pygame.init() # makes pygame work
width = 800
higth = 600
resolution = (width,higth)

							#old colors
red = (255, 99, 71) 		#(255,0,0) # Configures some colors
green = (50, 205, 50) 		#(0,255,0)
blue =  (65, 105, 225) 		#(0,0,255)
white = (255,255,255)
black = (0,0,0)
yellow = (230, 230, 0)
purple = (95,158,160)       #purple = (153,0,153)

font = pygame.font.Font(None, 30)
largefont = pygame.font.Font(None, 90)
screen = pygame.display.set_mode(resolution) #sets the screen dimensions
pygame.display.set_caption('Opseilen!')
score = int(0)
correct = 2
#inp = str(inputbox.ask(screen, 'Message'))   input fuction from inputbox
                

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
ans_o_sport = [['topsportcentrum rotterdam']]
ans_mc_history = [['A.De Nieuwe Binnenweg','B.Maasbrug','C.Koninginnenbrug']]
ans_o_history = [['Nieuwe Rotterdamsche Courant']]
ans_mc_entert = [['A.Drive&Eat','B.Bicycle Dinner','C.Bike&Bite']]
ans_o_entert = [['De Markthal']]
ans_mc_geo = [['A.De Willemsbrug','B.De Koninginnebrug','C.De van Briennenoordbrug']]
ans_o_geo = [['De kubuswoningen']]







def buttons_menu(): #makes drawing easier
    mc_button = pygame.draw.rect(screen,purple,(0.1*width,0.1*higth,0.3*width,25))
    open_button = pygame.draw.rect(screen,green,(0.1*width,0.2*higth,0.3*width,25))
    quit_button = pygame.draw.rect(screen,blue,(0.1*width,0.3*higth,0.3*width,25))
    dice_button = pygame.draw.rect(screen,red,(0.1*width,0.4*higth,0.3*width,25))
    

#initializes rectangle coords
mc_button = pygame.draw.rect(screen,purple,(0.1*width,0.1*higth,0.3*width,25)) # mc question button
open_button = pygame.draw.rect(screen,green,(0.1*width,0.2*higth,0.3*width,25)) #open question button
quit_button = pygame.draw.rect(screen,blue,(0.1*width,0.3*higth,0.3*width,25)) #place to draw quit button (quit doesn't work yet)
dice_button = pygame.draw.rect(screen,red,(0.1*width,0.4*higth,0.3*width,25)) #place to draw button to roll a die
quest_field = pygame.draw.rect(screen,black,(0.1*width,0.6*higth,0.4*width,25)) # place to draw question
mc_field = pygame.draw.rect(screen,black,(0.1*width,0.7*higth,0.4*width,25)) #place to draw mc options
was_question_correct_rect = pygame.draw.rect(screen,black,(0.1*width,0.8*higth,0.4*width,25))  #place to draw "wrong answer' or 'correct' message


def music(): #start music function   
    pygame.mixer.music.load('background.mp3')#specifies music file
    pygame.mixer.music.play(-1) #loops forever
def stop_music():#stop music function
    pygame.mixer.music.stop()


def question_open(cat,ori_cat):
    global score #needed to avoid error
    global correct
    question = random.choice(cat) #to get a random question from the corresponding list
    screen.blit(font.render(question,True,(255,255,255)),(0.1*width,0.6*higth)) #to draw the question
    pygame.display.update(quest_field) #to display the question
    answer = str(inputbox.ask(screen, "Give your answer!")) #asks for answer
    answer = [answer] #transforms answer to list 
    question = [question] #transforms question to list
    question.extend(answer) #adds question and answer together
    if question in ori_cat: #checks if the answer is correct
        score += 100
        correct = 1
    else:
        correct = 0

def question_mc(cat,ans_cat,ori_cat):
    global score #needed to avoid error
    global correct
    question = random.choice(cat) #takes a random question from the corresponding list
    screen.blit(font.render(question,True,(255,255,255)),(0.1*width,0.6*higth)) #draws the question
    screen.blit(font.render(str(ans_cat),True,(255,255,255)),(0.1*width,0.7*higth)) #draws the options
    pygame.display.update(quest_field) #displays the question
    pygame.display.update(mc_field) #displays the options
    answer = str(inputbox.ask(screen,  'Enter a, b, or c.')) #asks for the answer
    answer = [answer] #transforms the answer to a list
    question = [question] #transforms the question to a list
    question.extend(answer) #adds the question and answer to check if it is correct
    if question in ori_cat: #checks if the question + answer is correct by comparing it to the correct question+answer pairs
        score += 100
        correct = 1
    else:
        correct = 0


def homescreen(): 
    running = True
    random1 = "" #needed for the die
    quest = "" 
    ask_quest_cat = "" #needed to let questions work
    global correct
    global score # needed to avoid error

    #player1 = str(inputbox.ask(screen, "enter name for player1"))
    #player2 = str(inputbox.ask(screen, "enter name for player2"))
    #player3 = str(inputbox.ask(screen, "enter name for player3"))
    #player4 = str(inputbox.ask(screen, "enter name for player4"))

    while running: #homescreen loop
        screen.fill(black)
        buttons_menu()  
        for event in pygame.event.get(): 
            
            if event.type == pygame.QUIT: #quits the game if you press the red button
                pygame.quit()
                sys.exit()
                os._exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if open_button.collidepoint(pos):
                    ask_quest_cat = str(inputbox.ask(screen,'enter 1 for sport, 2 for entertainment, 3 for history or 4 for geography'))
                    if ask_quest_cat == "1":
                        question_open(o_sport,ori_o_sport)
                    elif ask_quest_cat == "2":
                        question_open(o_entert,ori_o_entert)
                    elif ask_quest_cat == "3":
                        question_open(o_history,ori_o_history)
                    elif ask_quest_cat == "4":
                        question_open(o_geo,ori_o_geo)
                   
                    #if answer == "a":
                    #    score += 100
                    #else:
                    #    print("Wrong answer!")
                elif mc_button.collidepoint(pos):
                    ask_quest_cat = str(inputbox.ask(screen,'enter 1 for sport, 2 for entertainment, 3 for history or 4 for geography'))
                    if ask_quest_cat == "1":
                        question_mc(mc_sport,ans_mc_sport,ori_mc_sport)
                    elif ask_quest_cat == "2":
                        question_mc(mc_entert,ans_mc_entert,ori_mc_entert)
                    elif ask_quest_cat == "3":
                        question_mc(mc_history,ans_mc_history,ori_mc_history)
                    elif ask_quest_cat == "4":
                        question_mc(mc_geo,ans_mc_geo,ori_mc_geo)
                elif dice_button.collidepoint(pos):    
                    random1 = str(random.randint(1,6))
        if correct == 1:
            screen.blit(font.render('Your answer is correct!',True,white),(0.1*width,0.8*higth))
        elif correct == 0:
            screen.blit(font.render('Your answer is wrong!',True,white),(0.1*width,0.8*higth))
        screen.blit(font.render(str(score),True,white),(0.05*width,0.95*higth))
        screen.blit(font.render('Roll the die',True,(255,255,255)),(0.1*width,0.4*higth))
        screen.blit(font.render('Multiple choice question',True,(255,255,255)),(0.1*width,0.1*higth))
        screen.blit(font.render('Open question',True,(255,255,255)),(0.1*width,0.2*higth))
        screen.blit(font.render(random1,True,(255,255,255)),(0.95*width,0.05*higth))
        pygame.display.flip()


homescreen()
