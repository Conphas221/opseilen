import pygame, math, sys, random, time
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


def buttons_menu():
    play_button = pygame.draw.rect(100,100,50,25)




def dice_roll():
    #screen.fill(black)
    dice_result = font.render(str(random.randint(2,12)),1,purple)
    screen.blit(dice_result,(0.95*width,0.05*higth))



def music(): #start music function   
    pygame.mixer.music.load('background.mp3')#specifies music file
    pygame.mixer.music.play(-1) #loops forever
def stop_music():#stop music function
    pygame.mixer.music.stop()

def draw():
    screen.fill(black)
    buttons_menu
    dice_roll
    pygame.display.flip()


def homescreen():
    running = True
    while running: #homescreen loop
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: #quits the game if you press the red button
                pygame.quit()
                sys.exit()
        draw




homescreen()
