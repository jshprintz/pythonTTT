# PY PAC POE

#Define global variables
turn = 'X'
board = {}
win = False
move = None

# Initialize game
def init_game():
    global board, win
    win = False
    disp_message()    
    board = {
        'a1': '   ', 'b1': '   ', 'c1': '   ',
        'a2': '   ', 'b2': '   ', 'c2': '   ',
        'a3': '   ', 'b3': '   ', 'c3': '   ',
    }
    disp_board()

#AAP, before being prompted for a move,
#  I want to see the board printed out in the console, 
# so that I know what moves have been made:
def disp_board():
    global board

    print(f'''
         A   B   C

    1)  {board['a1']}|{board['b1']}|{board['c1']}   
        -----------
    2)  {board['a2']}|{board['b2']}|{board['c2']}  
        -----------
    3)  {board['a3']}|{board['b3']}|{board['c3']} 
    
    ''')

# Determines players turn
def change_turn():
    global turn

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'


# As a player (AAP), I want to see a welcome 
# message at the start:
def disp_message():
    print(''' 
    ----------------------
    Let's play Py-Pac-Poe!
    ----------------------
    ''')

# Checks to see if a player won
def check_win():
    global board, turn, win
    pass


# Inputs the move from the current player
def get_move():
    global board, turn, move
    print(f'''Player {turn}'s Move (example B2):''')
    move = input()
    move.lower()


def check_move():
    count = 0
    global board, turn, move

    # Compares the players pick to the current board
    for square in board:
        if move == square and board[square] == '   ':
            board[square] = f' {turn} '
            check_win()
            change_turn()
        elif move == square and board[square] != '   ':
            print('That square has already been picked! Please pick again.')
        else:
            count += 1
    # Not a valid pick
    if count == 9:
        print('Not a valid square! Please pick again.')


# Start game
init_game()

while win == False:
    get_move()
    check_move()
    disp_board()
    # Temporary to keep it from looping
    win = True