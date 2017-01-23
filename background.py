import pygame
import math
import sys
import tower
class frontlayer1:
	def __init__(self, x1, y1, x2, y2):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2

	def update(self):
		pass

	def draw(self, screen):
		pygame.draw.rect(screen, tower.white, (int(self.x1), int(self.y1), int(self.x2), int(self.y2)))

class frontlayer2:
	def __init__(self, x1, y1, x2, y2):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2

	def update(self):
		pass

	def draw(self, screen):
		pygame.draw.rect(screen, tower.white, (int(self.x1), int(self.y1), int(self.x2), int(self.y2)))

class frontlayer3:
	def __init__(self, x1, y1, x2, y2):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2

	def update(self):
		pass

	def draw(self, screen):
		pygame.draw.rect(screen, tower.white, (int(self.x1), int(self.y1), int(self.x2), int(self.y2)))
