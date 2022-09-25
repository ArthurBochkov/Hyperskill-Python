class TicTacToe:

    def __init__(self):
        self.board = []
        self.line = ''
        self.mover = ''

    def loadBoard(self, line):
        self.board = [line[0:3], line[3:6], line[6:9]]
        self.line = line

    def printHead(self):
        print('---------')

    def printLine(self, num):
        print(f'| {self.board[num][0]} {self.board[num][1]} {self.board[num][2]} |')

    def printResult(self):
        if not (-1 <= self.line.count('X') - self.line.count('O') <= 1):
            return 'Impossible'

        win = ''
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] in 'XO':
                print('q', i)
                win += self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] in 'XO':
                print('w', i)
                win += self.board[0][i]
        if len(win) > 1:
            return 'Impossible'
        elif len(win) == 1:
            return win + ' wins'

        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] in 'XO':
            return f'{self.board[0][0]} wins'
        if self.board[2][0] == self.board[1][1] == self.board[0][2] and self.board[2][0] in 'XO':
            return f'{self.board[2][0]} wins'

        if (self.board[0] + self.board[1] + self.board[2]).count(' ') > 0:
            return ''

        return 'Draw'

    def printBoard(self):
        self.printHead()
        self.printLine(0)
        self.printLine(1)
        self.printLine(2)
        self.printHead()

    def move(self):
        self.mover = 'X' if self.mover != 'X' else 'O'
        while True:
            move = input().split()
            if len(move) < 2 or not move[0].isdigit() or not move[1].isdigit():
                print('You should enter numbers!')
                continue

            y = int(move[0]) - 1
            x = int(move[1]) - 1

            if not ((0 <= x <= 2) and (0 <= y <= 2)):
                print('Coordinates should be from 1 to 3!')
                continue

            if self.board[y][x] in 'XO':
                print('This cell is occupied! Choose another one!')
                continue

            self.board[y] = self.board[y][:x] + self.mover + self.board[y][x + 1:]
            self.printBoard()
            break

    def start(self):
        self.loadBoard('         ')
        self.printBoard()
        while True:
            self.move()
            if self.printResult():
                print(self.printResult())
                break

game = TicTacToe()
game.start()
