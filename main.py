import pygame
import math
import sys
import game
import other
import globalz
import MainMenuNew


class Empty:
	def __init__(self):
		self.IsEmpty = True
empty = Empty()

class Node:
	def __init__(self, value, tail):
		self.IsEmpty = False
		self.Value = value
		self.Tail = tail 
	

games = game.Game()

# Starts program
def program():
	#game.Game.program_loop()
	games.program_loop()
	mainmenu.MainmenuNew.program_loop()

program()




dice_result+".bmp"