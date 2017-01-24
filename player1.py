import pygame
import math
import sys
import tower

class player_1:
	def __init__(self, x, y, r, fill):
		self.x = x
		self.y = y
		self.r = r
		self.fill = fill

	IsWDown = False
	IsSDown = False
	IsADown = False
	IsDDown = False
	cnt = 0
	def update(self, 
			bgn_blue, 
			bgn_red, 
			bgn_green, 
			bgn_yellow, 
			x_pos, y_pos, cnt_pos1x, whole_side, cnt_pos_back):
		self.bgn_blue = bgn_blue
		self.bgn_red = bgn_red
		self.bgn_green = bgn_green
		self.bgn_yellow = bgn_yellow
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.cnt_pos1x = cnt_pos1x
		self.whole_side = whole_side
		self.cnt_pos_back = cnt_pos_back
		keys = pygame.key.get_pressed()
		if (self.cnt < 10):
			if keys[pygame.K_w] and not self.IsWDown:
					self.IsWDown = True
					self.y = self.y - (int(y_pos))
					self.cnt = self.cnt + 1
			else:
				if not keys[pygame.K_w]:
					self.IsWDown = False

		elif ((self.cnt >= 10) and not (self.cnt == 15)):
			if keys[pygame.K_w] and not self.IsWDown:
					self.IsWDown = True
					if (self.cnt == 10):	
						if ((self.x < bgn_green) and (self.x > bgn_red)):
							self.x = (int(cnt_pos1x))
						elif ((self.x < bgn_yellow) and (self.x > bgn_green)):
							self.x = (int(cnt_pos1x)) + (int(whole_side))
						elif (self.x > bgn_yellow):
							self. x = (int(cnt_pos1x)) + ((int(whole_side) * 2))
						elif (self.x < bgn_red):
							self.x = (int(cnt_pos1x)) - (int(whole_side))

					self.y = self.y - (int(y_pos))
					self.cnt = self.cnt + 1
			else:
				if not keys[pygame.K_w]:
					self.IsWDown = False

		elif (self.cnt == 15):
			if keys[pygame.K_w] and not self.IsWDown:
					self.IsWDown = True
					self.y = self.y

			else:
				if not keys[pygame.K_w]:
					self.IsWDown = False
			

		if ((self.cnt < 10) and not (self.cnt == 0)):
			if keys[pygame.K_s] and not self.IsSDown:
				self.IsSDown = True
				self.y = self.y + (int(y_pos))
				self.cnt = self.cnt - 1
			else:
				if not keys[pygame.K_s]:
					self.IsSDown = False
		elif((self.cnt >= 10)):
			if keys[pygame.K_s] and not self.IsSDown:
					self.IsSDown = True
					if (self.cnt == 11):
						self.x = self.x - (int(cnt_pos_back))
					self.y = self.y + (int(y_pos))
					self.cnt = self.cnt - 1

			else:
				if not keys[pygame.K_s]:
					self.IsSDown = False

		elif (self.cnt == 0):
			if keys[pygame.K_s] and not self.IsSDown:
					self.IsSDown = True
					self.y = self.y

			else:
				if not keys[pygame.K_s]:
					self.IsSDown = False

		if (self.cnt < 11):
			if keys[pygame.K_a] and not self.IsADown:
				self.IsADown = True
				self.x = self.x - (int(x_pos))
			else:
				if not keys[pygame.K_a]:
					self.IsADown = False

		else:
			if keys[pygame.K_a] and not self.IsADown:
				self.IsADown = True
				self.x = self.x - (int(whole_side))
			else:
				if not keys[pygame.K_a]:
					self.IsADown = False

		if (self.cnt < 11):
			if keys[pygame.K_d] and not self.IsDDown:
				self.IsDDown = True
				self.x = self.x + (int(x_pos))
			else:
				if not keys[pygame.K_d]:
					self.IsDDown = False

		else:
			if keys[pygame.K_d] and not self.IsDDown:
				self.IsDDown = True
				self.x = self.x + (int(whole_side))
			else:
				if not keys[pygame.K_d]:
					self.IsDDown = False
	
	def draw(self, screen):
		pygame.draw.circle(screen, tower.black, (int(self.x), int(self.y)), (int(self.r)), (int(self.fill)))











