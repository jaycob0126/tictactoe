

class Tictactoe:

    def __init__(self, player1, player2):
        """initialize all game variables"""
        self.player1 = player1
        self.player2 = player2

        # Create board container
        self.board = [' ' for _ in range(9)]

        # Game status
        self.active = True
        self.current_player = 0
        self.blank_cells = [0]
        pass

    def show_board(self):
        """ Shows the in"""
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
        pass

    @staticmethod
    def show_board_index():
        """ Shows the index number of playing board"""
        for row in [[str(i) for i in range(7-3*j, 10-3*j)] for j in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
        pass

    def next_player(self):
        """ Selects next player to mark """

        if self.current_player == 0:
            self.player1.mark(self)
        else:
            self.player2.mark(self)

        self.current_player = 1 - self.current_player

        # After a player has marked, Update the available moves
        self.available_moves()

    def available_moves(self):
        """ Returns a list of index of cells that have not been marked"""
        self.blank_cells = [ i for i, cell in enumerate(self.board) if cell == ' ']

    def check_game_stats(self):
        """ Checks all the status of game objects and ends the game
            if a player has won or there are no available cells to mark"""

        player1_points = self.player1.update_points(self)
        player2_points = self.player2.update_points(self)

        if max(player1_points) == 3:
            print("player1 wins!")
            self.active = False
        elif max(player2_points) == 3:
            print("player2 wins!")
            self.active = False
        elif len(self.blank_cells) == 0:
            # If all cells have been marked deactivate the game
            print("Its a tie!")
            self.active = False


def play(game):
    """ function to create the game loop"""
    Tictactoe.show_board_index()

    while game.active:
        game.next_player()
        game.show_board()
        game.check_game_stats()
