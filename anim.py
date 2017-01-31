import pygame
import math
import sys
import other
import tower
import os
import time
import random
import globalz
empty = tower.Empty()
rec = pygame.draw.rect(globalz.screen,globalz.white,(25,600,116,116))

diceimages = [pygame.image.load(os.path.join('Project2/1.bmp')),
              pygame.image.load(os.path.join('Project2/2.bmp')),
              pygame.image.load(os.path.join('Project2/3.bmp')),
              pygame.image.load(os.path.join('Project2/4.bmp')),
              pygame.image.load(os.path.join('Project2/5.bmp')),
              pygame.image.load(os.path.join('Project2/6.bmp'))]
class Animation:
    def __init__(self, x, y, game):
        self.game = game
        self.x = x
        self.y = y
        self.done = False
        self.old = other.dice.dice_result
        self.imglst = tower.Node(diceimages[0], 
              tower.Node(diceimages[1], 
               tower.Node(diceimages[2], 
                tower.Node(diceimages[3], 
                 tower.Node(diceimages[4], 
                  tower.Node(diceimages[5], empty))))))
        
    

    def update(self):
       if self.old != other.dice.dice_result or other.dice.dice_result == 9:
           lst = self.imglst
           while (not  diceimages[other.dice.dice_result-1] == lst.Value):
                lst = lst.Tail
                if lst.IsEmpty:
                    lst = self.imglst
                    break
                self.image = lst.Value
           self.done = True
       self.old = other.dice.dice_result
            

    def Draw(self, screen):
         if self.done:
             for x in range(0,10):
               screen.blit(diceimages[random.randint(0,5)],(25,600))
               time.sleep(0.05)
               pygame.display.update(rec)
             self.done = False
         else:
             screen.blit(self.image,(25, 600))  
             self.done = False
