from random import choice


class Player:

    def __init__(self, symbol):
        self.symbol = symbol

        # there are 8 checks
        self.points = [0 for _ in range(8)]
        pass

    def mark(self, game, player_in):
        """ Marks the board depending"""
        game.board[player_in] = self.symbol

    def update_points(self, game):
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
        player_in = input('0-8 or q to exit: ')

        if player_in == 'q':
            game.active = False
        else:
            super().mark(game, int(player_in))


# TODO: Edit computer player
class ComputerPlayer(Player):

    def __init__(self, symbol):
        super().__init__(symbol)
        pass

    def mark(self, game):
        print('Computer Moves')
        player_in = choice(game.blank_cells)

        if player_in == 'q':
            game.active = False
        else:
            super().mark(game, int(player_in))