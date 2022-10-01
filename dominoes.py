import random

class Domino:

    def __init__(self):
        self.stock_pieces = []
        self.computer_pieces = []
        self.player_pieces = []
        self.status = ''
        self.max_piece = []
        self.snake = []
        self.snake_begin = None
        self.snake_end = None

    def go(self):
        self.stock_pieces = [[x, y] for x in range(7) for y in range(x + 1)]
        for _ in range(7):
            piece = random.choice(self.stock_pieces)
            self.computer_pieces.append(piece)
            self.stock_pieces.remove(piece)
            piece = random.choice(self.stock_pieces)
            self.player_pieces.append(piece)
            self.stock_pieces.remove(piece)

        for x in range(7):
            self.max_piece = [6 - x, 6 - x]
            if self.max_piece in self.computer_pieces:
                self.computer_pieces.remove(self.max_piece)
                self.status = 'player'
                break
            if self.max_piece in self.player_pieces:
                self.player_pieces.remove(self.max_piece)
                self.status = 'computer'
                break
        self.snake = [self.max_piece]
        self.snake_begin = self.max_piece[0]
        self.snake_end = self.max_piece[1]


    def try_move(self, who, piece, end):
        if end:
            if piece[0] == self.snake_end:
                self.snake.append(piece)
                self.snake_end = piece[1]
                who.remove(piece)
                return True
            elif piece[1] == self.snake_end:
                piece.reverse()
                self.snake.append(piece)
                self.snake_end = piece[1]
                who.remove(piece)
                return True
        else:
            if piece[1] == self.snake_begin:
                self.snake.insert(0, piece)
                self.snake_begin = piece[0]
                who.remove(piece)
                return True
            elif piece[0] == self.snake_begin:
                piece.reverse()
                self.snake.insert(0, piece)
                self.snake_begin = piece[0]
                who.remove(piece)
                return True
        return False


    def move_player(self, piece_num):
        piece = self.player_pieces[abs(piece_num) - 1]
        return self.try_move(self.player_pieces, piece, piece_num > 0)

    def move_computer(self):
        for x in self.computer_pieces:
            if self.try_move(self.computer_pieces, x , True):
                return True
            if self.try_move(self.computer_pieces, x , False):
                return True
        else:
            piece = self.get_stock_piece()


    def get_stock_piece(self):
        if self.stock_pieces:
            piece = random.choice(self.stock_pieces)
            if self.status == 'computer':
                self.computer_pieces.append(piece)
            else:
                self.player_pieces.append(piece)
            self.stock_pieces.remove(piece)
            return piece

    def move(self):
        if self.status == 'player':
            while True:
                piece_num = input()
                if not piece_num.lstrip('-').isdigit():
                    print('Invalid input. Please try again.')
                    continue
                piece_num = int(piece_num)
                if 0 < abs(piece_num) <= len(self.player_pieces):
                    if self.move_player(piece_num):
                        break
                    else:
                        print('Illegal move. Please try again.')
                elif piece_num == 0:
                    self.get_stock_piece()
                    break
                else:
                    print('Invalid input. Please try again.')
            self.status = 'computer'
        else:
            self.move_computer()
            self.status = 'player'

    def check_end(self):
        if len(self.player_pieces) == 0:
            self.print()
            print('Status: The game is over. You won!')
            return True
        if len(self.computer_pieces) == 0:
            self.print()
            print('Status: The game is over. The computer won!')
            return True
        for x in range(7):
            if [s[0] for s in self.snake].count(x) + [s[1] for s in self.snake].count(x) == 8:
                print('Status: The game is over. It\'s a draw!')
                return True
        return False

    def print(self):
        print('=' * 70)
        print(f'Stock size: {len(self.stock_pieces)}')
        print(f'Computer pieces: {len(self.computer_pieces)}')
        print()
        if len(self.snake) > 6:
            for i in range(3):
                print(self.snake[i], end='')
            print('...', end='')
            for i in range(3):
                print(self.snake[-3 + i], end='')
        else:
            for x in self.snake:
                print(x, end='')
        print()
        print()
        print('Your pieces:')
        for i,x in enumerate(self.player_pieces):
            print(f'{i+1}:{x}')
        print()
        if self.status == 'player':
            print('Status: It\'s your turn to make a move. Enter your command.')
        else:
            print('Status: Computer is about to make a move. Press Enter to continue...')
            input()

    def start(self):
        self.go()
        while True:
            self.print()
            self.move()
            if self.check_end():
                break

domino = Domino()
domino.start()

