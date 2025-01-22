#tic tac toe

from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('- | - | -')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('- | - | -')
    print(board[1]+' | '+board[2]+' | '+board[3])

def choiced_marker():
    player1=''
    while player1 not in ['X','O']:
        player1=input('enter player1 marker (X or O): ')
        if player1=='X':
            player2='O'
        else:
            player2='X'
    return player1,player2


def user_validation():
    pos=''
    while pos not in range(1,10):
        pos=input('enter position (1-9): ')
        if pos.isdigit():
            pos=int(pos)
        if pos not in range(1,10):
            print('give valid position number')
        
    return pos


def game_on():
    game=''
    while game not in ['y','n']:
        game=input('type y to keep playing or type n to stop: ')
        if game=='y':
            return True
        elif game=='n':
            return False
        else:
            print('type y or n ')
        
def win_check(board,mark):
    if ((board[1]==board[2]==board[3]==mark) or    #rows
    (board[4]==board[5]==board[6]==mark) or 
    (board[7]==board[8]==board[9]==mark) or 
    (board[1]==board[4]==board[7]==mark) or        #columns
    (board[2]==board[5]==board[8]==mark) or 
    (board[3]==board[6]==board[9]==mark) or 
    (board[1]==board[5]==board[9]==mark) or        #diagonals
    (board[3]==board[5]==board[7]==mark)):
        print(f'WooHoo! You have won. "{mark}" user victory')
        return 'GG' 
    else:
        pass


def space_check(board,pos):
    while board[pos]!=' ':
        print('This slot is taken')
        pos=user_validation()
     
    return pos
    

def full_board_check(board):
    for i in range(1,10):
        if board[i]==' ':
            return True
    else:
        return False



print('Welcome to TIC TAC TOE!!!!')   
play=True
board=[' ']*10
player1_mark,player2_mark=choiced_marker()
print(f'player1: {player1_mark}')
print(f'player2: {player2_mark}')
while play:
    display_board(board)
    x=user_validation()
    x=space_check(board,x)
    board[x]=player1_mark
    g=win_check(board,player1_mark)
    if g=='GG':
        display_board(board)
        break
    a=full_board_check(board)
    if a==False:
        print('Its a Tie')
        display_board(board)
        break
    display_board(board)
    x=user_validation()
    x=space_check(board,x)
    board[x]=player2_mark
    g=win_check(board,player2_mark)
    if g=='GG':
        display_board(board)
        break
    a=full_board_check(board)
    if a==False:
        print('Its a Tie')
        display_board(board)
        break
    display_board(board)
    play=game_on()

