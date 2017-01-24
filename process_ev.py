import pygame
import math
import sys
import globalz
import other
import button

# Handeling pygame events
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            button.click(event.pos)
    return False