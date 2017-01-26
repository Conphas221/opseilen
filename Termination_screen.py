import pygame
import math

#colors
white = (255,255,255)
blue = (0, 0, 255)
black = (0, 0, 0)

class Empty:
        def __init__(self):
                self.IsEmpty = True
empty = Empty()


class Node:
        def __init__(self, value, tail):
                self.IsEmpty = False
                self.Value = value
                self.Tail = tail 

class termanation_screen: 
    def __init__(self):
        self.width = 1280
        self.height = 720
        self.resolution = (self.width, self.height)
        #self.fullscreen = pygame.FULLSCREEN

        pygame.init() # Makes pygame work

        # Set the resolution
        self.screen = pygame.display.set_mode(self.resolution)

        # Set Title
        self.caption = pygame.display.set_caption('Termanation screen')

        # Set default font
        self.font = pygame.font.Font(None, 30)

        #Draw scoreboard
        #..........

        #Draw message
        def draw(self):
            self.screen.fill(100, 100, 225)
            text = self.font.render("Game over, thanks for playing!")
            self.screen.blit(text, self.width/2, self.height/2)

            #bg_image = pygame.image.load("...")
            #self.screen.blit(bg_image, self.width/ ., self.height * ..)

            #button stuff
            #..

            pygame.display.flip()
        
        def update(self):
            pass

        def program_loop(self):
            while not process_events:
                self.update()
                self.draw()


def process_events():
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        sys.exit()
        return False  # return termanation_screen in game.py

# Main game logic
def program():
        TermanationScreen = termanation_screen()
        TermanationScreen.program_loop()

# Starts program
program()


#in class termanation_screen changed:
#player_won = False
#..
#if pos = ..
#    player_won = True

#    font = pygame.font.Font(None, 50)
#    if user_won:
#	        text = font.render("Congratulations!  You won!", 1, white)
#    else:
#	        text = font.render("You lost!", 1, white)	
#    screen.blit(text, area.width/2, area.height/2)
#    pygame.display.flip()