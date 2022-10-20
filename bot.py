class Bot:
    def __init__(self, name, birth):
        self.name = name
        self.birth = birth
        self.your_name = None
        self.your_age = None

    def greeting(self):
        print(f'Hello! My name is {self.name}.')
        print(f'I was created in {self.birth}.')
        self.your_name = input('Please, remind me your name.')
        print(f'\nWhat a great name you have, {self.your_name}!')
        print('Let me guess your age.')
        print('Enter remainders of dividing your age by 3, 5 and 7.')
        x = [int(input()) for _ in range(3)]
        self.your_age = (x[0] * 70 + x[1] * 21 + x[2] * 15) % 105
        print(f'Your age is {self.your_age}; that\'s a good time to start programming!')

    def count(self):
        num = int(input('Now I will prove to you that I can count to any number you want.'))
        print()
        for i in range(num + 1):
            print(f'{i} !')

    def test(self):
        print('Let\'s test your programming knowledge.')
        print('Why do we use methods?')
        print('1. To repeat a statement multiple times.')
        print('2. To decompose a program into several small subroutines.')
        print('3. To determine the execution time of a program.')
        print('4. To interrupt the execution of a program.')
        while True:
            if input() == '2':
                break
            print('Please, try again.')

    def goodbye(self):
        print('Congratulations, have a nice day!')


if __name__ == '__main__':
    bot = Bot('Aid', 2020)
    bot.greeting()
    bot.count()
    bot.test()
    bot.goodbye()
