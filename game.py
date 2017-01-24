import pygame
import math
import sys
import background
import tower
import process_ev
import player1
import points
import other
import globalz
import button

class Game:
    def __init__(self):
        # Resolution
        self.width = 1280
        self.height = 720
        self.resolution = (self.width,self.height)
        #self.fullscreen = pygame.FULLSCREEN

        pygame.init() # Makes pygame work

        # Set the resolution
        self.screen = pygame.display.set_mode(self.resolution)

        # Set Title
        self.caption = pygame.display.set_caption('Opseilen!')

        # Set default font
        self.font = pygame.font.Font(None, 30)

        # Create front layers
        background.frontlayer1 = background.frontlayer1(0, (0 + float(self.height / 20)), float(((self.width / 3) / 2) - self.width * 0.002), self.height)
        background.frontlayer2 = background.frontlayer2(float(((self.width / 3) * 2) + ((self.width / 3) / 2) + self.width * 0.002), (0 + float(self.height / 20)), float(self.width / 3), self.height)
        background.frontlayer3 = background.frontlayer3(0, (float(self.height - (self.height / 20))) , self.width, (float(self.height / 20)))

        #Create the tower
        tower.Tower_red = tower.Tower_red(float(self.width / 3), (0 + float(self.height / 20)), (float(self.width / 3) / 2), (float(self.height - (self.height / 10))))
        tower.Tower_green = tower.Tower_green(float(self.width / 3)  + (float(self.width / 3) / 2), (0 + float(self.height / 20)), (float(self.width / 3) / 2), (float(self.height - (self.height / 10))))
        tower.Tower_blue = tower.Tower_blue(float((self.width / 3) / 2), (0 + float(self.height / 20)), (float(self.width / 3) / 2), (float(self.height - (self.height / 10))))
        tower.Tower_yellow = tower.Tower_yellow(float((self.width / 3) * 2), (0 + float(self.height / 20)), (float(self.width / 3) / 2), (float(self.height - (self.height / 10))))

        # Create Players
        player1.player_1 = player1.player_1((float((self.width / 3) + ((self.width / 3) / 8))), (float(self.height) - (self.height / 40)), (float(self.width * 0.015)), (float(self.width * 0.005)))


	# Update logic of game
    def update(self):
        background.frontlayer1.update()
        background.frontlayer2.update()
        background.frontlayer3.update()


        tower.Tower_red.update()
        tower.Tower_green.update()
        tower.Tower_blue.update()
        tower.Tower_yellow.update()

        #self.Player1.update()
        player1.player_1.update(float((self.width / 3) / 2), 
            float(self.width / 3), 
            float(self.width / 3)  + (float(self.width / 3) / 2), 
            float((self.width / 3) * 2), 
            float((self.width / 3) / 4), 
            float((self.height / 17)), 
            float((self.width / 3) + ((self.width / 3) / 4)), 
            float((self.width / 3) / 2), 
            float((self.width / 3) / 8, ))

    def draw(self):
        # Clearing the screen
        self.screen.fill((0, 0, 0))

        # Draw elements
        background.frontlayer1.draw(self.screen)
        background.frontlayer2.draw(self.screen)
        background.frontlayer3.draw(self.screen)
        # banter = other.Rects(self)
        # banter.draw(self.screen)

        #Draw tower 
        tower.Tower_red.draw(self.screen)
        tower.Tower_green.draw(self.screen)
        tower.Tower_blue.draw(self.screen)
        tower.Tower_yellow.draw(self.screen)

        # Draw Players
        player1.player_1.draw(self.screen)
       # (game, x, y, width, height, text, size, backcolor, frontcolor, callback):
     #  button.draw(game, 45, game.height * 0.9, 100, 32, "Start", 20, (0,0,0), (255,255,255), lambda game: start_chosen(game, 1))
        button.draw(self,0,0,100,100,"getfukd",30,(0,0,0),(255,255,255), lambda game: print("thijs is homo"))

        # Flipping the screen
        pygame.display.flip()

        # Actual loop
    def program_loop(self):
        while not process_ev.process_events():
            self.update()
            self.draw()

# Handeling pygame events
#def process_events():
#	for event in pygame.event.get():
#		if event.type == pygame.QUIT:
#			return True
#		#elif event.type == pygame.KEYDOWN:
#		#	game.Player1.key_event(event)
#	return False

	