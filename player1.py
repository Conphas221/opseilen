import pygame
import math
import sys
import tower
import other
import globalz

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
		#when player moves up present a question based on the tower and outcome of the automatic dice roll
		keys = pygame.key.get_pressed()
		if (self.cnt < 10):
			if keys[pygame.K_UP] and not self.IsWDown:
				while other.questions.pressed == False:
					print(self.x,bgn_blue,bgn_red,bgn_green,bgn_yellow)
					other.dice.dice_roll()
					if other.dice.dice_result % 2 == 0:
						if self.x < bgn_red:
							other.questions.question_mc(globalz.mc_sport,globalz.ori_mc_sport,globalz.ans_mc_sport)
						if self.x > bgn_red and self.x < bgn_green:
							other.questions.question_mc(globalz.mc_entert,globalz.ori_mc_entert,globalz.ans_mc_entert)
						if self.x > bgn_green and self.x < bgn_yellow:
							other.questions.question_mc(globalz.mc_geo,globalz.ori_mc_geo,globalz.ans_mc_geo)
						if self.x > bgn_yellow:
							other.questions.question_mc(globalz.mc_history,globalz.ori_mc_history,globalz.ans_mc_history)
					if other.dice.dice_result % 2 != 0:
						if self.x < bgn_red:
							other.questions.question_open(globalz.o_sport,globalz.ori_o_sport,globalz.key_o_sport)
						if self.x > bgn_red and self.x < bgn_green:
							other.questions.question_open(globalz.o_entert,globalz.ori_o_entert,globalz.key_o_entert)
						if self.x > bgn_green and self.x < bgn_yellow:
							other.questions.question_open(globalz.o_geo,globalz.ori_o_geo,globalz.key_o_geo)
						if self.x > bgn_yellow:
							other.questions.question_open(globalz.o_history,globalz.ori_o_history,globalz.key_o_history)
				if other.questions.player1_correct == 1:
					other.dice.dice_roll()
					for x in range(0, math.ceil(other.dice.dice_result/2)):
							self.IsWDown = True
							self.y = self.y - (int(y_pos))
							self.cnt = self.cnt + 1
					if (self.cnt > 10):	
								if ((self.x < bgn_green) and (self.x > bgn_red)):
									self.x = (int(cnt_pos1x))
								elif ((self.x < bgn_yellow) and (self.x > bgn_green)):
									self.x = (int(cnt_pos1x)) + (int(whole_side))
								elif (self.x > bgn_yellow):
									self. x = (int(cnt_pos1x)) + ((int(whole_side) * 2))
								elif (self.x < bgn_red):
									self.x = (int(cnt_pos1x)) - (int(whole_side))
					other.questions.player1_correct = 2
				other.questions.pressed = False
				other.turns.turn()
			else:
				if not keys[pygame.K_UP]:
					self.IsWDown = False

		elif ((self.cnt >= 10) and not (self.cnt >= 15)):
			if keys[pygame.K_UP] and not self.IsWDown:
				while other.questions.pressed == False:
					other.dice.dice_roll()
					if other.dice.dice_result % 2 == 0:
						if self.x < bgn_red:
							other.questions.question_mc(globalz.mc_sport,globalz.ori_mc_sport,globalz.ans_mc_sport)
						if self.x > bgn_red and self.x < bgn_green:
							other.questions.question_mc(globalz.mc_entert,globalz.ori_mc_entert,globalz.ans_mc_entert)
						if self.x > bgn_green and self.x < bgn_yellow:
							other.questions.question_mc(globalz.mc_geo,globalz.ori_mc_geo,globalz.ans_mc_geo)
						if self.x > bgn_yellow:
							other.questions.question_mc(globalz.mc_history,globalz.ori_mc_history,globalz.ans_mc_history)
					if other.dice.dice_result % 2 != 0:
						if self.x < bgn_red:
							other.questions.question_open(globalz.o_sport,globalz.ori_o_sport,globalz.key_o_sport)
						if self.x > bgn_red and self.x < bgn_green:
							other.questions.question_open(globalz.o_entert,globalz.ori_o_entert,globalz.key_o_entert)
						if self.x > bgn_green and self.x < bgn_yellow:
							other.questions.question_open(globalz.o_geo,globalz.ori_o_geo,globalz.key_o_geo)
						if self.x > bgn_yellow:
							other.questions.question_open(globalz.o_history,globalz.ori_o_history,globalz.key_o_history)
				if other.questions.player1_correct == 1:
					other.dice.dice_roll()
					for x in range(0, math.ceil(other.dice.dice_result/2)):
						if (self.cnt >= 10):	
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
					other.questions.player1_correct = 2
				other.questions.pressed = False
				other.turns.turn()

			else:
				if not keys[pygame.K_UP]:
					self.IsWDown = False

		elif (self.cnt >= 15):
			if keys[pygame.K_UP] and not self.IsWDown:
					self.IsWDown = True
					self.y = self.y

			else:
				if not keys[pygame.K_UP]:
					self.IsWDown = False
			
			#when player moves down present a question based on the tower and outcome of the automatic dice roll
		if ((self.cnt < 10) and not (self.cnt <= 0)):
			if keys[pygame.K_DOWN] and not self.IsSDown:
				while other.questions.pressed == False:
					other.dice.dice_roll()
					if other.dice.dice_result % 2 == 0:
						if self.x < bgn_red:
							other.questions.question_mc(globalz.mc_sport,globalz.ori_mc_sport,globalz.ans_mc_sport)
						if self.x > bgn_red and self.x < bgn_green:
							other.questions.question_mc(globalz.mc_entert,globalz.ori_mc_entert,globalz.ans_mc_entert)
						if self.x > bgn_green and self.x < bgn_yellow:
							other.questions.question_mc(globalz.mc_geo,globalz.ori_mc_geo,globalz.ans_mc_geo)
						if self.x > bgn_yellow:
							other.questions.question_mc(globalz.mc_history,globalz.ori_mc_history,globalz.ans_mc_history)
					if other.dice.dice_result % 2 != 0:
						if self.x < bgn_red:
							other.questions.question_open(globalz.o_sport,globalz.ori_o_sport,globalz.key_o_sport)
						if self.x > bgn_red and self.x < bgn_green:
							other.questions.question_open(globalz.o_entert,globalz.ori_o_entert,globalz.key_o_entert)
						if self.x > bgn_green and self.x < bgn_yellow:
							other.questions.question_open(globalz.o_geo,globalz.ori_o_geo,globalz.key_o_geo)
						if self.x > bgn_yellow:
							other.questions.question_open(globalz.o_history,globalz.ori_o_history,globalz.key_o_history)
				if other.questions.player1_correct == 1:
					other.dice.dice_roll()
					for x in range(0, math.ceil(other.dice.dice_result/2)):
						self.IsSDown = True
						self.y = self.y + (int(y_pos))
						self.cnt = self.cnt - 1
						if self.cnt == 0: #breaks the loop so that the player can't move below the starting position
							break
					other.questions.player1_correct = 2
				other.questions.pressed = False
				other.turns.turn()
			else:
				if not keys[pygame.K_DOWN]:
					self.IsSDown = False
		elif((self.cnt >= 10)):
			if keys[pygame.K_DOWN] and not self.IsSDown:
				while other.questions.pressed == False:
					other.dice.dice_roll()
					if other.dice.dice_result % 2 == 0:
						if self.x < bgn_red:
							other.questions.question_mc(globalz.mc_sport,globalz.ori_mc_sport,globalz.ans_mc_sport)
						if self.x > bgn_red and self.x < bgn_green:
							other.questions.question_mc(globalz.mc_entert,globalz.ori_mc_entert,globalz.ans_mc_entert)
						if self.x > bgn_green and self.x < bgn_yellow:
							other.questions.question_mc(globalz.mc_geo,globalz.ori_mc_geo,globalz.ans_mc_geo)
						if self.x > bgn_yellow:
							other.questions.question_mc(globalz.mc_history,globalz.ori_mc_history,globalz.ans_mc_history)
					if other.dice.dice_result % 2 != 0:
						if self.x < bgn_red:
							other.questions.question_open(globalz.o_sport,globalz.ori_o_sport,globalz.key_o_sport)
						if self.x > bgn_red and self.x < bgn_green:
							other.questions.question_open(globalz.o_entert,globalz.ori_o_entert,globalz.key_o_entert)
						if self.x > bgn_green and self.x < bgn_yellow:
							other.questions.question_open(globalz.o_geo,globalz.ori_o_geo,globalz.key_o_geo)
						if self.x > bgn_yellow:
							other.questions.question_open(globalz.o_history,globalz.ori_o_history,globalz.key_o_history)
				if other.questions.player1_correct == 1:
					other.dice.dice_roll()
					for x in range(0, math.ceil(other.dice.dice_result/2)):
						self.IsSDown = True
						if (self.cnt == 11): #makes sure the player icon position is correct when moving down from the top 5 spots
							self.x = self.x - (int(cnt_pos_back))
						self.y = self.y + (int(y_pos))
						self.cnt = self.cnt - 1
					other.questions.player1_correct = 2
				other.questions.pressed = False
				other.turns.turn()

			else:
				if not keys[pygame.K_DOWN]:
					self.IsSDown = False
		#player can't move down when below the tower
		elif (self.cnt == 0):
			if keys[pygame.K_DOWN] and not self.IsSDown:
					self.IsSDown = True
					self.y = self.y

			else:
				if not keys[pygame.K_DOWN]:
					self.IsSDown = False
		#asks a question when the player moves left on the tower
		if (self.cnt < 11) and (self.cnt > 0):
			if keys[pygame.K_LEFT] and not self.IsADown:
				while other.questions.pressed == False:
					other.dice.dice_roll()
					if other.dice.dice_result % 2 == 0:
						if self.x < bgn_red:
							other.questions.question_mc(globalz.mc_sport,globalz.ori_mc_sport,globalz.ans_mc_sport)
						if self.x > bgn_red and self.x < bgn_green:
							other.questions.question_mc(globalz.mc_entert,globalz.ori_mc_entert,globalz.ans_mc_entert)
						if self.x > bgn_green and self.x < bgn_yellow:
							other.questions.question_mc(globalz.mc_geo,globalz.ori_mc_geo,globalz.ans_mc_geo)
						if self.x > bgn_yellow:
							other.questions.question_mc(globalz.mc_history,globalz.ori_mc_history,globalz.ans_mc_history)
					if other.dice.dice_result % 2 != 0:
						if self.x < bgn_red:
							other.questions.question_open(globalz.o_sport,globalz.ori_o_sport,globalz.key_o_sport)
						if self.x > bgn_red and self.x < bgn_green:
							other.questions.question_open(globalz.o_entert,globalz.ori_o_entert,globalz.key_o_entert)
						if self.x > bgn_green and self.x < bgn_yellow:
							other.questions.question_open(globalz.o_geo,globalz.ori_o_geo,globalz.key_o_geo)
						if self.x > bgn_yellow:
							other.questions.question_open(globalz.o_history,globalz.ori_o_history,globalz.key_o_history)
				if other.questions.player1_correct == 1:
					other.dice.dice_roll()
					for x in range(0, math.ceil(other.dice.dice_result/2)):
						self.IsADown = True
						if (self.x < left_end):
							self.x = self.right_end + (int(x_pos))
						else:
							self.x = self.x - (int(x_pos))
					other.questions.player1_correct = 2
				other.questions.pressed = False
				other.turns.turn()
			

			else:
				if not keys[pygame.K_LEFT]:
					self.IsADown = False
		#doesn't ask a question when the player moves below the tower to position himself
		elif (self.cnt == 0):
			if keys[pygame.K_LEFT] and not self.IsADown:
				self.IsADown = True
				if (self.x < left_end):
					self.x = self.right_end + (int(x_pos))
				else:
					self.x = self.x - (int(x_pos))
			else:
				if not keys[pygame.K_LEFT]:
					self.IsADown = False
	#presents a question and moves the player left if answered correctly
		else:
			if keys[pygame.K_LEFT] and not self.IsADown:
				while other.questions.pressed == False:
					other.dice.dice_roll()
					if other.dice.dice_result % 2 == 0:
						if self.x < bgn_red:
							other.questions.question_mc(globalz.mc_sport,globalz.ori_mc_sport,globalz.ans_mc_sport)
						if self.x > bgn_red and self.x < bgn_green:
							other.questions.question_mc(globalz.mc_entert,globalz.ori_mc_entert,globalz.ans_mc_entert)
						if self.x > bgn_green and self.x < bgn_yellow:
							other.questions.question_mc(globalz.mc_geo,globalz.ori_mc_geo,globalz.ans_mc_geo)
						if self.x > bgn_yellow:
							other.questions.question_mc(globalz.mc_history,globalz.ori_mc_history,globalz.ans_mc_history)
					if other.dice.dice_result % 2 != 0:
						if self.x < bgn_red:
							other.questions.question_open(globalz.o_sport,globalz.ori_o_sport,globalz.key_o_sport)
						if self.x > bgn_red and self.x < bgn_green:
							other.questions.question_open(globalz.o_entert,globalz.ori_o_entert,globalz.key_o_entert)
						if self.x > bgn_green and self.x < bgn_yellow:
							other.questions.question_open(globalz.o_geo,globalz.ori_o_geo,globalz.key_o_geo)
						if self.x > bgn_yellow:
							other.questions.question_open(globalz.o_history,globalz.ori_o_history,globalz.key_o_history)
				if other.questions.player1_correct == 1:
					other.dice.dice_roll()
					for x in range(0, math.ceil(other.dice.dice_result/2)):
						self.IsADown = True
						if (self.x < left_end):
							self.x = self.x + (3*(int(whole_side)))
						else:
							self.x = self.x - (int(whole_side))
					other.questions.player1_correct = 2
				other.questions.pressed = False
				other.turns.turn()
			else:
				if not keys[pygame.K_LEFT]:
					self.IsADown = False
		#asks a question when the player moves right on the tower
		if (self.cnt < 11) and (self.cnt > 0):
			if keys[pygame.K_RIGHT] and not self.IsDDown:
				while other.questions.pressed == False:
					other.dice.dice_roll()
					if other.dice.dice_result % 2 == 0:
						if self.x < bgn_red:
							other.questions.question_mc(globalz.mc_sport,globalz.ori_mc_sport,globalz.ans_mc_sport)
						if self.x > bgn_red and self.x < bgn_green:
							other.questions.question_mc(globalz.mc_entert,globalz.ori_mc_entert,globalz.ans_mc_entert)
						if self.x > bgn_green and self.x < bgn_yellow:
							other.questions.question_mc(globalz.mc_geo,globalz.ori_mc_geo,globalz.ans_mc_geo)
						if self.x > bgn_yellow:
							other.questions.question_mc(globalz.mc_history,globalz.ori_mc_history,globalz.ans_mc_history)
					if other.dice.dice_result % 2 != 0:
						if self.x < bgn_red:
							other.questions.question_open(globalz.o_sport,globalz.ori_o_sport,globalz.key_o_sport)
						if self.x > bgn_red and self.x < bgn_green:
							other.questions.question_open(globalz.o_entert,globalz.ori_o_entert,globalz.key_o_entert)
						if self.x > bgn_green and self.x < bgn_yellow:
							other.questions.question_open(globalz.o_geo,globalz.ori_o_geo,globalz.key_o_geo)
						if self.x > bgn_yellow:
							other.questions.question_open(globalz.o_history,globalz.ori_o_history,globalz.key_o_history)
				if other.questions.player1_correct == 1:
					other.dice.dice_roll()
					for x in range(0, math.ceil(other.dice.dice_result/2)):
						self.IsDDown = True
						if (self.x > right_end):
							self.x = self.left_end - (int(x_pos))
						else:
							self.x = self.x + (int(x_pos))
					other.questions.player1_correct = 2
				other.questions.pressed = False
				other.turns.turn()

			else:
				if not keys[pygame.K_RIGHT]:
					self.IsDDown = False
			
			#when player is not on tower move right without questions
		elif (self.cnt == 0):
			if keys[pygame.K_RIGHT] and not self.IsDDown:
				self.IsDDown = True
				if (self.x > right_end):
					self.x = self.left_end - (int(x_pos))
				else:
					self.x = self.x + (int(x_pos))
			else:
				if not keys[pygame.K_RIGHT]:
					self.IsDDown = False
		#moves player right after answering the presented question correctly
		else:
			if keys[pygame.K_RIGHT] and not self.IsDDown:
				while other.questions.pressed == False:
					other.dice.dice_roll()
					if other.dice.dice_result % 2 == 0:
						if self.x < bgn_red:
							other.questions.question_mc(globalz.mc_sport,globalz.ori_mc_sport,globalz.ans_mc_sport)
						if self.x > bgn_red and self.x < bgn_green:
							other.questions.question_mc(globalz.mc_entert,globalz.ori_mc_entert,globalz.ans_mc_entert)
						if self.x > bgn_green and self.x < bgn_yellow:
							other.questions.question_mc(globalz.mc_geo,globalz.ori_mc_geo,globalz.ans_mc_geo)
						if self.x > bgn_yellow:
							other.questions.question_mc(globalz.mc_history,globalz.ori_mc_history,globalz.ans_mc_history)
					if other.dice.dice_result % 2 != 0:
						if self.x < bgn_red:
							other.questions.question_open(globalz.o_sport,globalz.ori_o_sport,globalz.key_o_sport)
						if self.x > bgn_red and self.x < bgn_green:
							other.questions.question_open(globalz.o_entert,globalz.ori_o_entert,globalz.key_o_entert)
						if self.x > bgn_green and self.x < bgn_yellow:
							other.questions.question_open(globalz.o_geo,globalz.ori_o_geo,globalz.key_o_geo)
						if self.x > bgn_yellow:
							other.questions.question_open(globalz.o_history,globalz.ori_o_history,globalz.key_o_history)
				if other.questions.player1_correct == 1:
					other.dice.dice_roll()
					for x in range(0, math.ceil(other.dice.dice_result/2)):
						self.IsDDown = True
						if (self.x > right_end):
							self.x = self.x - (3*(int(whole_side)))
						else:
							self.x = self.x + (int(whole_side))
					other.questions.player1_correct = 2
				other.questions.pressed = False
				other.turns.turn()
			else:
				if not keys[pygame.K_RIGHT]:
					self.IsDDown = False
	#draws the player icon
	def draw(self, screen):
		pygame.draw.circle(screen, tower.black, (int(self.x), int(self.y)), (int(self.r)), (int(self.fill)))

