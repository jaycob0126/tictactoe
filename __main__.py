from game import Game, play
from player import HumanPlayer, ComputerPlayer


if __name__ == "__main__":
    player1 = HumanPlayer('x')
    player2 = HumanPlayer('0')
    tictactoe = Game(player1, player2)
    play(tictactoe)
    pass