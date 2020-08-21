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
        current_move = input("Which space would you like to move to?")
        if current_move <= '9' and current_move >= '1':
            current_move = int(current_move)
            if board[(current_move-1)] != "O" or "X":
                board[(current_move-1)] = "O"
                DisplayBoard(board)
                break
        else: 
            print('try again')
        
# # the function accepts the board current status, asks the user about their move, 
# # checks the input and updates the board according to the user's decision


def MakeListOfFreeFields(board):
    free = []
    for number in range(1,10):
        if board[number] not in ['O','X']:
            free.append(number)
    return free

# #
# # the function browses the board and builds a list of all the free squares; 
# # the list consists of tuples, while each tuple is a pair of row and column numbers
# #


def VictoryFor(board, sign):
    victory = False
    global victor
    victor = None
    while victory == False:
        if board[0] == board [1] == board [2]:
            victor = board[0]
            victory = True
        elif board[3] == board [4] == board [5]:
            victor = board[3]
            victory = True
        elif board[6] == board [7] == board [8]:
            victor = board[6]
            victory = True
        elif board[0] == board [3] == board [6]:
            victor = board[0]
            victory = True
        elif board[1] == board [4] == board [7]:
            victor = board[1]
            victory = True
        elif board[2] == board [5] == board [8]:
            victor = board[2]
            victory = True
        elif board[0] == board [4] == board [8]:
            victor = board[1]
            victory = True
        elif board[2] == board [4] == board [6]:
            victor = board[2]
            victory = True
    return victor
        




# #
# # the function analyzes the board status in order to check if 
# # the player using 'O's or 'X's has won the game
# #

# def DrawMove(board):
# #
# # the function draws the computer's move and updates the board
# #
