class Player:
    def __init__(self, symbol):
        # x or o
        self.symbol = symbol
class Game:
    def __init__(self):
        # doing 'str' because when we do '.join()' in
        # the display_game, '.join()' can only be used on lists of strings
        self.board = [str(x) for x in range(9)]
    def display_game(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

# |  |  |  |
# |  |  |  |
# |  |  |  |
g = Game()
g.display_game()