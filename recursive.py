import numpy

puzzle = input("Enter the sudoku: ")
for char in puzzle:
    if not char.isnumeric():
        puzzle = puzzle.replace(char, '0')

# We need to convert the string into a 2D array
puzzle = [[int(puzzle[9 * i + j]) for j in range(9)] for i in range(9)]

print(numpy.matrix(puzzle))
print()

def valid(row, col, value):
    global puzzle
    for i in range(0, 9):
        if puzzle[row][i] == value or puzzle[i][col] == value:
            return False
        
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for i in range(0, 3):
        for j in range(0, 3):
            if puzzle[row_start + i][col_start + j] == value:
                return False
    return True


def solve():
    global puzzle
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                for value in range(1, 10):
                    if valid(row, col, value):
                        puzzle[row][col] = value
                        solve()
                        puzzle[row][col] = 0
                return
    print(numpy.matrix(puzzle))

solve()
