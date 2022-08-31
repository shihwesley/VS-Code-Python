# build a tic tac toe game

import random


def build_board():
    board = []
    for i in range(3):
        board.append([' '] * 3)
    return board

def display_board(board):
    print('\n' * 100)
    print('   |   |')
    print(' ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2] + ' ')
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2] + ' ')
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2] + ' ')
    print('   |   |')
    print('\n' * 100)

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 11)

def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position[0]][position[1]] = marker

def win_check(board, mark):
    return ((board[0][0] == mark and board[0][1] == mark and board[0][2] == mark) or # across the top
    (board[1][0] == mark and board[1][1] == mark and board[1][2] == mark) or # across the middle
    (board[2][0] == mark and board[2][1] == mark and board[2][2] == mark) or # across the bottom
    (board[0][0] == mark and board[1][0] == mark and board[2][0] == mark) or # down the left side
    (board[0][1] == mark and board[1][1] == mark and board[2][1] == mark) or # down the middle
    (board[0][2] == mark and board[1][2] == mark and board[2][2] == mark) or # down the right side
    (board[0][0] == mark and board[1][1] == mark and board[2][2] == mark) or # diagonal
    (board[0][2] == mark and board[1][1] == mark and board[2][0] == mark)) # diagonal

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    return board[position[0]][position[1]] == ' '

def full_board_check(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

def player_choice(board):
    position = []
    while position not in [1, 2, 3] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        return position

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

def play_game():
    print('Welcome to Tic Tac Toe!')
    while True:
        the_board = build_board()
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print(turn + ' will go first.')
        play_game = input('Are you ready to play? Enter Yes or No.')
        if play_game.lower()[0] == 'y':
            game_on = True
        else:
            game_on = False
        while game_on:
            if turn == 'Player 1':
                display_board(the_board)
                position = player_choice(the_board)
                place_marker(the_board, player1_marker, position)

                if win_check(the_board, player1_marker):
                    display_board(the_board)
                    print('Congratulations! You have won the game!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 2'
            else:
                display_board(the_board)
                position = player_choice(the_board)
                place_marker(the_board, player2_marker, position)

                if win_check(the_board, player2_marker):
                    display_board(the_board)
                    print('Player 2 has won!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 1'
        if not replay():
            break

if __name__ == '__main__':
    play_game()
    print('Thanks for playing!')


