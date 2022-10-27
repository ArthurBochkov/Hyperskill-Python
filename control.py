import gzip
import statistics

class Control:

    def __init__(self):
        self.content = None

    def read(self):
        with gzip.open(input()) as f:
            self.content = f.readlines()[1::4]
        self.content = [x.decode().rstrip('\n') for x in self.content]

    def get_ns(self):
        return len([x for x in self.content if x.count("N") > 0])

    def get_statistics(self):
        print(f'Reads in the file = {len(self.content)}:')
        print(f'Reads sequence average length = {round(sum([len(x) for x in self.content]) / len(self.content))}')

        print(f'Repeats = {len(self.content) - len(set(self.content))}')
        print(f'Reads with Ns = {self.get_ns()}')

        average = round(statistics.mean([(x.count('G') + x.count("C")) * 100 / len(x) for x in self.content]), 2)
        print(f'GC content average = {average}%')
        print(f'Ns per read sequence = {round(statistics.mean([x.count("N") * 100 / len(x) for x in self.content]), 2)}%')


if __name__ == '__main__':
    exp = []

    best_control = 0
    best_ns = None

    for i in range(3):
        exp.append(Control())
        exp[i].read()
        if best_ns == None or exp[i].get_ns() < best_ns:
            best_control = i
            best_ns = exp[i].get_ns()

    exp[best_control].get_statistics()