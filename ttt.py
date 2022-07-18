class Player:
    def __init__(self, symbol):
        # X or O
        self.symbol = symbol
class Game:
    def __init__(self):
        # doing 'str' because when we do '.join()' in
        # the display_game, '.join()' can only be used on lists of strings
        self.board = [str(x) for x in range(9)]
        self.winner = None
    def display_game(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    def move(self, value, position): #value being X or O and position being 0-8
        self.board[position] = value
    def check_set_winner(self, symbol):
        if self.board[0] == self.board[1] == self.board[2]:
            #OR 0 == 3 == 6
            #OR 0 == 4 == 8
            #OR 2 == 5 == 8
            #OR 6 == 7 == 8
            self.winner = symbol

# |  |  |  |
# |  |  |  |
# |  |  |  |
p1 = Player('O')
g = Game()
g.move(p1.symbol, 2)
g.display_game()
while not g.winner:
    move_position = input("Your move? Type a # from 0 - 8: ")
    g.move(p1.symbol, int(move_position))
    g.display_game()
    g.check_set_winner(p1.symbol)
if g.winner:
    print(f"{g.winner} wins!")