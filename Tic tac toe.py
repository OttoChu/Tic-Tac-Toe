import os

def print_grid(grid):
    empty_line = '       |       |'
    for i in range(3):
        line = '   ' + grid[i][0] + '   |   ' + grid[i][1] + '   |   ' + grid[i][2]
        print(empty_line)
        print(line)
        print(empty_line)
        if i != 2:
            print('-----------------------')

def check_full(grid):
    for each_row in grid:
        for each_item in each_row:
            if each_item == ' ':
                return False
    return True
    
def check_win(grid):
    for each_row in grid:
        if each_row[0] != ' ' and each_row[0] == each_row[1] and each_row[0] == each_row[2]:
            return each_row[0]
# checking the columns
    for x in range(3):
        column = []
        for y in range(3):
            column.append(grid[y][x])
        if column[0] != ' ' and column[0] == column[1] and column[0] == column[2]:
            return column[0]
# checking the diagonals
    if grid[1][1] != ' ' and ((grid[1][1] == grid[0][0] and grid[1][1] == grid[2][2]) or (grid[1][1] == grid[0][2] and grid[1][1] == grid[2][0])):
        return grid[1][1]
    return None

def empty_grid():
    return [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def play():
    players = ['X', 'O']
    while True:
        grid = empty_grid()
        while True:
            for i in range(2):
                os.system('cls')
                print_grid(grid)
                print()
                winner = check_win(grid)
                if winner != None:
                    print(f"The winner is '{winner}'")
                    break
                if check_full(grid):
                    print('Draw!')
                    break
                print(f"'{players[i]}' move")
                while True:
                    coor = input('\nEnter the coordinates of chosen square (xy): ')
                    if len(coor) != 2:
                        print('Invaild input!')
                        print('Please try again!')
                    elif not(coor[0].isdigit()) or not(coor[1].isdigit()):
                        print('Invaild input!')
                        print('Please try again!')
                    elif int(coor[0]) < 1 or int(coor[0]) > 3 or int(coor[1]) < 1 or int(coor[1]) > 3:
                        print('Index out of range!')
                        print('Please try again!')
                    elif grid[int(coor[1]) - 1][int(coor[0]) - 1] != ' ':
                        print('Square is not empty!')
                        print('Please try again!')
                    else:
                        grid[int(coor[1]) - 1][int(coor[0]) - 1] = players[i]
                        break
            if winner != None or check_full(grid):
                break
        while True:
            print()
            again = input('Again? (y/n) ').upper()
            if again == 'Y' or again == 'N':
                break
        if again == 'N':
            break
    
play()