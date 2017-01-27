import pygame, math, sys, other

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
    def __init__(self, screen, baseX, baseY, x, y, color, radius, border):
        self.X = x
        self.Y = y
        self.Radius = radius
        self.Border = border
        self.baseX = baseX
        self.baseY = baseY
    def getX(self): return self.X

    def getY(self): return self.Y

    def draw(self, screen):
        pygame.draw.circle(screen, black, [int((self.baseX + self.X)), int((self.baseY - self.Y))], self.Radius, self.Border)

    def update(self):
        return True

# Create a Grid class to render cells on the grid ( 2, 10 blocks/positions)
class RedGrid:
    GridLength = 10
    GridWidth = 2

    cell_list = []
    def __init__(self, screen, baseX, baseY):

        for row in range(1, RedGrid.GridWidth + 1):
            for column in range(1, RedGrid.GridLength + 1):
                RedGrid.cell_list.append(Cell(screen, baseX, baseY, row * 115, column * 45, white, 5, 0))

    def draw():
        for cells in RedGrid.cell_list:
            cells.draw(other.screen)

    def update(self):
        return True

class YellowGrid:
    GridLength = 10
    GridWidth = 2

    cell_list = []
    def __init__(self, screen, baseX, baseY):

        for row in range(1, YellowGrid.GridWidth + 1):
            for column in range(1, YellowGrid.GridLength + 1):
                YellowGrid.cell_list.append(Cell(screen, baseX, baseY, row * 115, column * 45, white, 5, 0))

    def draw():
        for cells in YellowGrid.cell_list:
            cells.draw(other.screen)

    def update(self):
        return True

class BlueGrid:
    GridLength = 10
    GridWidth = 2

    cell_list = []
    def __init__(self, screen, baseX, baseY):


        for row in range(1, BlueGrid.GridWidth + 1):
            for column in range(1, BlueGrid.GridLength + 1):
                BlueGrid.cell_list.append(Cell(screen, baseX, baseY, row * 115, column * 45, white, 5, 0))

    def draw():
        for cells in BlueGrid.cell_list:
            cells.draw(other.screen)

    def update(self):
        return True

class GreenGrid:
    GridLength = 10
    GridWidth = 2

    cell_list = []
    def __init__(self, screen, baseX, baseY):


        for row in range(1, GreenGrid.GridWidth + 1):
            for column in range(1, GreenGrid.GridLength + 1):
                GreenGrid.cell_list.append(Cell(screen, baseX, baseY, row * 115, column * 45, white, 5, 0))

    def draw():
        for cells in GreenGrid.cell_list:
            cells.draw(other.screen)

    def update(self):
        return True




class RedGridTop:
    cell_list = []
    GridLength = 5
    GridWidth = 1
    def __init__(self, screen, baseX, baseY):

        for row in range(1, RedGridTop.GridWidth + 1):
            for column in range(1, RedGridTop.GridLength + 1):
                RedGridTop.cell_list.append(Cell(screen, baseX, baseY, row * 115, column * 45, white, 5, 0))

    def draw():
        for cells in RedGridTop.cell_list:
            cells.draw(other.screen)
            
    def update(self):
        return True

class YellowGridTop:
    GridLength = 5
    GridWidth = 1

    cell_list = []
    def __init__(self, screen, baseX, baseY):


        for row in range(1, YellowGridTop.GridWidth + 1):
            for column in range(1, YellowGridTop.GridLength + 1):
                YellowGridTop.cell_list.append(Cell(screen, baseX, baseY, row * 115, column * 45, white, 5, 0))

    def draw():
        for cells in YellowGridTop.cell_list:
            cells.draw(other.screen)

    def update(self):
        return True

class BlueGridTop:
    GridLength = 5
    GridWidth = 1

    cell_list = []
    def __init__(self, screen, baseX, baseY):


        for row in range(1, BlueGridTop.GridWidth + 1):
            for column in range(1, BlueGridTop.GridLength + 1):
                BlueGridTop.cell_list.append(Cell(screen, baseX, baseY, row * 115, column * 45, white, 5, 0))

    def draw():
        for cells in BlueGridTop.cell_list:
            cells.draw(other.screen)

    def update(self):
        return True

class GreenGridTop:
    GridLength = 5
    GridWidth = 1

    cell_list = []
    def __init__(self, screen, baseX, baseY):


        for row in range(1, GreenGridTop.GridWidth + 1):
            for column in range(1, GreenGridTop.GridLength + 1):
                GreenGridTop.cell_list.append(Cell(screen, baseX, baseY, row * 115, column * 45, white, 5, 0))

    def draw():
        for cells in GreenGridTop.cell_list:
            cells.draw(other.screen)

    def update(self):
        return True
