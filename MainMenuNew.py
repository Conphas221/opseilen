import pygame
import sys
import os
import main
import game
import other
import database
pygame.init()
width = 700
height = 800
screen = pygame.display.set_mode((width, height))
font = pygame.font.Font(None, 30)

def reloop():
    other.turns.player1_name = ""
    other.turns.player2_name = ""
    other.turns.player3_name = ""
    other.turns.player4_name = ""
    other.turns.player_count = 0
    other.turns.playerz = []
    other.turns.current_player = 0
    other.turns.current_player_name = ""
    other.turns.match_started = False
    game.Game.ina = 0
    game.Game.won = 0
    other.questions.correct = 2
    other.questions.player1_correct = 2
    other.questions.player2_correct = 2
    other.questions.player3_correct = 2
    other.questions.player4_correct = 2
    other.questions.pressed = False
    other.questions.dice_result = 1
    for _ in dir():
        if _[0]!='_': delattr(sys.modules[__name__], _)
    exec(open("MainMenuNew.py").read())

class Button:
    def __init__(self, text, x, y, action):
        self.X = x
        self.Y = y
        self.DefaultText = text
        self.Color = (130, 130, 130)
        self.Action = action

        self.Text = (pygame.font.Font(None, 30)).render(text, 1, self.Color)
        self.Rect = self.Text.get_rect()
        self.Rect.topleft = (x, y)

    def Update(self, events):
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                if self.Rect.collidepoint(event.pos):                    
                    self.Text = (pygame.font.Font(None, 40)).render(self.DefaultText, 1, (255, 190, 0))            
                else:
                    self.Text = (pygame.font.Font(None, 40)).render(self.DefaultText, 1, (130, 130, 130))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.Rect.collidepoint(event.pos):                    
                    return self.Action()
        return self
        
    def Draw(self, screen):
        screen.blit(self.Text, self.Rect)


class InstructionMenu:
    def __init__(self, width, height):
        self.Width = width
        self.Height = height        
        self.Image = pygame.image.load(os.path.join('Project2/spelregels.bmp'))

        self.Buttons = [Button("BACK", 10, 50, lambda : MainMenu(width, height))]
    def Update(self):
        events = pygame.event.get()
        for event in events:            
            if event.type == pygame.QUIT:
              sys.exit()
        for button in self.Buttons:
            res = button.Update(events)
            if (res != button):
                return res
        return self

    def Draw(self, screen):
        screen.blit(self.Image,(150, 50))
        for button in self.Buttons:
            button.Draw(screen)


class HighScoreMenu:
    def __init__(self, width, height):
        self.Width = width
        self.Height = height 
        #self.Image = pygame.image.load(os.path.join('project2/euromast_illustratie_02.jpg'))
        self.scorelist = database.execute_query("SELECT name,wins FROM scores ORDER BY wins DESC")
        self.playernames = []
        self.playerscores = []
        self.highscore = []

        self.Buttons = [Button("BACK", 10, 50, lambda : MainMenu(width, height))]    
    
    def update1(self):
        for entry in self.scorelist:
            #self.playernames.extend(str(entry["name"]))
            #self.playerscores.extend(str(entry["wins"]))
            highscores = (entry["name"], entry["wins"])
            self.highscore.extend(highscores)
    
    def Update(self):
        events = pygame.event.get()
        for event in events:            
            if event.type == pygame.QUIT:
                sys.exit()
        for button in self.Buttons:
            res = button.Update(events)
            if (res != button):
                return res
        return self
    
    def Draw(self, screen):
        self.update1()
        for l in range(0,10):

            screen.blit(font.render(str(self.highscore[l]),True,(0,0,0)),(150, 50*((1+l)*1.1)))
        for k in range(1,11,2):
            screen.blit(font.render("wins",True,(0,0,0)),(180, 50*((1+k)*1.1)))
            #screen.blit(self.playerscores[l],(450, 50*((1+l)*30)))
            
        for button in self.Buttons:
            button.Draw(screen)


class MainMenu:
    def __init__(self, width, height):
        self.Width = width
        self.Height = height        
        self.Image = pygame.image.load(os.path.join('project2/euromast_illustratie_02.jpg'))
        self.Buttons = [Button("PLAY", 250, 40, lambda : game.Game().program_loop()),
                        #Button("LOAD SAVE GAME", 250, 80, lambda: [game.Game().program_loop(), other.SaveGame.load()]),
                        Button("INSTRUCTIONS", 250, 110, lambda : InstructionMenu(width, height)),
                        Button("HIGH SCORE", 250, 180, lambda : HighScoreMenu(width, height)),
                        Button("QUIT", 250, 250, lambda : sys.exit())]
    def Update(self):
        events = pygame.event.get()
        for event in events:            
            if event.type == pygame.QUIT:
              sys.exit()
        for button in self.Buttons:
            res = button.Update(events)
            if (res != button):
                return res
        return self

    def Draw(self, screen):
        screen.blit(self.Image,(0, 310))
        for button in self.Buttons:
            button.Draw(screen)


scene = MainMenu(width, height)
while True:
    pygame.event.pump()
    screen.fill((255,255,255))    

    scene = scene.Update()
    scene.Draw(screen)


    pygame.display.flip()


loop()

def program():
    mainmenu = MainMenuNew()
    mainmenu.program_loop()

program()
