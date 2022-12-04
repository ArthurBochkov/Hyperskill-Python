import random

class TicTacToe:

    lines = (((0,0), (0,1), (0,2)),
             ((1,0), (1,1), (1,2)),
             ((2,0), (2,1), (2,2)),
             ((0,0), (1,0), (2,0)),
             ((0,1), (1,1), (2,1)),
             ((0,2), (1,2), (2,2)),
             ((0,0), (1,1), (2,2)),
             ((0,2), (1,1), (2,0)))

    def __init__(self):
        self.board = []
        self.mover = ''
        self.players = ()

    def load(self):
        line = '         '
        self.board = [line[0:3], line[3:6], line[6:9]]
        self.printBoard()

    def printHead(self):
        print('---------')

    def printLine(self, num):
        print(f'| {self.board[num][0]} {self.board[num][1]} {self.board[num][2]} |')

    def printBoard(self):
        self.printHead()
        self.printLine(0)
        self.printLine(1)
        self.printLine(2)
        self.printHead()

    def getResult(self):
        count_x = (''.join(self.board)).count('X')
        count_o = (''.join(self.board)).count('O')
        if not (-1 <= count_x - count_o <= 1):
            return 'Impossible'

        win = ''
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] in 'XO':
                win += self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] in 'XO':
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

    def printResult(self):
        if res:= self.getResult():
            print(res)
        return bool(res)

    def setMove(self, y, x):
        self.board[y] = self.board[y][:x] + self.mover + self.board[y][x + 1:]

    def human_move(self):
        while True:
            move = input('Enter the coordinates: ').split()
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

            self.setMove(y, x)
            break

    def check_win(self):
        for x in TicTacToe.lines:
            line = [self.board[xx[0]][xx[1]] for xx in x]
            if line.count(self.mover) == 2 and line.count(' ') == 1:
                for xx in x:
                    if self.board[xx[0]][xx[1]] == ' ':
                        self.setMove(xx[0], xx[1])
                return True
        return False

    def check_loss(self):
        for x in TicTacToe.lines:
            line = [self.board[xx[0]][xx[1]] for xx in x]
            if line.count('X' if self.mover == 'O' else 'O') == 2 and line.count(' ') == 1:
                for xx in x:
                    if self.board[xx[0]][xx[1]] == ' ':
                        self.setMove(xx[0], xx[1])
                return True
        return False

    def computer_move_hard(self):
        if self.check_win():
            return
        if self.check_loss():
            return
        if self.board[1][1] == ' ':
            self.setMove(1, 1)
            return
        if self.board[1][1] != ' ':
            if self.board[0][0] == ' ':
                self.setMove(0,0)
                return
            if self.board[2][2] == ' ':
                self.setMove(2, 2)
                return
            if self.board[0][2] == ' ':
                self.setMove(0, 2)
                return
            if self.board[2][0] == ' ':
                self.setMove(2, 0)
                return
        self.computer_move_easy()

    def computer_move_medium(self):
        if self.check_win():
            return
        if self.check_loss():
            return
        self.computer_move_easy()

    def computer_move_easy(self):
        while True:
            y = random.randint(0, 2)
            x = random.randint(0, 2)
            if self.board[y][x] == ' ':
                self.setMove(y, x)
                return

    def computer_move(self):
        if self.mover == 'X':
            level = self.players[0]
        else:
            level = self.players[1]
        print(f'Making move level "{level}"')
        if level == 'easy':
            self.computer_move_easy()
        elif level == 'medium':
            self.computer_move_medium()
        elif level == 'hard':
            self.computer_move_hard()

    def getConnand(self):
        while True:
            command = input().split()
            if command[0] == 'start':
                if len(command) != 3:
                    print('Bad parameters!')
                    continue
                self.players = (command[1], command[2])
                self.load()
                self.doPlay()
            if command[0] == 'exit':
                return

    def doPlayer(self):
        n = 0 if self.mover == 'X' else 1
        if self.players[n] == 'user':
            self.human_move()
        else:
            self.computer_move()

    def doPlay(self):
        self.mover = 'X'
        while True:
            self.doPlayer()
            self.printBoard()
            if self.printResult():
                break
            self.mover = 'O' if self.mover == 'X' else 'X'

    def go(self):
        self.load()
        self.getConnand()

if __name__ == '__main__':
    tictactoe = TicTacToe()
    tictactoe.go()