import pygame, math, sys, random, time, string, inputbox, os
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
 #random1 = str(random.randint(1,6))   this line rolls the die

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



ori_mc_sport = [['Welke manier van sport word het meest beoefend in Rotterdam?','a']]
ori_o_sport = [['Hoe heet het centrum voor sport naast de Kuip?','topsportcentrum rotterdam']]
ori_mc_history = [['Wat was tijdens de Tweede Wereldoorlog de enige weg naar het centrum die de Duitsers probeerden te bereiken?','b']]
ori_o_history = [['Waar staat de afkorting van de krant NRC voor?','nieuwe rotterdamsche courant']]
ori_mc_entert = [['Hoe heet de culturele en culinaire ontdekkingstocht door Rotterdam?','c']]
ori_o_entert = [['Welk kunstwerk wordt ook wel de Nederlandse versie van de Sixtijnse Kapel genoemd?','de markthal']]
ori_mc_geo = [['Wat is de oudste brug van Rotterdam?','b']]
ori_o_geo = [['Hoe heten de bekendste huizen van Rotterdam?','de kubuswoningen']]


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
mc_button = pygame.draw.rect(screen,purple,(0.1*width,0.1*higth,0.3*width,25))
open_button = pygame.draw.rect(screen,green,(0.1*width,0.2*higth,0.3*width,25))
quit_button = pygame.draw.rect(screen,blue,(0.1*width,0.3*higth,0.3*width,25))
dice_button = pygame.draw.rect(screen,red,(0.1*width,0.4*higth,0.3*width,25))
    


def music(): #start music function   
    pygame.mixer.music.load('background.mp3')#specifies music file
    pygame.mixer.music.play(-1) #loops forever
def stop_music():#stop music function
    pygame.mixer.music.stop()





def homescreen():
    running = True
    random1 = ""
    answ = ""
    quest = ""
    given_answer = ""
    ask_quest_cat = ""
    score = int(0)
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
                        question = random.choice(o_sport)
                        print(question)
                        answer = str(inputbox.ask(screen, "Give your answer!"))
                        answer = [answer]
                        question = [question]
                        question.extend(answer)
                        if question in ori_o_sport:
                             score += 100
                        else:
                            print("Wrong answer!")
                    elif ask_quest_cat == "2":
                        question = random.choice(o_entert)
                        print(question)
                        answer = str(inputbox.ask(screen, "Give your answer!"))
                        answer = [answer]
                        question = [question]
                        question.extend(answer)
                        if question in ori_o_entert:
                             score += 100
                        else:
                            print("Wrong answer!")
                    elif ask_quest_cat == "3":
                        question = random.choice(o_history)
                        print(question)
                        answer = str(inputbox.ask(screen, "Give your answer!"))
                        answer = [answer]
                        question = [question]
                        question.extend(answer)
                        if question in ori_o_history:
                             score += 100
                        else:
                            print("Wrong answer!")
                    elif ask_quest_cat == "4":
                        question = random.choice(o_geo)
                        print(question)
                        answer = str(inputbox.ask(screen, "Give your answer!"))
                        answer = [answer]
                        question = [question]
                        question.extend(answer)
                        if question in ori_o_geo:
                             score += 100
                        else:
                            print("Wrong answer!")
                   
                    #if answer == "a":
                    #    score += 100
                    #else:
                    #    print("Wrong answer!")
                elif mc_button.collidepoint(pos):
                    ask_quest_cat = str(inputbox.ask(screen,'enter 1 for sport, 2 for entertainment, 3 for history or 4 for geography'))
                    if ask_quest_cat == "1":
                        question = random.choice(mc_sport)
                        print(question)
                        answer = str(inputbox.ask(screen,  'Enter a for A, b for B or c for C.'))
                        answer = [answer]
                        question = [question]
                        question.extend(answer)
                        if question in ori_mc_sport:
                             score += 100
                        else:
                            print("Wrong answer!")
                    elif ask_quest_cat == "2":
                        question = random.choice(mc_entert)
                        print(question)
                        answer = str(inputbox.ask(screen,  'Enter a for A, b for B or c for C.'))
                        answer = [answer]
                        question = [question]
                        question.extend(answer)
                        if question in ori_mc_entert:
                             score += 100
                        else:
                            print("Wrong answer!")
                    elif ask_quest_cat == "3":
                        question = random.choice(mc_history)
                        print(question)
                        answer = str(inputbox.ask(screen,  'Enter a for A, b for B or c for C.'))
                        answer = [answer]
                        question = [question]
                        question.extend(answer)
                        if question in ori_mc_history:
                             score += 100
                        else:
                            print("Wrong answer!")
                    elif ask_quest_cat == "4":
                        question = random.choice(mc_geo)
                        print(question)
                        answer = str(inputbox.ask(screen,  'Enter a for A, b for B or c for C.'))
                        answer = [answer]
                        question = [question]
                        question.extend(answer)
                        if question in ori_mc_geo:
                             score += 100
                        else:
                            print("Wrong answer!")
                elif dice_button.collidepoint(pos):    
                    random1 = str(random.randint(1,6))
        score_result = font.render((str(score)),1,yellow)
        screen.blit(score_result,(0.05*width,0.95*higth))
        screen.blit(font.render('Roll the die',True,(255,255,255)),(0.1*width,0.4*higth))
        screen.blit(font.render('Multiple choice question',True,(255,255,255)),(0.1*width,0.1*higth))
        screen.blit(font.render('Open question',True,(255,255,255)),(0.1*width,0.2*higth))
        screen.blit(font.render(answ,True,(255,255,255)),(0.1*width,0.5*higth))
        dice_result = font.render((random1),1,yellow)
        screen.blit(dice_result,(0.95*width,0.05*higth))
        pygame.display.flip()


homescreen()
