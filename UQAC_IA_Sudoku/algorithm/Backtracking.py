import UQAC_IA_Sudoku.environment.box as box
import numpy as np


def backtracking(envi, iteration=1):
    i, j = nextUnassignedValue(envi)
    if i == j is None:
        return True
    else:
        for value in range(10):
            if envi.checkPlacement((i, j), value):
                envi.placeElement((i, j), value)

                if backtracking(envi, iteration + 1):
                    return True
                envi.grid[i][j] = box.box(value=0)
        return False


def backtrackingMRV(envi, iteration=1):
    i, j = nextUnassignedValueMRV(envi)
    if i == j is None:
        return True
    else:
        for value in range(10):
            if envi.checkPlacement((i, j), value):
                envi.placeElement((i, j), value)

                if backtrackingMRV(envi, iteration + 1):
                    return True
                envi.grid[i][j] = box.box(value=0)
        return False


def nextUnassignedValue(envi):
    for i in range(9):
        for j in range(9):
            if envi.grid[i][j].getNumber() == 0:
                return i, j
    return None, None


def nextUnassignedValueMRV(envi):
    possibilities = numPossiblities(envi)
    if possibilities.any() != np.zeros((9, 9)).any():
        min = np.min(possibilities[np.nonzero(possibilities)])
        for i in range(9):
            for j in range(9):
                if possibilities[i, j] == min:
                    return i, j
    return None, None


def numPossiblities(envi):
    possibilities = np.zeros((9, 9))
    for i in range(9):
        for j in range(9):
            if envi.grid[i][j] == 0:
                for value in range(10):
                    if envi.checkPlacement((i, j), value):
                        possibilities[i][j] += 1
    return possibilities
