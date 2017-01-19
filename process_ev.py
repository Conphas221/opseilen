import pygame
import math
import sys

# Handeling pygame events
def process_events():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			return True
		#elif event.type == pygame.KEYDOWN:
		#	game.Player1.key_event(event)
	return False