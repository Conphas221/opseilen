import pygame
import math
import sys
import background
import tower
import process_ev
import player1
import player2
import player3
import player4
import points
import other
import globalz
import button
import inputbox
import Grid

class Game:
    def __init__(self):
        # Resolution
        self.width = 1366
        self.height = 768
        self.resolution = (self.width,self.height)
        #self.fullscreen = pygame.FULLSCREEN

        pygame.init() # Makes pygame work

        # Set the resolution
        self.screen = pygame.display.set_mode(self.resolution)

        # Set Title
        self.caption = pygame.display.set_caption('Opseilen!')

        # Set default font
        self.font = pygame.font.Font(None, 20)
        # Player draw and update key
        self.Is1Down = False

        self.Is2Down = False

        self.Is3Down = False

        self.Is4Down = False

        Grid.RedGridTop = Grid.RedGridTop(self, (float(((self.width / 3) + ((self.width / 3) / 8))- 57.5)), ((float((self.height) - (self.height / 40)))-450))
        Grid.YellowGridTop = Grid.YellowGridTop(self, (float(((self.width / 3) + ((self.width / 3) / 8))- 57.5)+ 450), ((float((self.height) - (self.height / 40)))- 450))
        Grid.BlueGridTop = Grid.BlueGridTop(self, (float(((self.width / 3) + ((self.width / 3) / 8))- 57.5)- 225), ((float((self.height) - (self.height / 40)))- 450))
        Grid.GreenGridTop = Grid.GreenGridTop(self, (float(((self.width / 3) + ((self.width / 3) / 8))- 57.5)+ 225), ((float((self.height) - (self.height / 40)))- 450))

        Grid.RedGrid = Grid.RedGrid(self, (float(((self.width / 3) + ((self.width / 3) / 8))- 115)), (float((self.height) - (self.height / 40))))
        Grid.YellowGrid = Grid.YellowGrid(self, (float(((self.width / 3) + ((self.width / 3) / 8))- 115)+ 450), (float((self.height) - (self.height / 40))))
        Grid.BlueGrid = Grid.BlueGrid(self, (float(((self.width / 3) + ((self.width / 3) / 8))- 115)- 225), (float((self.height) - (self.height / 40))))
        Grid.GreenGrid = Grid.GreenGrid(self, (float(((self.width / 3) + ((self.width / 3) / 8))- 115)+ 225), (float(self.height) - (self.height / 40)))
        
        # Player update key

        self.Is1Update = False
        self.Is2Update = False
        self.Is3Update = False
        self.Is4Update = False


        # Create front layers
        background.frontlayer1 = background.frontlayer1(0, (0 + float(self.height / 20)), float(((self.width / 3) / 2) - self.width * 0.002), self.height)
        background.frontlayer2 = background.frontlayer2(float(((self.width / 3) * 2) + ((self.width / 3) / 2) + self.width * 0.002), (0 + float(self.height / 20)), float(self.width / 3), self.height)
        background.frontlayer3 = background.frontlayer3(0, (float(self.height - (self.height / 20))) , self.width, (float(self.height / 20)))

        #Create the tower
        tower.Tower_red = tower.Tower_red(float(self.width / 3), (0 + float(self.height / 20)), (float(self.width / 3) / 2), (float(self.height - (self.height / 10))))
        tower.Tower_green = tower.Tower_green(float(self.width / 3)  + (float(self.width / 3) / 2), (0 + float(self.height / 20)), (float(self.width / 3) / 2), (float(self.height - (self.height / 10))))
        tower.Tower_blue = tower.Tower_blue(float((self.width / 3) / 2), (0 + float(self.height / 20)), (float(self.width / 3) / 2), (float(self.height - (self.height / 10))))
        tower.Tower_yellow = tower.Tower_yellow(float((self.width / 3) * 2), (0 + float(self.height / 20)), (float(self.width / 3) / 2), (float(self.height - (self.height / 10))))

        player1.player_1 = player1.player_1((float((self.width / 3) + ((self.width / 3) / 8))), (float(self.height) - (self.height / 40)),
							        (float(self.width * 0.015)), (float(self.width * 0.005)))
        player2.player_2 = player2.player_2((float((self.width / 3) + ((self.width / 3) / 8)) - (float(self.width * 0.0125))),
							        (float(self.height) - (self.height / 40)) - (float(self.width * 0.0125)), 
							        (float(self.width * 0.0125) * 2), (float(self.width * 0.0125) * 2), (float(self.width * 0.005)))
        player3.player_3 = player3.player_3((float((self.width / 3) + ((self.width / 3) / 8))), (float(self.height) - (self.height / 40)),
							        (float(self.width * 0.015)), 0)
        player4.player_4 = player4.player_4((float((self.width / 3) + ((self.width / 3) / 8)) - (float(self.width * 0.0125))),
							        (float(self.height) - (self.height / 40)) - (float(self.width * 0.0125)), 
							        (float(self.width * 0.0125) * 2), (float(self.width * 0.0125) * 2), 0)

    
        

	# Update logic of game
    def update(self):
        background.frontlayer1.update()
        background.frontlayer2.update()
        background.frontlayer3.update()


        tower.Tower_red.update()
        tower.Tower_green.update()
        tower.Tower_blue.update()
        tower.Tower_yellow.update()
      
        Grid.RedGrid.update()
        Grid.YellowGrid.update()
        Grid.BlueGrid.update()
        Grid.GreenGrid.update()

        Grid.RedGridTop.update()
        Grid.YellowGridTop.update()
        Grid.BlueGridTop.update()
        Grid.GreenGridTop.update()
      
      
      
        #self.Player1.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1] and not self.Is1Update:
            self.Is2Update = True
            self.Is3Update = True
            self.Is4Update = True

            player1.player_1.update(float((self.width / 3) / 2), 
						        float(self.width / 3), 
						        float(self.width / 3)  + (float(self.width / 3) / 2), 
						        float((self.width / 3) * 2), 
						        float((self.width / 3) / 4), 
						        float((self.height / 17)), 
						        float((self.width / 3) + ((self.width / 3) / 4)), 
						        float((self.width / 3) / 2), 
						        (float((self.width / 3) + ((self.width / 3) / 8)) - (float((self.width / 3) / 4))), 
						        (float((self.width / 3) + ((self.width / 3) / 8)) + (float((self.width / 3) / 4)) * 4), 
						        float((self.width / 3) / 8, ))
        else:
            if not keys[pygame.K_1]:
                self.Is1Update = False
        if keys[pygame.K_2] and not self.Is2Update:
            self.Is1Update = True
            self.Is3Update = True
            self.Is4Update = True
            player2.player_2.update(float((self.width / 3) / 2), 
						        float(self.width / 3), 
						        float(self.width / 3)  + (float(self.width / 3) / 2), 
						        float((self.width / 3) * 2), 
						        float((self.width / 3) / 4), 
						        float((self.height / 17)), 
						        float((self.width / 3) + ((self.width / 3) / 4) - (float(self.width * 0.0125))), 
						        float((self.width / 3) / 2), 
						        (float((self.width / 3) + ((self.width / 3) / 8)) - (float((self.width / 3) / 4)) - (float(self.width * 0.0125) * 2)), 
						        (float((self.width / 3) + ((self.width / 3) / 8)) + (float((self.width / 3) / 4)) * 4), 
						        float((self.width / 3) / 8, ))

        else:
            if not keys[pygame.K_2]:
                self.Is2Update = False

        if keys[pygame.K_3] and not self.Is3Update:
            self.Is1Update = True
            self.Is2Update = True
            self.Is4Update = True
            player3.player_3.update(float((self.width / 3) / 2), 
						        float(self.width / 3), 
						        float(self.width / 3)  + (float(self.width / 3) / 2), 
						        float((self.width / 3) * 2), 
						        float((self.width / 3) / 4), 
						        float((self.height / 17)), 
						        float((self.width / 3) + ((self.width / 3) / 4)), 
						        float((self.width / 3) / 2), 
						        (float((self.width / 3) + ((self.width / 3) / 8)) - (float((self.width / 3) / 4))), 
						        (float((self.width / 3) + ((self.width / 3) / 8)) + (float((self.width / 3) / 4)) * 4), 
						        float((self.width / 3) / 8, ))
        else:
            if not keys[pygame.K_3]:
                self.Is3Update = False

        if keys[pygame.K_4] and not self.Is4Update:
            self.Is1Update = True
            self.Is2Update = True
            self.Is3Update = True
            player4.player_4.update(float((self.width / 3) / 2), 
						        float(self.width / 3), 
						        float(self.width / 3)  + (float(self.width / 3) / 2), 
						        float((self.width / 3) * 2), 
						        float((self.width / 3) / 4), 
						        float((self.height / 17)), 
						        float((self.width / 3) + ((self.width / 3) / 4) - (float(self.width * 0.0125))), 
						        float((self.width / 3) / 2), 
						        (float((self.width / 3) + ((self.width / 3) / 8)) - (float((self.width / 3) / 4)) - (float(self.width * 0.0125) * 2)), 
						        (float((self.width / 3) + ((self.width / 3) / 8)) + (float((self.width / 3) / 4)) * 4), 
						        float((self.width / 3) / 8, ))

        else:
            if not keys[pygame.K_4]:
                self.Is4Update = False

        if keys[pygame.K_n]:
            other.turns.turn()

               

    def draw(self):
        # Clearing the screen
        self.screen.fill((0, 0, 0))
        button.update(self)
        # Draw elements
        background.frontlayer1.draw(self.screen)
        background.frontlayer2.draw(self.screen)
        background.frontlayer3.draw(self.screen)
     

        #Draw tower 
        tower.Tower_red.draw(self.screen)
        tower.Tower_green.draw(self.screen)
        tower.Tower_blue.draw(self.screen)
        tower.Tower_yellow.draw(self.screen)


        Grid.RedGrid.draw(self.screen)
        Grid.YellowGrid.draw(self.screen)
        Grid.BlueGrid.draw(self.screen)
        Grid.GreenGrid.draw(self.screen)

        Grid.RedGridTop.draw(self.screen)
        Grid.YellowGridTop.draw(self.screen)
        Grid.BlueGridTop.draw(self.screen)
        Grid.GreenGridTop.draw(self.screen)





