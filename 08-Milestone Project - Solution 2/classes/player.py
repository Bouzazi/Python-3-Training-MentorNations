class Player():
    # Initialise the player object
    def __init__(self, marker=' '):
        self.marker = marker

    # Get player input
    @staticmethod
    def player_input():
        marker = ''

        while not (marker == 'X' or marker == 'O'):
            marker = input('Player 1: Do you want to be X or O: ').upper()

        return ('X', 'O') if marker == 'X' else ('O', 'X')    