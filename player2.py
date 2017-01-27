import pygame
import math
import sys
import tower

class player_2:
	def __init__(self, x, y, x2, y2, fill):
		self.x = x
		self.y = y
		self.x2 = x2
		self.y2 = y2
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
			x_pos, y_pos, cnt_pos1x, whole_side, left_end, right_end, cnt_pos_back):
		self.bgn_blue = bgn_blue
		self.bgn_red = bgn_red
		self.bgn_green = bgn_green
		self.bgn_yellow = bgn_yellow
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.cnt_pos1x = cnt_pos1x
		self.whole_side = whole_side
		self.left_end = left_end
		self.right_end = right_end
		self.cnt_pos_back = cnt_pos_back
		keys = pygame.key.get_pressed()
		if (self.cnt < 10):
			if keys[pygame.K_UP] and not self.IsWDown:
					self.IsWDown = True
					self.y = self.y - (int(y_pos))
					self.cnt = self.cnt + 1
			else:
				if not keys[pygame.K_UP]:
					self.IsWDown = False

		elif ((self.cnt >= 10) and not (self.cnt == 15)):
			if keys[pygame.K_UP] and not self.IsWDown:
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
				if not keys[pygame.K_UP]:
					self.IsWDown = False

		elif (self.cnt == 15):
			if keys[pygame.K_UP] and not self.IsWDown:
					self.IsWDown = True
					self.y = self.y

			else:
				if not keys[pygame.K_UP]:
					self.IsWDown = False
			

		if ((self.cnt < 10) and not (self.cnt == 0)):
			if keys[pygame.K_DOWN] and not self.IsSDown:
				self.IsSDown = True
				self.y = self.y + (int(y_pos))
				self.cnt = self.cnt - 1
			else:
				if not keys[pygame.K_DOWN]:
					self.IsSDown = False
		elif((self.cnt >= 10)):
			if keys[pygame.K_DOWN] and not self.IsSDown:
					self.IsSDown = True
					if (self.cnt == 11):
						self.x = self.x - (int(cnt_pos_back))
					self.y = self.y + (int(y_pos))
					self.cnt = self.cnt - 1

			else:
				if not keys[pygame.K_DOWN]:
					self.IsSDown = False

		elif (self.cnt == 0):
			if keys[pygame.K_DOWN] and not self.IsSDown:
					self.IsSDown = True
					self.y = self.y

			else:
				if not keys[pygame.K_DOWN]:
					self.IsSDown = False

		if (self.cnt < 11):
			if keys[pygame.K_LEFT] and not self.IsADown:
				self.IsADown = True
				if (self.x < left_end):
					self.x = self.x
				else:
					self.x = self.x - (int(x_pos))
			else:
				if not keys[pygame.K_LEFT]:
					self.IsADown = False

		else:
			if keys[pygame.K_LEFT] and not self.IsADown:
				self.IsADown = True
				if (self.x < left_end):
					self.x = self.x
				else:
					self.x = self.x - (int(whole_side))
			else:
				if not keys[pygame.K_LEFT]:
					self.IsADown = False

		if (self.cnt < 11):
			if keys[pygame.K_RIGHT] and not self.IsDDown:
				self.IsDDown = True
				if (self.x > right_end):
					self.x = self.x
				else:
					self.x = self.x + (int(x_pos))
			else:
				if not keys[pygame.K_RIGHT]:
					self.IsDDown = False

		else:
			if keys[pygame.K_RIGHT] and not self.IsDDown:
				self.IsDDown = True
				if (self.x > right_end):
					self.x = self.x
				else:
					self.x = self.x + (int(whole_side))
			else:
				if not keys[pygame.K_RIGHT]:
					self.IsDDown = False
	
	def draw(self, screen):
		pygame.draw.rect(screen, tower.black, (int(self.x), int(self.y), int(self.x2), int(self.y2)), (int(self.fill)))