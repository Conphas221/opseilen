import pygame, math, sys

red = (255,0,0) #configures some colors
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)


class Empty:
    def __init__(self):
        self.IsEmpty = True
empty = Empty()

class Node:
    def __init__(self, value, tail):
        self.IsEmpty = False
        self.Value = value
        self.Tail = tail 

# Create a Cell class
class Cell:
    def __init__(self, screen, baseX, baseY, x, y, color, border):
        self.Length = 15
        self.Width = 15
        self.X = x
        self.Y = y
        self.Border = border
        self.baseX = baseX
        self.baseY = baseY
    def getX(self): return self.X

    def getY(self): return self.Y

    def draw(self, screen):
        pygame.draw.rect(screen, black, [(self.baseX + self.X), (self.baseY + self.Y), self.Width, self.Length], self.Border)

    def update(self):
        return True

# Create a Grid class to render cells on the grid ( 2, 10 blocks/positions)
class RedGrid:
    def __init__(self, screen, baseX, baseY):
        self.GridLength = 10
        self.GridWidth = 2

        self.cell_list = []

        for row in range(1, self.GridWidth + 1):
            for column in range(1, self.GridLength + 1):
                self.cell_list.append(Cell(screen, baseX, baseY, row * 50, column * 70, white, 3))

    def get(self, x, y):
        for pos in self.cell_list:
            if pos.X == x * 2 and pos.Y == y * 8:
                return pos

        return False

    def draw(self, screen):
        for cells in self.cell_list:
            cells.draw(screen)

    def update(self):
        return True

class YellowGrid:
    def __init__(self, screen, baseX, baseY):
        self.GridLength = 10
        self.GridWidth = 2

        self.cell_list = []

        for row in range(1, self.GridWidth + 1):
            for column in range(1, self.GridLength + 1):
                self.cell_list.append(Cell(screen, baseX, baseY, row * 50, column * 70, white, 3))

    def get(self, x, y):
        for pos in self.cell_list:
            if pos.X == x * 2 and pos.Y == y * 8:
                return pos

        return False

    def draw(self, screen):
        for cells in self.cell_list:
            cells.draw(screen)

    def update(self):
        return True

class BlueGrid:
    def __init__(self, screen, baseX, baseY):
        self.GridLength = 10
        self.GridWidth = 2

        self.cell_list = []

        for row in range(1, self.GridWidth + 1):
            for column in range(1, self.GridLength + 1):
                self.cell_list.append(Cell(screen, baseX, baseY, row * 50, column * 70, white, 3))

    def get(self, x, y):
        for pos in self.cell_list:
            if pos.X == x * 2 and pos.Y == y * 8:
                return pos

        return False

    def draw(self, screen):
        for cells in self.cell_list:
            cells.draw(screen)

    def update(self):
        return True

class GreenGrid:
    def __init__(self, screen, baseX, baseY):
        self.GridLength = 10
        self.GridWidth = 2

        self.cell_list = []

        for row in range(1, self.GridWidth + 1):
            for column in range(1, self.GridLength + 1):
                self.cell_list.append(Cell(screen, baseX, baseY, row * 50, column * 70, white, 3))

    def get(self, x, y):
        for pos in self.cell_list:
            if pos.X == x * 2 and pos.Y == y * 8:
                return pos

        return False

    def draw(self, screen):
        for cells in self.cell_list:
            cells.draw(screen)

    def update(self):
        return True
