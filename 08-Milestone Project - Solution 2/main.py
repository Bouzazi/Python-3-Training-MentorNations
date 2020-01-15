from classes.board import Board
from classes.player import Player

print("Welcome to Tic Tac Toe!")
while True:
    theBoard = Board()
    player1 = Player() 
    player2 = Player()
    player1.marker, player2.marker = Player.player_input()
    print('Player 1 choose '+ player1.marker + ', Player 2 choose '+player2.marker)
    print(('Player 1' if theBoard.turn == 1 else 'Player 2') + ' will play first!')
    theBoard.game_state = input('Are you ready to play? Enter Yes or No: ').lower().startswith('y')

    while theBoard.game_state:
        if theBoard.turn == 1:
            theBoard.do_turn(player1)
        else:
            theBoard.do_turn(player2)

    if not input('Do you want to play again? Enter Yes or No: ').upper().startswith('Y'):
        break