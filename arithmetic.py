import random

class Calc:

    operation = {
        "+": (lambda x, y: x + y),
        "-": (lambda x, y: x - y),
        "*": (lambda x, y: x * y)
    }

    level = {1:'simple operations with numbers 2-9',
             2:'integral squares 11-29'}

    def __init__(self):
        self.right = 0
        self.wrong = 0
        self.level = None
        self.name = None

    def check(self):
        if self.level == 1:
            x = random.randrange(2, 10)
            y = random.randrange(2, 10)
            oper = random.choice(list(Calc.operation))
            print(f'{x} {oper} {y}')
            res = Calc.operation[oper](int(x), int(y))
        else:
            x = random.randrange(11, 30)
            print(x)
            res = pow(x, 2)

        while True:
            answer = input()
            if not answer.lstrip('-').isdigit():
                print('Incorrect format.')
                continue
            break

        if str(res) == answer:
            self.right += 1
            print('Right!')
        else:
            self.wrong += 1
            print('Wrong!')

    def check_all(self):
        for _ in range(5):
            self.check()
        print(f'Your mark is {self.right}/{self.right + self.wrong}.')

    def get_level(self):
        while True:
            answer = input('Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9\n2 - integral squares of 11-29')
            if answer in ['1', '2']:
                self.level = int(answer)
                break
            print('Incorrect format.')

    def save_result(self):
        answer = input(f'Your mark is {self.right}/{self.right + self.wrong}. Would you like to save the result? Enter yes or no.')
        if answer in ('yes', 'YES', 'y', 'Yes'):
            name = input('What is your name?')
            with open('results.txt', 'a') as f:
                f.write(f'{name}: {self.right}/{self.right + self.wrong} in level {self.level} ({Calc.level[self.level]})')
            print('The results are saved in "results.txt".')



if __name__ == '__main__':
    calc = Calc()
    calc.get_level()
    calc.check_all()
    calc.save_result()