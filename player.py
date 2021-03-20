from random import choice


class Player:

    def __init__(self, symbol):
        self.symbol = symbol

        # there are 8 checks 3 rows, 3 columns, 2 diagonals
        self.points = [0 for _ in range(8)]
        pass

    def mark(self, game, player_in):
        """ Marks the board depending"""
        game.board[player_in] = self.symbol

    def update_points(self, game):
        """ Updates the player point list """

        # diagonal points
        diag_point1 = 0
        diag_point2 = 0

        for i in range(3):
            row_point = 0
            col_point = 0
            for j in range(3):
                row_index = j + 3*i
                col_index = i + 3*j
                if game.board[row_index] == self.symbol:
                    row_point += 1

                if game.board[col_index] == self.symbol:
                    col_point += 1

            self.points[i] = row_point
            self.points[i+3] = col_point

            diag_index1 = 4*i
            diag_index2 = 2*(i+1)

            if game.board[diag_index1] == self.symbol:
                diag_point1 += 1
            if game.board[diag_index2] == self.symbol:
                diag_point2 += 1

        self.points[-2] = diag_point1
        self.points[-1] = diag_point2
        return self.points


class HumanPlayer(Player):

    def __init__(self, symbol):
        super().__init__(symbol)
        pass

    def mark(self, game):
        """ Marking with input validation"""

        while True:
            player_in = input('1-9 or q to exit: ')
            if player_in == 'q':
                sure_to_exit = input('are you sure to exit game? y/n: ')
                if sure_to_exit == 'y':
                    print('Game terminated')
                    game.active = False
                    break
                elif sure_to_exit == 'n':
                    continue
            else:
                try:
                    # Map the layout of a keyboard numpad
                    # haha just practicing some list comprehension
                    cell_index = [item for row in [[i for i in range(6-3*j, 9 - 3*j)] for j in range(3)] for item in row]
                    player_input = int(player_in)

                    # Check if user input is within 1-9 range
                    if player_input < 1 or player_input > 9:
                        print('Invalid number, Please input 1-9')
                        continue

                    if cell_index[player_input-1] not in game.blank_cells:
                        print("Cell already marked")
                        continue

                    # Calls superclass' mark method
                    super().mark(game, cell_index[player_input-1])
                    break

                except ValueError:
                    # Exception if user has inputted a value other than 1-9 or q
                    print("Invalid input, Please input 1-9 or q to exit")


class ComputerPlayer(Player):
    """A computer player that only plays just in random choices"""
    def __init__(self, symbol):
        super().__init__(symbol)
        pass

    def mark(self, game):
        player_in = choice(game.blank_cells)

        if player_in == 'q':
            game.active = False
        else:
            super().mark(game, int(player_in))