#class Player1:
#	def __init__(self, game):
#		self.Game = game
#		self.Gridposvert1 = Node(playerdraw((self.Game.width / 3) + ((self.Game.width / 3) / 6), 
#								 (self.Game.height / 1.05), (self.Game.width * 0.025)), 
#					  Node(playerdraw((self.Game.width / 3) + ((self.Game.width / 3) / 6), 
#					   (self.Game.height / 1.14), (self.Game.width * 0.025)), empty))
#		l = self.Gridposvert1
#		self.Gridposhor1 = Node(playerdraw((self.Game.width / 3) + ((self.Game.width / 3) / 6), 
#								 (self.Game.height / 1.05), (self.Game.width * 0.025)), 
#					  Node(playerdraw((self.Game.width / 3) + ((self.Game.width / 3) / 3), 
#					   (self.Game.height / 1.05), (self.Game.width * 0.025)), empty))
#		l_2 = self.Gridposhor1
#		while (not l_2.Tail.IsEmpty):
#			l_2 = l_2.Tail
#		l_2.Tail = self.Gridposhor1

#		while (not l.Tail.IsEmpty):
#			l = l.Tail
#		l.Tail = self.Gridposvert1

#		self.delete_pos = False
	
#	def key_event(self, event):
#		if event.key == pygame.K_w:
#			l = self.Gridposvert1
#			while(l.Tail.Value != self.Gridposvert1.Value):
#				l = l.Tail
#			self.Gridposvert1 = l
#		if event.key == pygame.K_s:
#			self.Gridposvert1 = self.Gridposvert1.Tail
#		if event.key == pygame.K_a:
#			self.Gridposhor1 = self.Gridposhor1.Tail
#		if event.key == pygame.K_d:
#			l_2 = self.Gridposhor1
#			self.delete_pos = True
#			while(l_2.Tail.Value != self.Gridposhor1.Value):
#				l_2 = l_2.Tail
#			self.Gridposhor1 = l_2

#	def update(self):
#		"""
#		keys = pygame.key.get_pressed()

#		if keys[pygame.K_w] and not self.IsWDown:
#			self.IsWDown = True
#			l = self.Gridposvert1
#			while(l.Tail.Value != self.Gridposvert1.Value):
#				l = l.Tail
#			self.Gridposvert1 = l
#		else:
#			if not keys[pygame.K_w]:
#				self.IsWDown = False



#		if keys[pygame.K_s] and not self.IsSDown:
#			self.Gridposvert1 = self.Gridposvert1.Tail
#			self.IsSDown = True

#		else:
#			if not keys[pygame.K_s]:
#				self.IsSDown = False
	
#		if keys[pygame.K_d] and not self.IsDDown:
#			self.IsDDown = True
#			l_2 = self.Gridposhor1
#			self.delete_pos = True
#			while(l_2.Tail.Value != self.Gridposhor1.Value):
#				l_2 = l_2.Tail
#			self.Gridposhor1 = l_2
#		else:
#			if not keys[pygame.K_d]:
#				self.IsDDown = False

#		if keys[pygame.K_a] and not self.IsADown:
#			self.Gridposhor1 = self.Gridposhor1.Tail
#			self.IsADown = True
#			if self.Gridposhor1.Value == playerdraw((self.Game.width / 3) + ((self.Game.width / 3) / 6), 
#								 (self.Game.height / 1.05), (self.Game.width * 0.025)):
#				self.delete_pos - False
#			else:
#				if not keys[pygame.K_d]:
#					self.IsADown = False
#		pass

#	def draw(self, screen):
#		if not self.delete_pos:
#			self.Gridposvert1.Value.draw(screen, (self.Gridposvert1.Value), (self.Gridposvert1.Value), (self.Gridposvert1.Value))
#		else:
#			self.Gridposhor1.Value.draw(screen, (self.Gridposhor1.Value), (self.Gridposhor1.Value), (self.Gridposhor1.Value))

#class playerdraw:
#	def __init__(self, positionx, positiony, radius):
#		self.Positionx = positionx
#		self.Positiony = positiony
#		self.Radius = radius
#	def draw(self, screen, positionx, positiony, radius):
#		pygame.draw.circle(screen, black, (int(self.Positionx), int(self.Positiony)), int(self.Radius))