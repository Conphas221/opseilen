import pygame, math, sys
red = (255,0,0) #configures some colors
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)


class Empty:
	def __init__(self):
		self.IsEmpty = True
empty = Empty()

class Node:
	def __init__(self, value, tail):
		self.IsEmpty = False
		self.Value = value
		self.Tail = tail 

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
		self.frontlayer1 = frontlayer1(0, 0, float((self.width / 3) - self.width * 0.002), self.height)
		self.frontlayer2 = frontlayer2(float(((self.width / 3) * 2) + self.width * 0.002), 0, float(self.width / 3), self.height)

		#Create the tower
		self.Tower = Tower(self)

	# Update logic of game
	def update(self):
		self.frontlayer1.update()
		self.frontlayer2.update()

		self.Tower.update()

	def draw(self):
		# Clearing the screen
		self.screen.fill((0, 0, 0))

		# Draw elements
		self.frontlayer1.draw(self.screen)
		self.frontlayer2.draw(self.screen)

		#Draw tower 
		self.Tower.draw(self.screen)

		# Flipping the screen
		pygame.display.flip()

	# Actual loop
	def program_loop(self):
		while not process_events():
			self.update()
			self.draw()


#colorlist = Node(red, Node(blue, Node(yellow, Node(green, colorlist))))
class Tower:
	def __init__(self, game):
		self.Sides = Node(Side(red), Node(Side(green), Node(Side(yellow), Node(Side(blue),empty))))
		l = self.Sides 
		while (not l.Tail.IsEmpty):
			l = l.Tail
		l.Tail = self.Sides

		self.IsRightDown = False
		self.IsLeftDown = False

		self.Game = game
	
	def update(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_RIGHT] and not self.IsRightDown:
			self.IsRightDown = True
			l = self.Sides
			while(l.Tail.Value != self.Sides.Value):
				l = l.Tail
			self.Sides = l
		else:
			if not keys[pygame.K_RIGHT]:
				self.IsRightDown = False



		if keys[pygame.K_LEFT] and not self.IsLeftDown:
			self.Sides = self.Sides.Tail
			self.IsLeftDown = True

		else:
			if not keys[pygame.K_LEFT]:
				self.IsLeftDown = False



	def draw(self, screen):
		self.Sides.Value.draw(screen, float(self.Game.width / 3), 0, (float(self.Game.width / 3) / 2), self.Game.height)
		self.Sides.Tail.Value.draw(screen, float(self.Game.width / 3)  + (float(self.Game.width / 3) / 2), 0, (float(self.Game.width / 3) / 2), self.Game.height)

class Side:
	def __init__(self, color):
		self.Color = color
	def draw(self, screen, x1, y1, x2, y2):
		pygame.draw.rect(screen, self.Color, (int(x1), int(y1), int(x2), int(y2)))




class frontlayer1:
	def __init__(self, x1, y1, x2, y2):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2


	def update(self):
		return True

	def draw(self, screen):
		pygame.draw.rect(screen, white, (int(self.x1), int(self.y1), int(self.x2), int(self.y2)))

class frontlayer2:
	def __init__(self, x1, y1, x2, y2):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2


	def update(self):
		return True

	def draw(self, screen):
		pygame.draw.rect(screen, white, (int(self.x1), int(self.y1), int(self.x2), int(self.y2)))


#class backlayer_red:
#	def __init__(self, x1, y1, x2, y2):
#		self.x1 = x1
#		self.y1 = y1
#		self.x2 = x2
#		self.y2 = y2


#	def update(self):
#		return True

#	def draw(self, screen):
#		pygame.draw.rect(screen, red, (int(self.x1), int(self.y1), int(self.x2), int(self.y2)))

#class backlayer_yellow:
#	def __init__(self, x1, y1, x2, y2):
#		self.x1 = x1
#		self.y1 = y1
#		self.x2 = x2
#		self.y2 = y2


#	def update(self):
#		return True

#	def draw(self, screen):
#		pygame.draw.rect(screen, yellow, (int(self.x1), int(self.y1), int(self.x2), int(self.y2)))

	
# Handeling pygame events
def process_events():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			return True
	return False





# Main game logic
def program():
	game = Game()
	game.program_loop()

# Starts program
program()


