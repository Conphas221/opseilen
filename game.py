import pygame
import math
import sys
import background
import tower
import process_ev


class Game:
	def __init__(self):
		# Resolution
		self.width = 1024
		self.height = 768
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
		background.frontlayer1 = background.frontlayer1(0, 0, float((self.width / 3) - self.width * 0.002), self.height)
		background.frontlayer2 = background.frontlayer2(float(((self.width / 3) * 2) + self.width * 0.002), 0, float(self.width / 3), self.height)

		#Create the tower
		tower.Tower = tower.Tower(self)

		# Create Players
		#self.Player1 = Player1(self)


	# Update logic of game
	def update(self):
		background.frontlayer1.update()
		background.frontlayer2.update()

		tower.Tower.update()
		#self.Player1.update()

	def draw(self):
		# Clearing the screen
		self.screen.fill((0, 0, 0))

		# Draw elements
		background.frontlayer1.draw(self.screen)
		background.frontlayer2.draw(self.screen)

		#Draw tower 
		tower.Tower.draw(self.screen)

		# Draw Players
		#self.Player1.draw(self.screen)


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

	