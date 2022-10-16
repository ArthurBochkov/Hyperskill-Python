import copy

class Game:

    def __init__(self):
        self.x = None
        self.y = None
        self.board = None
        self.knight = None
        self.num_move = None
        self.puzzle = None
        self.steps = ((+2, +1), (+2, -1), (-2, +1), (-2, -1), (+1, +2), (+1, -2), (-1, +2), (-1, -2))

    def check_num(self, num):
        if not num.isdigit():
            return False
        if int(num) < 1:
            return False
        return True

    def check_dim(self, num):
        if not num.isdigit():
            return False
        if int(num) < 1 or int(num) > 99:
            return False
        return True

    def print_line(self):
        print(' ' + '-' * ((self.x + 1) * 3 + 1))

    def print_board(self):
        self.print_line()
        for y in range(self.y):
            print(str(self.y - y) + '| ', end='')
            for x in range(self.x):
                print('_' if self.board[self.y - y - 1][x] == '_' else ' ', end='')
                print(self.board[self.y - y - 1][x] + ' ', end='')
            print('|')
        self.print_line()
        print('   ', end='')
        for i in range(self.x):
            print(' ' + str(i + 1) + ' ', end='')
        print()

    def set_knight(self, new_x, new_y):
        self.board[new_y][new_x] = 'X'
        self.knight = [new_x, new_y]
        self.num_move += 1

    def get_knight(self):
        while True:
            try:
                xy = input('Enter the knight\'s starting position:').split()
                if len(xy) != 2:
                    raise Exception
                if not self.check_num(xy[0]) or not self.check_num(xy[1]):
                    raise Exception
                if int(xy[0]) > self.x or int(xy[1]) > self.y:
                    raise Exception
                self.set_knight(int(xy[0]) - 1, int(xy[1]) - 1)
                answer = input('Do you want to try the puzzle? (y/n):')
                self.puzzle = (answer == 'y')
                if answer == 'y' or answer == 'n':
                    return
                else:
                    print('Invalid input!')
            except:
                print('Invalid position!')


    def get_board(self):
        while True:
            try:
                xy = input('Enter your board dimensions:').split()
                if not self.check_dim(xy[0]) or not self.check_dim(xy[1]):
                    raise Exception
                self.x = int(xy[0])
                self.y = int(xy[1])
                self.board = [['_' for _ in range(self.x)] for _ in range(self.y)]
                break
            except:
                print('Invalid dimensions!')

    def check_possible(self, x, y, div_x, div_y):
        return  1 if 0 <= x + div_x < self.x and 0 <= y + div_y < self.y and self.board[y + div_y][x + div_x] == '_'  else 0

    def set_possible_pos(self, mov_x, mov_y):
        new_x = self.knight[0] + mov_x
        new_y = self.knight[1] + mov_y
        if 0 <= new_x < self.x and 0 <= new_y < self.y and self.board[new_y][new_x] == '_':
            num = 0
            for step in self.steps:
                num += self.check_possible(new_x, new_y, step[0], step[1])
            self.board[new_y][new_x] = str(num)

    def set_possible(self):
        for step in self.steps:
            self.set_possible_pos(step[0], step[1])

    def do_move(self):
        while True:
            try:
                xy = input('Enter your next move:').split()
                if len(xy) != 2:
                    raise Exception
                if not self.check_num(xy[0]) or not self.check_num(xy[1]):
                    raise Exception
                if int(xy[0]) > self.x or int(xy[1]) > self.y:
                    raise Exception
                new_x = int(xy[0]) - 1
                new_y = int(xy[1]) - 1
                if self.board[new_y][new_x] == '_' or self.board[new_y][new_x] == 'X'  or self.board[new_y][new_x] == '*':
                    raise Exception
                for y in range(self.y):
                    for x in range(self.x):
                        if self.board[y][x] == 'X':
                            self.board[y][x] = '*'
                        elif self.board[y][x] not in '_*':
                            self.board[y][x] = '_'
                self.set_knight(new_x, new_y)
                self.set_possible()
                self.print_board()
                for y in range(self.y):
                    for x in range(self.x):
                        if self.board[y][x].isdigit():
                            return True
                break
            except:
                print('Invalid move!', end ='')
                return False

        for y in range(self.y):
            for x in range(self.x):
                if self.board[y][x] == '_':
                    print('No more possible moves!')
                    print(f'Your knight visited {self.num_move} squares!')
                    return False
        print('What a great tour! Congratulations!')
        return False

    def check_solution(self, board, knight, num):
        for step in self.steps:
            new_x = knight[0] + step[0]
            new_y = knight[1] + step[1]
            if 0 <= new_x < self.x and 0 <= new_y < self.y and board[new_y][new_x] == '_':
                new_board = copy.deepcopy(board)
                new_board[new_y][new_x] = str(num)
                fl_full = True
                for y in range(self.y):
                    for x in range(self.x):
                        if new_board[y][x] == '_':
                            fl_full = False
                if fl_full:
                    if self.puzzle == False:
                        self.board = new_board
                    return True
                res = self.check_solution(new_board, [new_x, new_y], num + 1)
                if res:
                    return True
        return False

    def start(self):
        self.num_move = 0
        self.get_board()
        self.get_knight()
        if self.puzzle:
            if self.check_solution(copy.deepcopy(self.board), copy.deepcopy(self.knight),1):
                self.set_possible()
                print('Here\'s the solution!')
                self.print_board()
                while self.do_move():
                    pass
            else:
                print('No solution exists!')
        else:
            self.board[self.knight[1]][self.knight[0]] = '1'
            if self.check_solution(copy.deepcopy(self.board), copy.deepcopy(self.knight),2):
                print('Here\'s the solution!')
                self.print_board()
            else:
                print('No solution exists!')


if __name__ ==  '__main__':
    game = Game()
    game.start()
