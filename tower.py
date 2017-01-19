import pygame
import math
import sys

red = (255,0,0) # Configures some colors
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

class Tower:
	def __init__(self, game):
		self.game = game
		self.Sides = Node(Side(red), Node(Side(green), Node(Side(yellow), Node(Side(blue),empty))))
		l = self.Sides 
		while (not l.Tail.IsEmpty):
			l = l.Tail
		l.Tail = self.Sides

		self.IsRightDown = False
		self.IsLeftDown = False
	
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
		self.Sides.Value.draw(screen, float(self.game.width / 3), 0, (float(self.game.width / 3) / 2), self.game.height)
		self.Sides.Tail.Value.draw(screen, float(self.game.width / 3)  + (float(self.game.width / 3) / 2), 0, (float(self.game.width / 3) / 2), self.game.height)

class Side:
	def __init__(self, color):
		self.Color = color
	def draw(self, screen, x1, y1, x2, y2):
		pygame.draw.rect(screen, self.Color, (int(x1), int(y1), int(x2), int(y2)))