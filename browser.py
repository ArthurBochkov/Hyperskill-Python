import os
import requests
import sys

from colorama import Fore
from bs4 import BeautifulSoup

class Browser:

    def __init__(self):
        self.current_page = None
        self.back_pages = []
        self.dir = None

    def print_page(self, command):
        r = requests.get('http://' + command)
        soup = BeautifulSoup(r.content, 'html.parser')
        text = ''
        for x in soup.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6", "span", "a", "ul", "ol", "li"]):
            if str(x).startswith('<a '):
                text += Fore.BLUE + x.text + '\n'
            else:
                text += x.text + '\n'
        with open(self.dir + '/' + command.replace('.', '_').lower()[:command.index('.')], 'w') as f:
            f.write(text)
        print(text)

    def stage6(self):
        self.dir = sys.argv[1]
        if not os.access(self.dir, os.F_OK):
            os.mkdir(self.dir)
        while True:
            command = input()
            if command == 'exit':
                return
            elif command == 'back':
                if len(self.back_pages) > 0:
                    self.back_pages.pop()
                if len(self.back_pages) > 0:
                    self.print_page(self.back_pages[-1])
            elif '.' not in command:
                print('Invalid URL')
            else:
                self.print_page(command)
                self.back_pages.append(command)

    def go(self):
        self.stage6()


if __name__ == '__main__':
    browser = Browser()
    browser.go()
