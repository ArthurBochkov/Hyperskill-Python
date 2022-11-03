import random

class TextGenerator:
    def __init__(self):
        self.bigram = {}

    def load(self):
        name = input()
        with open(name, "r", encoding="utf-8") as f:
                token = f.read().split()

        for i in range(len(token) - 1):
            self.bigram.setdefault(token[i], {})
            self.bigram[token[i]].setdefault(token[i + 1], 0)
            self.bigram[token[i]][token[i + 1]] += 1

    def chains(self):
        for j in range(10):
            num = 0
            while True:
                if num == 0:
                    while True:
                        word = random.choice(list(self.bigram.keys()))
                        if word[0] == word[0].upper() and word[0].isalpha() and word[-1] not in '.!?':
                            break
                else:
                    word = random.choices(list(self.bigram[word].keys()), tuple(self.bigram[word].values()))[0]
                print(f'{word} ', end='')
                num += 1
                if num >= 5 and word[-1] in '.!?':
                    print()
                    break


if __name__ == '__main__':
    tg = TextGenerator()
    tg.load()
    tg.chains()
