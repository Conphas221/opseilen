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
font = pygame.font.Font(None, 20)
largefont = pygame.font.Font(None, 90)
screen = pygame.display.set_mode(resolution) #sets the screen dimensions
pygame.display.set_caption('Opseilen!')



 



class turns:
    player1_name = ""
    player2_name = ""
    player3_name = ""
    player4_name = ""
    player_count = 0
    playerz = []
    current_player = 0
    current_player_name = ""
    match_started = False

    def turn():
        if turns.current_player < turns.player_count:
           turns.current_player += 1
           
        else:
            turns.current_player = 1
        turns.current_player_name = turns.playerz[turns.current_player-1]
        time.sleep(0.15)
    def firstturn(n):
        if n == 1:
            turns.current_player = 0
        if n == 2:
            turns.current_player = 1
        if n == 3:
            turns.current_player = 2
        if n == 4:
            turns.current_player = 3
        turns.turn()
        turns.match_started = True

    def naming(nr):
        if nr == 1:
            turns.player1_name = str(inputbox.ask(screen,  'Enter player 1 name'))
            turns.player_count += 1
            list_player1name = [turns.player1_name]
            turns.playerz.extend(list_player1name)
            #turns.current_player = 1
        elif nr == 2:
            turns.player2_name = str(inputbox.ask(screen,  'Enter player 2 name'))
            turns.player_count += 1
            list_player2name = [turns.player2_name]
            turns.playerz.extend(list_player2name)
            #turns.current_player = 2
        elif nr == 3:
            turns.player3_name = str(inputbox.ask(screen,  'Enter player 3 name'))
            turns.player_count += 1
            list_player3name = [turns.player3_name]
            turns.playerz.extend(list_player3name)
            #turns.current_player = 3
        elif nr == 4:
            turns.player4_name = str(inputbox.ask(screen,  'Enter player 4 name'))
            turns.player_count += 1
            list_player4name = [turns.player4_name]
            turns.playerz.extend(list_player4name)
            #turns.current_player = 4

        
#class Rects():
    
#    def __init__(self,game):
#        self.Game = game

#    def draw(self,screen):
#        mc_button = pygame.draw.rect(screen,purple,(0.0*self.Game.width,0.1*self.Game.height,0.3*self.Game.width,25)) # mc question button
#        open_button = pygame.draw.rect(screen,green,(0.0*self.Game.width,0.2*self.Game.height,0.3*self.Game.width,25)) #open question button
#        quit_button = pygame.draw.rect(screen,blue,(0.0*self.Game.width,0.3*self.Game.height,0.3*self.Game.width,25)) #place to draw quit button (quit doesn't work yet)
#        dice_button = pygame.draw.rect(screen,red,(0.0*self.Game.width,0.4*self.Game.height,0.3*self.Game.width,25)) #place to draw button to roll a die
#        quest_field = pygame.draw.rect(screen,black,(0.0*self.Game.width,0.6*self.Game.height,0.4*self.Game.width,25)) # place to draw question
#        mc_field = pygame.draw.rect(screen,black,(0.0*self.Game.width,0.7*self.Game.height,0.4*self.Game.width,25)) #place to draw mc options
#        was_question_correct_rect = pygame.draw.rect(screen,black,(0.0*self.Game.width,0.8*self.Game.height,0.4*self.Game.width,25))  #place to draw "wrong answer' or 'correct' message
#    def update():
        
#        pos = pygame.mouse.get_pos()
#        if  globalz.dice_button.collidepoint(pos):    
#            random1 = str(random.randint(1,6))
#            print(random1)




def music(): #start music function   
    pygame.mixer.music.load('background.mp3')#specifies music file
    pygame.mixer.music.play(-1) #loops forever
def stop_music():#stop music function
    pygame.mixer.music.stop()




class dice:
    dice_result = 0
    def dice_roll():
        dice.dice_result = random.randint(1,6)


class questions:
    correct = 2
    player1_correct = 2
    player2_correct = 2
    player3_correct = 2
    player4_correct = 2
    pressed = False
    def question_mc(cat,ori_cat,ans_cat):
        question = random.choice(cat) #takes a random question from the corresponding list
        screen.blit(font.render(question,True,(255,255,255)),(0*width,5)) #draws the question
        screen.blit(font.render(str(ans_cat),True,(255,255,255)),(0.6*width,5)) #draws the options
        pygame.display.update(globalz.quest_field) #displays the question
        pygame.display.update(globalz.mc_field) #displays the options
        answer = str(inputbox.ask(screen,  'Enter a, b, or c.')) #asks for the answer
        answer = [answer] #transforms the answer to a list
        question = [question] #transforms the question to a list
        question.extend(answer) #adds the question and answer to check if it is correct
        if question in ori_cat: #checks if the question + answer is correct by comparing it to the correct question+answer pairs
            questions.correct = 1
            if turns.current_player == 1:
                questions.player1_correct = 1
            elif turns.current_player == 2:
                questions.player2_correct = 1
            elif turns.current_player == 3:
                questions.player3_correct = 1
            elif turns.current_player == 4:
                questions.player4_correct = 1
            questions.pressed = True
        else:
            questions.correct = 0
            if turns.current_player == 1:
                questions.player1_correct = 0
            elif turns.current_player == 2:
                questions.player2_correct = 0
            elif turns.current_player == 3:
                questions.player3_correct = 0
            elif turns.current_player == 4:
                questions.player4_correct = 0
            questions.pressed = True


    def question_open(cat,ori_cat,keys):
        question = random.choice(cat) #to get a random question from the corresponding list
        screen.blit(font.render(question,True,(255,255,255)),(0.0*width,5)) #to draw the question
        pygame.display.update(globalz.quest_field) #to display the question
        answer = str(inputbox.ask(screen, "Give your answer!")) #asks for answer
        answers = answer
        answer = [answer] #transforms answer to list 
        question = [question] #transforms question to list
        question.extend(answer) #adds question and answer together
        key_words = keys
        if question in ori_cat: #checks if the answer is correct
            questions.correct = 1
            if turns.current_player == 1:
                questions.player1_correct = 1
            elif turns.current_player == 2:
                questions.player2_correct = 1
            elif turns.current_player == 3:
                questions.player3_correct = 1
            elif turns.current_player == 4:
                questions.player4_correct = 1
            questions.pressed = True
        elif any(i in key_words for i in answers.split()):
            questions.correct = 1
            if turns.current_player == 1:
                questions.player1_correct = 1
            elif turns.current_player == 2:
                questions.player2_correct = 1
            elif turns.current_player == 3:
                questions.player3_correct = 1
            elif turns.current_player == 4:
                questions.player4_correct = 1
            questions.pressed = True
        else:
            questions.correct = 0
            if turns.current_player == 1:
                questions.player1_correct = 0
            elif turns.current_player == 2:
                questions.player2_correct = 0
            elif turns.current_player == 3:
                questions.player3_correct = 0
            elif turns.current_player == 4:
                questions.player4_correct = 0
            questions.pressed = True