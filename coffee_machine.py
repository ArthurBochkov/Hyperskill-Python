class CoffeeMachine:

    ingradients = {'water':'ml', 'milk':'ml', 'coffee beans':'grams', 'money':'$', 'disposable cups':''}

    ingredient_espresso = {'water':250, 'coffee beans':16, 'money':4, 'disposable cups':1}
    ingredient_latte = {'water':350, 'milk':75, 'coffee beans':20, 'money': 7, 'disposable cups':1}
    ingredient_cappuccino = {'water':200, 'milk':100, 'coffee beans':12, 'money': 6, 'disposable cups':1}

    coffee = {'1':ingredient_espresso, '2':ingredient_latte, '3':ingredient_cappuccino}

    def __init__(self):
        self.my_ingredients = {'water': 400, 'milk':540, 'coffee beans':120,
                       'disposable cups':9, 'money':550}

    def welcome(self):
        print('The coffee machine has:')
        for x,y in self.my_ingredients.items():
            if x == 'money':
                print(f'{CoffeeMachine.ingradients[x]}{y} of {x}')
            else:
                if CoffeeMachine.ingradients[x] == '':
                    print(f'{y} of {x}')
                else:
                    print(f'{y} {CoffeeMachine.ingradients[x]} of {x}')

    def check_coffee(self, coffee):
        for x,y in coffee.items():
            if x != 'money':
                if y > self.my_ingredients[x]:
                    print(f'Sorry, not enough {x}!')
                    return False
        print('I have enough resources, making you a coffee!')
        return True

    def make_coffee(self, coffee):
        for x,y in coffee.items():
            if x == 'money':
                self.my_ingredients[x] += y
            else:
                self.my_ingredients[x] -= y

    def do_buy(self):
        answer = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        if answer == 'back':
            return
        if self.check_coffee(CoffeeMachine.coffee[answer]):
            self.make_coffee(CoffeeMachine.coffee[answer])

    def do_fill(self):
        for x,y in CoffeeMachine.ingradients.items():
            if x != 'money':
                answer = input(f'Write how many {y} of {x} you want to add: ')
                self.my_ingredients[x] += int(answer)

    def do_take(self):
        print(f'I gave you ${self.my_ingredients["money"]}')
        self.my_ingredients['money'] = 0

    def command(self):
        answer = input('Write action (buy, fill, take, remaining, exit): ')
        if answer == 'buy':
            self.do_buy()
        elif answer == 'fill':
            self.do_fill()
        elif answer == 'take':
            self.do_take()
        elif answer == 'remaining':
            self.welcome()
        elif answer == 'exit':
            return False

    def start(self):
        while self.command() != False:
            pass


if __name__ == '__main__':
    cm = CoffeeMachine()
    cm.start()

