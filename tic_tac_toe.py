def create_board():
    global board
    board = []
    i=1
    while i < 10:
        board.append(i)
        i += 1

create_board()
#board created, board is now global


def DisplayBoard(board):
    print("+---"*3, end = "+\n")
    print("|   "*3, end = "|\n")
    print("|", end="")
    for i in range(3):
        print(f" {board[i]} " , sep="|", end="|")
    print("\n", end ="")
    print("|   "*3, end = "|\n")
    print("+---"*3, end = "+\n")
    print("|   "*3, end = "|\n")
    print("|", end="")
    for i in range(3,6):
        print(f" {board[i]} " , sep="|", end="|")
    print("\n", end ="")
    print("|   "*3, end = "|\n")
    print("+---"*3, end = "+\n")
    print("|   "*3, end = "|\n")
    print("|", end="")
    for i in range(6,9):
        print(f" {board[i]} " , sep="|", end="|")
    print("\n", end ="")
    print("|   "*3, end = "|\n")
    print("+---"*3, end = "+\n")    
    

DisplayBoard(board)

def EnterMove(board):
    #global current_move
    while True:
        current_move = int(input("Which space would you like to move to?"))
        if current_move <= 9 and current_move >= 1:
            board[current_move-1] = "O"
            DisplayBoard(board)
            break
        
EnterMove(board)

# # the function accepts the board current status, asks the user about their move, 
# # checks the input and updates the board according to the user's decision


# def MakeListOfFreeFields(board):
# #
# # the function browses the board and builds a list of all the free squares; 
# # the list consists of tuples, while each tuple is a pair of row and column numbers
# #

# def VictoryFor(board, sign):
# #
# # the function analyzes the board status in order to check if 
# # the player using 'O's or 'X's has won the game
# #

# def DrawMove(board):
# #
# # the function draws the computer's move and updates the board
# #