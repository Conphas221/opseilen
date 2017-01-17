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
    

def dice_roll(): #rolls a pair of dice and gives you the result
    dice_result = font.render(str(random.randint(2,12)),1,yellow)
    screen.blit(dice_result,(0.95*width,0.05*higth))



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
                    print("LOL")
                    random1 = str(random.randint(2,12))
        dice_result = font.render((random1),1,yellow)
        screen.blit(dice_result,(0.95*width,0.05*higth))
        pygame.display.flip()


homescreen()