# Draw Players
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1] and not self.Is1Down:
            if other.turns.player1_name == "":
               other.turns.naming(1)
            self.Is1Down = True
            player1.player_1.draw(self.screen)
           
        else:
            if self.Is1Down:
                player1.player_1.draw(self.screen)

        if keys[pygame.K_2] and not self.Is2Down:
            if other.turns.player2_name == "":
               other.turns.naming(2)
            self.Is2Down = True
            player2.player_2.draw(self.screen)

        else:
            if self.Is2Down:
                player2.player_2.draw(self.screen)

        if keys[pygame.K_3] and not self.Is3Down:
            #if other.turns.player3_name == "":
            #   other.turns.naming(3)
            self.Is3Down = True
            player3.player_3.draw(self.screen)


        else:
            if self.Is3Down:
                player3.player_3.draw(self.screen)

        if keys[pygame.K_4] and not self.Is4Down:
            #if other.turns.player4_name == "":
            #   other.turns.naming(4)
            self.Is4Down = True
            player4.player_4.draw(self.screen)

        else:
            if self.Is4Down:
                player4.player_4.draw(self.screen)

       # (game, x, y, width, height, text, size, backcolor, frontcolor, callback):
     #  button.draw(game, 45, game.height * 0.9, 100, 32, "Start", 20, (0,0,0), (255,255,255), lambda game: start_chosen(game, 1))
        button.draw(self,25,100,150,25,"open sport",20,(0,0,0),(255,255,255), lambda game: other.questions.question_open(globalz.o_sport,globalz.ori_o_sport,globalz.key_o_sport))
        button.draw(self,25,150,150,25,"open history",20,(0,0,0),(255,255,255), lambda game: other.questions.question_open(globalz.o_history,globalz.ori_o_history,globalz.key_o_history))
        button.draw(self,25,200,150,25,"open entertainment",20,(0,0,0),(255,255,255), lambda game: other.questions.question_open(globalz.o_entert,globalz.ori_o_entert,globalz.key_o_entert))
        button.draw(self,25,250,150,25,"open geography",20,(0,0,0),(255,255,255), lambda game: other.questions.question_open(globalz.o_geo,globalz.ori_o_geo,globalz.key_o_geo))
        button.draw(self,25,300,150,25,"mc sport",20,(0,0,0),(255,255,255), lambda game: other.questions.question_mc(globalz.mc_sport,globalz.ori_mc_sport,globalz.ans_mc_sport))
        button.draw(self,25,350,150,25,"mc entertainment",20,(0,0,0),(255,255,255), lambda game: other.questions.question_mc(globalz.mc_entert,globalz.ori_mc_entert,globalz.ans_mc_entert))
        button.draw(self,25,400,150,25,"mc history",20,(0,0,0),(255,255,255), lambda game: other.questions.question_mc(globalz.mc_history,globalz.ori_mc_history,globalz.ans_mc_history))
        button.draw(self,25,450,150,25,"mc geograhpy",20,(0,0,0),(255,255,255), lambda game: other.questions.question_mc(globalz.mc_geo,globalz.ori_mc_geo,globalz.ans_mc_geo))
        button.draw(self,25,500,150,25,"roll the dice",20,(153,0,153),(255,255,0), lambda game: other.dice.dice_roll())
        if other.questions.correct == 1:
            button.draw(self,0.85*self.width,450,150,25,"Your answer is correct!",20,(0,0,0),(255,255,255), lambda game: None)
        elif other.questions.correct == 0:
            button.draw(self,0.85*self.width,450,150,25,"Your answer is wrong!",20,(0,0,0),(255,255,255), lambda game: None)
        button.draw(self,0.85*self.width,100,30,25,str(other.dice.dice_result),20,(153,0,153),(255,255,0), lambda game: None)
        button.draw(self,0.85*self.width,500,200,25,str(other.turns.current_player_name),20,(0,0,0),(255,255,255), lambda game: None)
        button.draw(self,0.85*self.width,525,200,25,'player 1='+str(other.turns.player1_name),20,(255,255,255),(0,0,0), lambda game: None)
        button.draw(self,0.85*self.width,550,200,25,'player 2='+str(other.turns.player2_name),20,(255,255,255),(0,0,0), lambda game: None)
        button.draw(self,0.85*self.width,575,200,25,'player 3='+str(other.turns.player3_name),20,(255,255,255),(0,0,0), lambda game: None)
        button.draw(self,0.85*self.width,600,200,25,'player 4='+str(other.turns.player4_name),20,(255,255,255),(0,0,0), lambda game: None)
        # Flipping the screen
        pygame.display.flip()

        # Actual loop

    def program_loop(self):
        while not process_ev.process_events():
            self.update()
            self.draw()

# Handeling pygame events
#def process_events():
#	for event in pygame.event.get():
#		if event.type == pygame.QUIT:
#			return True
#		#elif event.type == pygame.KEYDOWN:
#		#	game.Player1.key_event(event)
#	return False