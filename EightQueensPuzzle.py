# F. Derek Roman - GitHub Profile -  CodeNamor
# SWDV-610-3W Data Structures     Unit 8 final Project


# solving the problem of placing 8 queens on a chess board that are not able to attack one another
# define necessary imports for this application
import copy

def take_input():
    #get input on what size  the chess board should be
    while True:
        # try / catch block to raise error if needed
        # this is a check on the size of the chess board from the user input
        try:
            boardSize = int(input('What is the size of the chessboard? n = \n'))
            # if the board size is equal to 1?
            if boardSize == 1:
                print("Trivial solution, choose a board size of atleast 4")
            # if the board size is less than or equal to 3
            if boardSize <= 3:
                print("Enter a value such that size>=4")
                continue
            # otherwise return the input size
            return boardSize
        # raise a ValueError exception type
        except ValueError:
            print("Invalid value entered. Enter again")
def get_board(boardSize):
    # this will return the board size
    board = [0]*boardSize
    for ix in range(boardSize):
        board[ix] = [0]*boardSize
    return board
#print the solutions to be seen in the screen
def print_solutions(solutions, size):
    # for each solution
    for sol in solutions:
        #for each row in the solution
        for row in sol:
            #print the row of the solution
            print(row)
        #prints a blank line after the board grid
        print()
# is it safe to put the queen in the spot?
def is_safe(board, row, col, size):
# algorithm to solve for the problem of placing queens on the board
    for iy in range(col):
        if board[row][iy] == 1:
            return False  
    ix, iy = row, col
    while ix >= 0 and iy >= 0:
        if board[ix][iy] == 1:
            return False
        ix-=1
        iy-=1  
    jx, jy = row,col
    while jx < size and jy >= 0:
        if board[jx][jy] == 1:
            return False
        jx+=1
        jy-=1
    # otherwise put the queen in the spot
    return True
def solve(board, col, size):
#algorithm to solve the problem based upon the size of the board
    if col >= size:
        return
    # for the index in the range of the size of the board
    for i in range(size):
        if is_safe(board, i, col, size):
            board[i][col] = 1
            if col == size-1:
                #adds the solution to the game board
                add_solution(board)
                board[i][col] = 0
                return
            # recursive algorithm to solve the problem. 
            solve(board, col+1, size)
            board[i][col] = 0
# add the solution to the game board
def add_solution(board):
    global solutions
    saved_board = copy.deepcopy(board)
    solutions.append(saved_board)
#calls to the above functions to solve the problem
size = take_input()
board = get_board(size)
solutions = []
solve(board, 0, size)
print_solutions(solutions, size)
#print the solutions found with string formating
print("Total solutions = {}".format(len(solutions))) 