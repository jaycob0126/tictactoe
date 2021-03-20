from game import Tictactoe, play
from player import HumanPlayer, ComputerPlayer


if __name__ == "__main__":
    player1 = HumanPlayer('x')
    player2 = ComputerPlayer('0')
    game = Tictactoe(player1, player2)
    play(game)
    pass