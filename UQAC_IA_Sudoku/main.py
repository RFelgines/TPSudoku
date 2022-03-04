import environment.env as env


def printGrid(grid):
    print('-------------------------')
    for i in range(9):
        print("|", end=' ')
        for j in range(9):
            print(grid[i][j].getNumber(), end=' ')
            if (j + 1) % 3 == 0:
                print("|", end=' ')
        if (i + 1) % 3 == 0:
            print()
            print('-------------------------')
        else:
            print()


def readSudokuFile(environment):
    newSudokuGrid = []
    with open("Sudoku.txt") as SudokuFile:
        for line in SudokuFile:
            newSudokuGrid.append(list(line.rstrip()))
    for i in range(9):
        for j in range(9):
            environment.placeElement((i, j), newSudokuGrid[i][j])


if __name__ == "__main__":
    env = env.env()
    readSudokuFile(env)
    printGrid(env.getGrid())
