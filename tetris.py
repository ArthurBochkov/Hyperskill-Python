import numpy as np


class Tetris:
    shapes = {
        'O': [[4, 14, 15, 5]],
        'I': [[4, 14, 24, 34], [3, 4, 5, 6]],
        'S': [[5, 4, 14, 13], [4, 14, 15, 25]],
        'Z': [[4, 5, 15, 16], [5, 15, 14, 24]],
        'L': [[4, 14, 24, 25], [5, 15, 14, 13], [4, 5, 15, 25], [6, 5, 4, 14]],
        'J': [[5, 15, 25, 24], [15, 5, 4, 3], [5, 4, 14, 24], [4, 14, 15, 16]],
        'T': [[4, 14, 24, 15], [4, 13, 14, 15], [5, 15, 25, 14], [4, 5, 6, 15]]
    }

    def __init__(self):
        self.field = None
        self.size_x = self.size_y = None
        self.figure = None
        self.mov_x = self.mov_y = None
        self.mov_pos = None
        self.pos_left = self.pos_right = self.pos_bottom = None

    def set_field(self):
        return np.full((self.size_y, self.size_x), '-')

    def print_field(self):
        for i in range(self.field.shape[0]):
            line = []
            for x in self.field[i]:
                line.append(x)
            for j in range(self.field.shape[1]):
                if self.check_shape_x_y(j, i):
                    line[j] = '0'
            print(' '.join(line))
        print()

    def add_shape(self):
        if self.figure:
            for x in Tetris.shapes[self.figure][self.mov_pos]:
                self.field[x // self.size_x + self.mov_y][(x + self.mov_x) % self.size_x] = '0'

    def check_shape(self, div_x, div_y, div_pos):
        for x in Tetris.shapes[self.figure][(self.mov_pos + div_pos) % len(Tetris.shapes[self.figure])]:
            if x // self.size_x + self.mov_y + div_y >= self.size_y or \
                x + self.mov_x + div_x < 0 or \
                    (x + self.mov_x) % self.size_x + div_x >= self.size_x:
                return False
            if self.field[x // self.size_x + self.mov_y + div_y][(x + self.mov_x) % self.size_x + div_x] == '0':
                return False
        return True

    def check_shape_x_y(self, x, y):
        if self.figure != None:
            for n in Tetris.shapes[self.figure][self.mov_pos]:
                if n // self.size_x + self.mov_y == y and (n + self.mov_x) % self.size_x == x:
                    return True
        return False

    def check_end(self):
        for x in range(self.field.shape[1]):
            for y in range(self.field.shape[0]):
                if self.field[y][x] == '-' and not self.check_shape_x_y(x, y):
                    break
            else:
                return True
        return False

    def delete_row(self, del_y):
        y = del_y
        while y > 0:
            for x in range(self.field.shape[1]):
                self.field[y][x] = self.field[y - 1][x]
            y -= 1
        for x in range(self.field.shape[1]):
            self.field[0][x] = '-'

    def do_break(self):
        self.add_shape()
        for y in range(self.field.shape[0]):
            for x in range(self.field.shape[1]):
                if self.field[y][x] == '-':
                    break
            else:
                self.delete_row(y)
        self.figure = None

    def start(self):
        self.size_x, self.size_y = map(int, input().split())
        self.field = self.set_field()
        command = ''

        while True:
            self.print_field()
            if command == 'down' and self.check_end():
                print('Game Over!')
                return

            command = input()
            if command == 'exit':
                return
            if command == 'piece':
                self.add_shape()
                self.figure = input()
                self.mov_x = self.mov_y = self.mov_pos = 0
                continue

            #self.get_position()
            if command == 'down':
                if self.check_shape(0, 1, 0):
                    self.mov_y += 1
            elif command == 'left':
                 if self.check_shape(-1, 1,0):
                    self.mov_x -= 1
                    self.mov_y += 1
            elif command == 'right':
                if self.check_shape(1, 1, 0):
                    self.mov_x += 1
                    self.mov_y += 1
            elif command == 'rotate':
                if self.check_shape(0, 1, 1):
                    self.mov_pos = (self.mov_pos + 1) % len(Tetris.shapes[self.figure])
                    self.mov_y += 1
            elif command == 'break':
                self.do_break()


if __name__ == '__main__':
    t = Tetris()
    t.start()