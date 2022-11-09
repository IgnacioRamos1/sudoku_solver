# First i need to input the sudoku board
# Divide each row in lists
# Then i need to check if the board is valid
    # The board is valid if:
        # Each row has no repeated numbers
        # Each column has no repeated numbers
        # Each 3x3 square has no repeated numbers
    # If it is valid, i need to solve it
    # If it is not valid, i need to print the error
# Then i need to print the solved board
    # First find next empty cell
    # Check if the value trying to input is valid
        # Is valid if:
            # The value is not in the row
            # The value is not in the column
            # The value is not in the 3x3 square
    # Use recursion to solve the board
    # Store each value in a list
# Finally print the solved board (stored in the list)


sudoku = []

class Number:
    def __init__(self, number):
        if number == 0:
            self.is_modifiable = True
        else:
            self.is_modifiable = False
        self.number = number


def map_input_to_sudoku(sudoku_str):
    for j in range (0, 81, 9):
        sudoku.append([Number(int(sudoku_str[i])) for i in range(j, j+9)])

def number_in_line(line, number):
    return number in [column.number for column in sudoku[line]]

def number_in_column(column, number):
    return number in [line[column].number for line in sudoku]

def number_in_cuadrant(cuadrant, number):

    if cuadrant == 0:
        for x in range(3):
            for y in range(3):
                if sudoku[x][y].number == number:
                    return True, [x, y]
        return False
    elif cuadrant == 1:
        for x in range(3):
            for y in range(3, 6):
                if sudoku[x][y].number == number:
                    return True, [x, y]
        return False
    elif cuadrant == 2:
        for x in range(3):
            for y in range(6, 9):
                if sudoku[x][y].number == number:
                    return True, [x, y]
        return False
    elif cuadrant == 3:
        for x in range(3, 6):
            for y in range(3):
                if sudoku[x][y].number == number:
                    return True, [x, y]
        return False
    elif cuadrant == 4:
        for x in range(3, 6):
            for y in range(3, 6):
                if sudoku[x][y].number == number:
                    return True, [x, y]
        return False
    elif cuadrant == 5:
        for x in range(3, 6):
            for y in range(6, 9):
                if sudoku[x][y].number == number:
                    return True, [x, y]
        return False
    elif cuadrant == 6:
        for x in range(6, 9):
            for y in range(3):
                if sudoku[x][y].number == number:
                    return True, [x, y]
        return False
    elif cuadrant == 7:
        for x in range(6, 9):
            for y in range(3, 6):
                if sudoku[x][y].number == number:
                    return True, [x, y]
        return False
    elif cuadrant == 8:
        for x in range(6, 9):
            for y in range(6, 9):
                if sudoku[x][y].number == number:
                    return True, [x, y]
        return False
    

def get_cuadrant(line, column):
    if line in range(3) and column in range(3):
        return 0
    elif line in range(3) and column in range(3, 6):
        return 1
    elif line in range(3) and column in range(6, 9):
        return 2
    elif line in range(3, 6) and column in range(3):
        return 3
    elif line in range(3, 6) and column in range(3, 6):
        return 4
    elif line in range(3, 6) and column in range(6, 9):
        return 5
    elif line in range(6, 9) and column in range(3):
        return 6
    elif line in range(6, 9) and column in range(3, 6):
        return 7
    elif line in range(6, 9) and column in range(6, 9):
        return 8

def new_number(n):
    return

def new_guess(line, column):
    guess = 1
    cuadrant = get_cuadrant(line, column)
    while number_in_line(line, guess) or number_in_column(column, guess) or number_in_cuadrant(cuadrant, guess):
        if sudoku[line][column].number == 9:
            guess = 0
            sudoku[line][column].number = 0
        guess += 1
        sudoku[line][column].number += 1
    return guess

def solve_sudoku():
    line = 0
    column = 0
    for line in range(9):
        column = 0
        for column in range(9):
            if (sudoku[line][column].is_modifiable):
                guess = new_guess(line, column)
                sudoku[line][column].number = guess
            column += 1
    return

def fill_obvious_cells():
    cells_filled = False
    line = 0
    column = 0
    for line in range(9):
        column = 0
        for column in range(9):
            if (sudoku[line][column].number == 0):
                possible_nums = [1,2,3,4,5,6,7,8,9]
                for num in range(1,10):
                    if number_in_line(line, num) or number_in_column(column, num) or number_in_cuadrant(get_cuadrant(line, column), num):
                        possible_nums.remove(num)
                if len(possible_nums) == 1:
                    sudoku[line][column].number = possible_nums[0]
                    cells_filled = True
    return cells_filled

def fill_evident_cells_by_row():
    cells_filled = False
    for line in sudoku:
        possible_numbers = [1,2,3,4,5,6,7,8,9]
        for column in line:
            if column.number in possible_numbers:
                possible_numbers.remove(column.number)
        if len(possible_numbers) == 1:
            for n in line:
                if n.number == 0:
                    n.number = possible_numbers[0]
                    cells_filled = True
    return cells_filled

def fill_evident_cells_by_column():
    cells_filled = False
    for column in range(9):
        possible_numbers = [1,2,3,4,5,6,7,8,9]
        for line in sudoku:
            if line[column].number in possible_numbers:
                possible_numbers.remove(line[column].number)
        if len(possible_numbers) == 1:
            for line in sudoku:
                if line[column].number == 0:
                    line[column].number = possible_numbers[0]
                    cells_filled = True
    return cells_filled

def fill_evident_cells_by_cuadrant():
    cells_filled = False
    for cuadrant in range(9):
        possible_numbers = [1,2,3,4,5,6,7,8,9]
        for number in range(1,10):
            if number_in_cuadrant(cuadrant, number):
                possible_numbers.remove(number)
        if len(possible_numbers) == 1:
            _, position_of_zero = number_in_cuadrant(cuadrant, 0)
            sudoku[position_of_zero[0]][position_of_zero[1]].number = possible_numbers[0]
            cells_filled = True
    return cells_filled

def print_sudoku():
    for i in range(9):
        print([i.number for i in sudoku[i]])

def count_zeros():
    zeros = 0
    for x in range(9):
        for y in range(9):
            if sudoku[x][y].number == 0:
                zeros += 1
    return zeros

def main():
    sudoku_str = input("Enter the sudoku: ")
    for char in sudoku_str:
        if not char.isnumeric():
            sudoku_str = sudoku_str.replace(char, '0')
    #sudoku_str = '000000000005360108408000200050047000602051070700800060510030000020000800003070000' #resolve capable
    map_input_to_sudoku(sudoku_str)
  
    print_sudoku()
    while fill_obvious_cells() or fill_evident_cells_by_row() or fill_evident_cells_by_column() or fill_evident_cells_by_cuadrant():
        continue
    print()
    print_sudoku()
        
main()