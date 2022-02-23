import logging

import environment.env
from environment.box import box
import numpy

class grid:
    grid = None

    def __init__(self):
        environment.env.grid = [[box() for i in range(9)] for j in range(9)]

    def getGrid(self):
       return self.grid

    def setGrid(self, grid):
        self.grid = grid

    def unique(list):
        unique_list = []
        for x in list:
            if x not in unique_list:
                unique_list.append(x)

    def availableNumbers(self, *pos): #Checks what numbers can be placed at a certain position
        availableNumbers = [1,2,3,4,5,6,7,8,9]
        x,y = pos
        column = []
        row = []
        subgrid = []

        for i in range(9):
            if grid[i][y] != 0: #There is a number
                row.append(grid[i][y])

        for i in range(9):
            if grid[x][i] != 0:
                column.append(grid[i][y])

        xSubgrid = (x // 3)*3
        ySubgrid = (y // 3)*3
        for i in range(3):
            for j in range(3):
                if grid[i + xSubgrid][j +ySubgrid] != 0:
                    row.append(grid[i + xSubgrid][j +ySubgrid])

        unusableNumbers = set(column+row+subgrid) # Numbers that you can't use
        templist = unusableNumbers+availableNumbers
        availableNumbers = self.unique(templist)
        return availableNumbers

    def LCR(self):
        ConstraintsValue = numpy.zeros(9,9)
        LCR = 0
        posLCR = 0,0
        for i in range(9):
            for j in range(9):
                ConstraintsValue[i][j] = len(self.availableNumbers(i , j))
                if ConstraintsValue[i][j] >= LCR:
                    posLCR = ConstraintsValue[i][j]
        return posLCR

    def MRV(self): #TODO
        ConstraintsValue = numpy.zeros(9,9)
        LCR = 0
        posLCR = 0,0
        for i in range(9):
            for j in range(9):
                ConstraintsValue[i][j] = len(self.availableNumbers(i , j))
                if ConstraintsValue[i][j] >= LCR:
                    posLCR = ConstraintsValue[i][j]
        return posLCR



    def checkPlacement(self, *pos,number): #Check if placement is correct
        x,y = pos
        if grid[x][y] != 0: # There is already a number at this position
            return False
        for i in range(9):
            if grid[i][y] == number:
                return False
        for i in range(9):
            if grid[x][i] == number:
                return False

        xSubgrid = (x // 3)*3
        ySubgrid = (y // 3)*3
        for i in range(3):
            for j in range(3):
                if grid[i + xSubgrid][j +ySubgrid]==number:
                    return False
        return True

    def placeElement(self,*pos, number):
        if self.checkPlacement(pos, number): # Optional if we ensure the placement is correct beforehand, may remove after testing
            x,y = pos
            grid[x][y] = number
            return True

        else:
            return False
