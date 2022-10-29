import requests
import json

class CoinConverter:
    def __init__(self):
        self.currency  = None
        self.change = {}
        self.res = None

    def get_change(self, new_currency):
        if self.res.get(new_currency) == None:
            self.change[new_currency] = 1
        else:
            self.change[new_currency] = self.res[new_currency]['rate']

    def start(self):
        self.currency = input()
        r = requests.get(f'http://www.floatrates.com/daily/{self.currency}.json')
        self.res = json.loads(r.text)
        self.get_change('usd')
        self.get_change('eur')

        while True:
            new_currency = input().lower()
            if new_currency == '':
                return
            amount = int(input())
            print('Checking the cache...')
            course = self.change.get(new_currency)
            if course == None:
                print('Sorry, but it is not in the cache!')
                self.get_change(new_currency)
            else:
                print('Oh! It is in the cache!')
            print(f'You received {round(amount * self.change[new_currency], 2)} {new_currency.upper()}.')


if __name__ == '__main__':
    conv = CoinConverter()
    conv.start()