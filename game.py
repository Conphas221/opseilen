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

        self.RedGridTop = Grid.RedGridTop(self, (float(((self.width / 3) + ((self.width / 3) / 8))- 57.5)), ((float((self.height) - (self.height / 40)))-450))
        self.YellowGridTop = Grid.YellowGridTop(self, (float(((self.width / 3) + ((self.width / 3) / 8))- 57.5)+ 450), ((float((self.height) - (self.height / 40)))- 450))
        self.BlueGridTop = Grid.BlueGridTop(self, (float(((self.width / 3) + ((self.width / 3) / 8))- 57.5)- 225), ((float((self.height) - (self.height / 40)))- 450))
        self.GreenGridTop = Grid.GreenGridTop(self, (float(((self.width / 3) + ((self.width / 3) / 8))- 57.5)+ 225), ((float((self.height) - (self.height / 40)))- 450))

        self.RedGrid = Grid.RedGrid(self, (float(((self.width / 3) + ((self.width / 3) / 8))- 115)), (float((self.height) - (self.height / 40))))
        self.YellowGrid = Grid.YellowGrid(self, (float(((self.width / 3) + ((self.width / 3) / 8))- 115)+ 450), (float((self.height) - (self.height / 40))))
        self.BlueGrid = Grid.BlueGrid(self, (float(((self.width / 3) + ((self.width / 3) / 8))- 115)- 225), (float((self.height) - (self.height / 40))))
        self.GreenGrid = Grid.GreenGrid(self, (float(((self.width / 3) + ((self.width / 3) / 8))- 115)+ 225), (float(self.height) - (self.height / 40)))
        
        # Player update key

        self.Is1Update = False
        self.Is2Update = False
        self.Is3Update = False
        self.Is4Update = False


        # Create front layers
        self.frontlayer1 = background.frontlayer1(0, (0 + float(self.height / 20)), float(((self.width / 3) / 2) - self.width * 0.002), self.height)
        self.frontlayer2 = background.frontlayer2(float(((self.width / 3) * 2) + ((self.width / 3) / 2) + self.width * 0.002), (0 + float(self.height / 20)), float(self.width / 3), self.height)
        self.frontlayer3 = background.frontlayer3(0, (float(self.height - (self.height / 20))) , self.width, (float(self.height / 20)))

        #Create the tower
        self.Tower_red = tower.Tower_red(float(self.width / 3), (0 + float(self.height / 20)), (float(self.width / 3) / 2), (float(self.height - (self.height / 10))))
        self.Tower_green = tower.Tower_green(float(self.width / 3)  + (float(self.width / 3) / 2), (0 + float(self.height / 20)), (float(self.width / 3) / 2), (float(self.height - (self.height / 10))))
        self.Tower_blue = tower.Tower_blue(float((self.width / 3) / 2), (0 + float(self.height / 20)), (float(self.width / 3) / 2), (float(self.height - (self.height / 10))))
        self.Tower_yellow = tower.Tower_yellow(float((self.width / 3) * 2), (0 + float(self.height / 20)), (float(self.width / 3) / 2), (float(self.height - (self.height / 10))))

        self.player_1 = player1.player_1((float((self.width / 3) + ((self.width / 3) / 8))), (float(self.height) - (self.height / 40)),
							        (float(self.width * 0.015)), (float(self.width * 0.005)))
        self.player_2 = player2.player_2((float((self.width / 3) + ((self.width / 3) / 8)) - (float(self.width * 0.0125))),
							        (float(self.height) - (self.height / 40)) - (float(self.width * 0.0125)), 
							        (float(self.width * 0.0125) * 2), (float(self.width * 0.0125) * 2), (float(self.width * 0.005)))
        self.player_3 = player3.player_3((float((self.width / 3) + ((self.width / 3) / 8))), (float(self.height) - (self.height / 40)),
							        (float(self.width * 0.015)), 0)
        self.player_4 = player4.player_4((float((self.width / 3) + ((self.width / 3) / 8)) - (float(self.width * 0.0125))),
							        (float(self.height) - (self.height / 40)) - (float(self.width * 0.0125)), 
							        (float(self.width * 0.0125) * 2), (float(self.width * 0.0125) * 2), 0)

        self.smenu_active = False
        
        

	# Update logic of game
    def update(self):
        self.frontlayer1.update()
        self.frontlayer2.update()
        self.frontlayer3.update()


        tower.Tower_red.update(self.Tower_red)
        tower.Tower_green.update(self.Tower_green)
        tower.Tower_blue.update(self.Tower_blue)
        tower.Tower_yellow.update(self.Tower_yellow)
      
        Grid.RedGrid.update(self.RedGrid)
        Grid.YellowGrid.update(self.YellowGrid)
        Grid.BlueGrid.update(self.BlueGrid)
        Grid.GreenGrid.update(self.GreenGrid)

        Grid.RedGridTop.update(self.RedGridTop)
        Grid.YellowGridTop.update(self.YellowGridTop)
        Grid.BlueGridTop.update(self.BlueGridTop)
        Grid.GreenGridTop.update(self.GreenGridTop)
      
       
        keys = pygame.key.get_pressed()
        if other.turns.current_player == 1:
            if not self.Is1Update:
                self.Is2Update = True
                self.Is3Update = True
                self.Is4Update = True

                self.player_1.update(float((self.width / 3) / 2), 
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
        if other.turns.current_player == 2:
            if not self.Is2Update:
                self.Is1Update = True
                self.Is3Update = True
                self.Is4Update = True
                self.player_2.update(float((self.width / 3) / 2), 
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
        if other.turns.current_player == 3:
            if not self.Is3Update:
                self.Is1Update = True
                self.Is2Update = True
                self.Is4Update = True
                self.player_3.update(float((self.width / 3) / 2), 
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
        if other.turns.current_player == 4:
            if not self.Is4Update:
                self.Is1Update = True
                self.Is2Update = True
                self.Is3Update = True
                self.player_4.update(float((self.width / 3) / 2), 
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
        self.frontlayer1.draw(self.screen)
        self.frontlayer2.draw(self.screen)
        self.frontlayer3.draw(self.screen)
     

        #Draw tower 
        tower.Tower_red.draw(self.Tower_red)
        tower.Tower_green.draw(self.Tower_green)
        tower.Tower_blue.draw(self.Tower_blue)
        tower.Tower_yellow.draw(self.Tower_yellow)


        Grid.RedGrid.draw()
        Grid.YellowGrid.draw()
        Grid.BlueGrid.draw()
        Grid.GreenGrid.draw()

        Grid.RedGridTop.draw()
        Grid.YellowGridTop.draw()
        Grid.BlueGridTop.draw()
        Grid.GreenGridTop.draw()





## Draw Players
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1] and not self.Is1Down:
            if other.turns.player1_name == "":
               other.turns.naming(1)
            self.Is1Down = True
            self.player_1.draw(self.screen)
           
        else:
            if self.Is1Down:
                self.player_1.draw(self.screen)

        if keys[pygame.K_2] and not self.Is2Down:
            if other.turns.player2_name == "":
                other.turns.naming(2)
            self.Is2Down = True
            self.player_2.draw(self.screen)

        else:
            if self.Is2Down:
                self.player_2.draw(self.screen)

        if keys[pygame.K_3] and not self.Is3Down:
            if other.turns.player3_name == "":
               other.turns.naming(3)
            self.Is3Down = True
            self.player_3.draw(self.screen)


        else:
            if self.Is3Down:
                self.player_3.draw(self.screen)

        if keys[pygame.K_4] and not self.Is4Down:
            if other.turns.player4_name == "":
               other.turns.naming(4)
            self.Is4Down = True
            self.player_4.draw(self.screen)

        else:
            if self.Is4Down:
                self.player_4.draw(self.screen)



        # (game, x, y, width, height, text, size, backcolor, frontcolor, callback):
        #  button.draw(game, 45, game.height * 0.9, 100, 32, "Start", 20, (0,0,0), (255,255,255), lambda game: start_chosen(game, 1))
        #button.draw(self,25,100,150,25,"open sport",20,(0,0,0),(255,255,255), lambda game: other.questions.question_open(globalz.o_sport,globalz.ori_o_sport,globalz.key_o_sport))
        button.draw(self,25,100,150,25,"open settings menu",20,(0,0,0),(255,255,255), lambda game: self.smenu())
        if not other.turns.match_started:  
            button.draw(self,25,150,150,25,"Player 1 goes first",20,(0,0,0),(255,255,255), lambda game: other.turns.firstturn(1))
            button.draw(self,25,200,150,25,"Player 2 goes first",20,(0,0,0),(255,255,255), lambda game: other.turns.firstturn(2))
            button.draw(self,25,250,150,25,"Player 3 goes first",20,(0,0,0),(255,255,255), lambda game: other.turns.firstturn(3))
            button.draw(self,25,300,150,25,"Player 4 goes first",20,(0,0,0),(255,255,255), lambda game: other.turns.firstturn(4))
        #button.draw(self,25,350,150,25,"mc entertainment",20,(0,0,0),(255,255,255), lambda game: other.questions.question_mc(globalz.mc_entert,globalz.ori_mc_entert,globalz.ans_mc_entert))
        #button.draw(self,25,400,150,25,"mc history",20,(0,0,0),(255,255,255), lambda game: other.questions.question_mc(globalz.mc_history,globalz.ori_mc_history,globalz.ans_mc_history))
        #button.draw(self,25,450,150,25,"mc geograhpy",20,(0,0,0),(255,255,255), lambda game: other.questions.question_mc(globalz.mc_geo,globalz.ori_mc_geo,globalz.ans_mc_geo))
        # changed backgroundcolor of dice
        button.draw(self,25,550,165,25,"ROLL THE DICE",20,(95,158,160),(255,255,255), lambda game: other.dice.dice_roll())
        # rect to clarify where the answer of questions is shown 
        button.draw(self,0.85*self.width,275,200,25,"RIGHT OR WRONG ANSWER?",20,(0,0,0),(255,255,255), lambda game: None)
        if other.questions.correct == 1:
            button.draw(self,0.85*self.width,300,200,25,"YOUR ANSWER IS CORRECT!",20,(124,252,0),(0,0,0), lambda game: None)
        elif other.questions.correct == 0:
            button.draw(self,0.85*self.width,300,200,25,"YOUR ANSWER IS WRONG",20,(255,0,0),(0,0,0), lambda game: None)


        #displays the result of the dice roll
        button.draw(self,25,600,150,25,str(other.dice.dice_result),20,(95,158,160),(255,255,255), lambda game: None)
       

        #displays the name of the current player
        button.draw(self,0.85*self.width,70,200,30,"CURRENT PLAYER IS",25,(0,0,0),(255,255,255), lambda game: None)
        button.draw(self,0.85*self.width,100,200,30,str(other.turns.current_player_name),25,(0,0,0),(255,255,255), lambda game: None)


        #shows the name each player has entered for themselves
        button.draw(self,0.85*self.width,525,200,25,'PLAYER 1 = '+str(other.turns.player1_name),20,(255,255,255),(0,0,0), lambda game: None)
        button.draw(self,0.85*self.width,550,200,25,'PLAYER 2 = '+str(other.turns.player2_name),20,(255,255,255),(0,0,0), lambda game: None)
        button.draw(self,0.85*self.width,575,200,25,'PLAYER 3 = '+str(other.turns.player3_name),20,(255,255,255),(0,0,0), lambda game: None)
        button.draw(self,0.85*self.width,600,200,25,'PLAYER 4 = '+str(other.turns.player4_name),20,(255,255,255),(0,0,0), lambda game: None)
       


        #checks whether a player has reached the finish, and if so, draws the termination screen and displays the name of the winner
        if self.player_1.cnt >= 15 or self.player_2.cnt >= 15 or self.player_3.cnt >= 15 or self.player_4.cnt >= 15:
            self.screen.fill((255,255,255))
            button.update(self)
            if self.player_1.cnt >= 15:
                button.draw(self,0.3*self.width,0.25*self.height,500,100,'The winner is: '+str(other.turns.player1_name),50,(255,255,255),(0,0,0), lambda game: None)
            elif self.player_2.cnt >= 15:
                button.draw(self,0.2*self.width,0.25*self.height,500,100,'The winner is: '+str(other.turns.player2_name),50,(255,255,255),(0,0,0), lambda game: None)
            elif self.player_3.cnt >= 15:
                button.draw(self,0.2*self.width,0.25*self.height,500,100,'The winner is: '+str(other.turns.player3_name),50,(255,255,255),(0,0,0), lambda game: None)
            elif self.player_4.cnt >= 15:
                button.draw(self,0.2*self.width,0.25*self.height,500,100,'The winner is: '+str(other.turns.player4_name),50,(255,255,255),(0,0,0), lambda game: None)
           
            #These are the buttons on the termination screen
            import MainMenuNew
            button.draw(self,0.1*self.width,0.75*self.height,500,100,'RETURN TO MAIN MENU',50,(0,0,0),(255,255,255), lambda game: MainMenuNew.reloop())
            button.draw(self,0.5*self.width,0.75*self.height,500,100,'QUIT GAME',50,(0,0,0),(255,255,255), lambda game: sys.exit())

   
            #checks whether the settings menu has been requested by the user, and if so, opens it.
        if self.smenu_active:
            self.screen.fill((255,255,255))
            button.update(self)
            button.draw(self,0.1*self.width,0.75*self.height,500,100,'Start background music',50,(0,0,0),(255,255,255), lambda game: other.music())
            button.draw(self,0.5*self.width,0.75*self.height,500,100,'Stop background music',50,(0,0,0),(255,255,255), lambda game: other.stop_music())
            button.draw(self,0.3*self.width,0.25*self.height,500,100,'back',50,(0,0,0),(255,255,255), lambda game: self.smenu())


        # Flipping the screen
        pygame.display.flip()

        



            
    def smenu(self):
        if self.smenu_active:
            self.smenu_active = False
        elif not self.smenu_active:
            self.smenu_active = True

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