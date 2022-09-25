import random

class Hangman:

    def __init__(self, words, attempts):
        self.words = words
        self.attempts =attempts
        self. won = 0
        self.lost = 0

    def start(self):
        key_word = random.choice(self.words)

        cur_attempts = self.attempts
        disp_word = len(key_word) * '-'
        letters = set()
        find = False

        while True:

            if cur_attempts == 0:
                print('You lost!')
                self.lost +=1
                break

            print(disp_word)
            char = input('Input a letter:')

            if len(char) != 1:
                print('Please, input a single letter.')
                continue

            if not char.isalpha() or char != char.lower():
                print('Please, enter a lowercase letter from the English alphabet.')
                continue

            if char in letters:
                print('You\'ve already guessed this letter')
                continue

            letters.add(char)

            find = False
            for i, x in enumerate(key_word):
                if char == x and disp_word[i] == '-':
                    disp_word = disp_word[:i] + char + disp_word[i + 1:]
                    find = True

            if not find:
                cur_attempts -= 1
                print(f'That letter doesn\'t appear in the word.  # {cur_attempts} attempts')

            if '-' not in disp_word:
                print(f'You guessed the word {disp_word}!')
                print('You survived!')
                self.won +=1
                break

config = {
    'words': ['python', 'java', 'swift', 'javascript'],
    'attempts': 8
}
game = Hangman(**config)

while True:
    print('H A N G M A N  # 8 attempts')
    command = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if command == 'play':
        game.start()
    elif command == 'results':
        print(f'You won: {game.won} times.')
        print(f'You lost: {game.lost} times.')
    elif command == 'exit':
        break
