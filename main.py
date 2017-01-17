import pygame, math, sys
width = 1024
higth = 768
resolution = (width,higth)
red = (255,0,0) #configures some colors
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)
pygame.init() # makes pygame work
screen = pygame.display.set_mode(resolution) #sets the screen dimensions

pygame.display.set_caption('Opseilen!')
while True: # main game loop
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: #quits the game if you press the red button
            pygame.quit()
            sys.exit()
    
    pygame.display.flip()