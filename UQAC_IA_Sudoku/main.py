import environment.env as env


def printGrid():
    print('----------------------------------------------------')
    for i in range(9):
        print("|", end=' ')
        for j in range(9):
            print(grid[i][j].number, end=' ')
            if (j+1) % 3 == 0:
                print("|", end=' ')
        if (i+1) % 3 == 0:
            print()
            print('----------------------------------------------------')
        else:
            print()


def readSudokuFile():
    with open("Sudoku.txt") as SudokuFile:
        Sudoku = SudokuFile.read()
        grid.grid.setGrid(SudokuFile)


if __name__ == "__main__":

    environment = env.env()
    grid = environment.getGrid()
    printGrid()
