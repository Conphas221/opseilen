import pygame
import math
import sys
import globalz
import other

red = (255, 71, 71) # Configures some colors
green = (71, 255, 71) 
blue = (71, 71, 255) 
white = (255,255,255)
black = (0,0,0)
yellow = (255, 255, 71)

class Empty:
	def __init__(self):
		self.IsEmpty = True
empty = Empty()

class Node:
	def __init__(self, value, tail):
		self.IsEmpty = False
		self.Value = value
		self.Tail = tail

class Tower_red:
	def __init__(self, x1, y1, x2, y2):
			self.x1 = x1
			self.y1 = y1
			self.x2 = x2
			self.y2 = y2

	def update(self):
		pass

	def draw(self):
		pygame.draw.rect(other.screen, red, (float(self.x1), float(self.y1), float(self.x2), float(self.y2)))
	
class Tower_green:
	def __init__(self, x1, y1, x2, y2):
			self.x1 = x1
			self.y1 = y1
			self.x2 = x2
			self.y2 = y2

	def update(self):
		pass

	def draw(self,):
		pygame.draw.rect(other.screen, green, (float(self.x1), float(self.y1), float(self.x2), float(self.y2)))
		
class Tower_blue:
	def __init__(self, x1, y1, x2, y2):
			self.x1 = x1
			self.y1 = y1
			self.x2 = x2
			self.y2 = y2

	def update(self):
		pass

	def draw(self):
		pygame.draw.rect(other.screen, blue, (float(self.x1), float(self.y1), float(self.x2), float(self.y2)))

class Tower_yellow:
	def __init__(self, x1, y1, x2, y2):
			self.x1 = x1
			self.y1 = y1
			self.x2 = x2
			self.y2 = y2

	def update(self):
		pass

	def draw(self):
		pygame.draw.rect(other.screen, yellow, (float(self.x1), float(self.y1), float(self.x2), float(self.y2)))

		#def __init__(self, game):
	#	self.game = game
	#	self.Sides = Node(Side(red), Node(Side(green), Node(Side(yellow), Node(Side(blue),empty))))
	#	l = self.Sides 
	#	while (not l.Tail.IsEmpty):
	#		l = l.Tail
	#	l.Tail = self.Sides

	#	self.IsRightDown = False
	#	self.IsLeftDown = False
	
	#def update(self):
		#keys = pygame.key.get_pressed()
		#if keys[pygame.K_RIGHT] and not self.IsRightDown:
		#	self.IsRightDown = True
		#	l = self.Sides
		#	while(l.Tail.Value != self.Sides.Value):
		#		l = l.Tail
		#	self.Sides = l
		#else:
		#	if not keys[pygame.K_RIGHT]:
		#		self.IsRightDown = False



		#if keys[pygame.K_LEFT] and not self.IsLeftDown:
		#	self.Sides = self.Sides.Tail
		#	self.IsLeftDown = True

		#else:
		#	if not keys[pygame.K_LEFT]:
		#		self.IsLeftDown = False
		

#class Side:
#	def __init__(self, color):
#		self.Color = color
#	def draw(self, screen, x1, y1, x2, y2):
#		pygame.draw.rect(screen, self.Color, (int(x1), int(y1), int(x2), int(y2)))