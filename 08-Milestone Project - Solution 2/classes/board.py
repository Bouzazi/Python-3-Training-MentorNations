from random import randint
from os import system

class Board():
    board = []
    turn = 1
    game_state = False

    # Initialise the board (core) object
    def __init__(self):
        self.board = [' '] * 10
        self.turn = randint(1, 2)

    # Change game state
    def set_game_state(self, state):
        self.game_state = state

    # Set the marker
    def place_marker(self, marker, position):
        self.board[position] = marker

    # Display the board
    def display(self):
        system('clear')
        print('   |   |   ')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9] +'  ')
        print('   |   |   ')
        print('------------')
        print('   |   |   ')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6] +'  ')
        print('   |   |   ')
        print('------------')
        print('   |   |   ')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3] +'  ')
        print('   |   |   ')

    # Check if the player won
    def win_check(self, mark):    
        return ((self.board[7] == mark and self.board[8] == mark and self.board[9] == mark) or # across the top
        (self.board[4] == mark and self.board[5] == mark and self.board[6] == mark) or # across the middle
        (self.board[1] == mark and self.board[2] == mark and self.board[3] == mark) or # across the bottom
        (self.board[7] == mark and self.board[4] == mark and self.board[1] == mark) or # down the middle
        (self.board[8] == mark and self.board[5] == mark and self.board[2] == mark) or # down the middle
        (self.board[9] == mark and self.board[6] == mark and self.board[3] == mark) or # down the right side
        (self.board[7] == mark and self.board[5] == mark and self.board[3] == mark) or # diagonal
        (self.board[9] == mark and self.board[5] == mark and self.board[1] == mark)) # diagonal

    # Check whether empty or not
    def space_check(self, position):
        return self.board[position] == ' '

    # Check for a draw
    def full_board_check(self):
        for i in range(1, 10):
            if self.space_check(i):
                return False
        return True

    # Get player choice
    def player_choice(self):
        position = 0
        while position not in [1,2,3,4,5,6,7,8,9] or not self.space_check(position):
            position = int(input('Player ' + str(self.turn) + ',Choose your next position: (1-9) '))
        return position

    # Handle player turn code
    def do_turn(self, player):
        self.display()
        position = self.player_choice()
        self.place_marker(player.marker, position)

        if  self.win_check(player.marker):
            self.display()
            print('Congratulations! Player ' + str(self.turn) +' has won the game!')
            self.set_game_state(False)
        else:
            if self.full_board_check():
                self.display()
                print('It\'s a draw!')
            else:
                self.turn = 2 if self.turn == 1 else 1 