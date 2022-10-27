import random

class BillSplitter:

    def __init__(self):
        self.num_members = None
        self.members = {}
        self.bill = None

    def start(self):
        while True:
            answer = input('Enter the number of friends joining (including you):')
            if not answer.isdigit() or int(answer) <= 0:
                print('\nNo one is joining for the party')
                return
            self.num_members = int(answer)
            break

        print('\nEnter the name of every friend (including you), each on a new line:')
        for _ in range(self.num_members):
            self.members[input()] = 0

        self.bill = int(input('\nEnter the total bill value:'))

        answer = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:')
        if answer == 'Yes':
            lucky = random.choice(list(self.members.keys()))
            print(f'\n{lucky} is the lucky one!')
            for x in self.members.keys():
                if x != lucky:
                    self.members[x] = round(self.bill / (self.num_members - 1), 2)
        else:
            print('\nNo one is going to be lucky')
            for x in self.members.keys():
                self.members[x] = round(self.bill / self.num_members, 2)

        print(f'\n{self.members}')


if __name__ == '__main__':
    bs = BillSplitter()
    bs.start()
