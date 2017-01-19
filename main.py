import pygame
import math
import sys
import game


class Empty:
	def __init__(self):
		self.IsEmpty = True
empty = Empty()

class Node:
	def __init__(self, value, tail):
		self.IsEmpty = False
		self.Value = value
		self.Tail = tail 
	

_game = game.Game()

# Starts program
def program():
	#game.Game.program_loop()
	_game.program_loop()

program()