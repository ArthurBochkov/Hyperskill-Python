import random

class RockScissorsPaper:

    items = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.computer_word = None
        self.my_word = None
        self.my_name = None
        self.my_score = 0
        self.variants = None

    def get_name(self):
        self.my_name = input('Enter your name:')
        self.get_rating()
        print(f'Hello, {self.my_name}')

    def get_rating(self):
        with open('rating.txt', 'r') as f:
            lines = f.readlines()
        for line in lines:
            if line.startswith(self.my_name):
                self.my_score = int(line.split()[1])

    def get_variants(self):
        answer = input()
        self.variants = RockScissorsPaper.items if answer == '' else answer.split(',')

    def computer_move(self):
        self.computer_word = random.choice(RockScissorsPaper.items)
        print('Okay, let\'s start')

    def my_move(self):
        while True:
            self.my_word = input()
            if self.my_word == '!exit':
                return False
            elif self.my_word == '!rating':
                print(f'Your rating: {self.my_score}')
                continue
            else:
                if self.my_word in self.variants:
                    return True
                else:
                    print('Invalid input')

    def print_result(self):
        if self.my_word == self.computer_word:
            print(f'There is a draw ({self.computer_word})')
            self.my_score += 50
            return
        for i in range((len(self.variants) - 1) // 2):
            num = self.variants.index(self.my_word)
            if self.variants[(num + i + 1) % len(self.variants)] == self.computer_word:
                print(f'Sorry, but the computer chose {self.computer_word}')
                return
        else:
            print(f'Well done. The computer chose {self.computer_word} and failed')
            self.my_score += 100

    def start(self):
        self.get_name()
        self.get_variants()
        while True:
            self.computer_move()
            if self.my_move():
                self.print_result()
            else:
                print('Bye!')
                return


if __name__ == '__main__':
    rsp = RockScissorsPaper()
    rsp.start()
