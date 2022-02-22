import environment as environment

if __name__ == "__main__":
    grid = environment.env.getGrid()

def printGrid():
    for i in range(9):
        for j in range(9):
            print(grid[i][j])
            print(' ')
            if not j % 3:
                print("|")
        print('\n')

def readSudokuFile():
    with open("Sudoku.txt") as SudokuFile:
        Sudoku = SudokuFile.read()
        environment.env.setGrid(Sudoku)

