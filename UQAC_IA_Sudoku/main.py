import copy
import time

import environment.env as env
import algorithm.Backtracking as backtracking


def printGrid(grid):
    print('╔═══════╦═══════╦═══════╗')
    for i in range(9):
        print("║", end=' ')
        for j in range(9):
            print(grid[i][j].getNumber(), end=' ')
            if (j + 1) % 3 == 0:
                print("║", end=' ')
        if (i + 1) % 3 == 0:
            print()
            if (i+1) in [3, 6]:
                print('╠═══════╬═══════╬═══════╣')
            else:
                print('╚═══════╩═══════╩═══════╝')
        else:
            print()


def readSudokuFile(environment):
    newSudokuGrid = []
    with open("Sudoku.txt") as SudokuFile:
        for line in SudokuFile:
            newSudokuGrid.append(list(line.rstrip()))
    for i in range(9):
        for j in range(9):
            value = int(newSudokuGrid[i][j])
            environment.placeElement((i, j), value)


if __name__ == "__main__":
    env = env.env()
    good = False
    while not good:
        mode = input("Mode ? (0 : Read Sudoku File / 1 : Generate Sudoku)\n")
        if mode == "0" or mode == "1":
            good = True

    if mode == "1":
        good = False
        diff = input("Difficulty ?\n0:Easy\n1:Medium\n2:Hard\n3:Very Hard\n4:Maximum possible difficulty\n")
        if diff == "0" or diff == "1" or diff == "2" or diff == "3" or diff == "4":
            good = True

    if mode == "0":
        readSudokuFile(env)
    if mode == "1":
        env.generateSudoku()
        env.putZeros(int(diff))
    envCopy = copy.copy(env)
    """
    0:Facile
    1:Moyen
    2:Difficile
    3:Hardcore
    4:Maximum Difficulty
    """
    print("Sudoku initial : ")
    printGrid(env.getGrid())

    start_time = time.perf_counter_ns()
    backtracking.backtracking(env)
    end_time = time.perf_counter_ns()
    print("Backtracking done, elapsed time : " + str(end_time-start_time) + "ns.")
    printGrid(env.getGrid())

    start_time = time.perf_counter_ns()
    backtracking.backtrackingMRV(envCopy)
    end_time = time.perf_counter_ns()
    print("Backtracking MRV done, elapsed time : " + str(end_time-start_time) + "ns.")
    printGrid(envCopy.getGrid())

