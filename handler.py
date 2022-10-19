import hashlib
import os
import sys

class FileHandler:

    def __init__(self, dir):
        self.dir = dir
        self.format = None
        self.sorting = None
        self.f_sorted = None
        self.dubl = None

    def read_format(self):
        self.format = input('Enter file format:')

    def read_sorting(self):
        print('Size sorting options:')
        print('1. Descending')
        print('2. Ascending')
        while True:
            self.sorting = input('Enter a sorting option:')
            if self.sorting not in ['1', '2']:
                print('Wrong option')
            else:
                break
            print('Wrong option')

    def read_del(self):
        while True:
            answer = input('Delete files?')
            if answer in ['yes', 'no']:
                return answer == 'yes'

    def del_dubl_num(self):
        while True:
            answer = input('Enter file numbers to delete:')
            if answer == '':
                print('Wrong format')
                continue
            ret = False
            for x in answer.split():
                if not x.isdigit() or self.dubl.get(int(x), None) == None:
                    print('Wrong format')
                    ret = True
                    break
            if ret:
                for x in self.dubl.items():
                    print(x)
                continue

            space = 0
            for x in answer.split():
                space += self.dubl[int(x)][1]
                os.remove(self.dubl[int(x)][0])
            print(f'Total freed up space: {space} bytes')
            break

    def read_dubl(self):
        while True:
            answer = input('Check for duplicates?')
            if answer in ['yes', 'no']:
                return answer == 'yes'

    def do(self):
        self.read_format()
        self.read_sorting()
        f = {}
        for root, _, files in os.walk(self.dir):
            for name in files:
                if self.format != '':
                    if not name.endswith('.' + self.format):
                        continue
                file_name = os.path.join(root, name)
                file_size = os.path.getsize(file_name)
                if f.get(file_size) == None:
                    f[file_size] = [file_name]
                else:
                    f[file_size].append(file_name)
        self.f_sorted = sorted(f.items())
        if self.sorting == '1':
            self.f_sorted.reverse()
        for x in self.f_sorted:
            print(x[0], 'bytes')
            for y in x[1]:
                print(y)

    def do_dubl(self):
        i = 0
        self.dubl = {}
        for x in self.f_sorted:
            print()
            print(x[0], 'bytes')
            hash_lib = {}
            for y in x[1]:
                with open(y, 'rb') as f:
                    hash = hashlib.md5(f.read()).hexdigest()
                    if hash_lib.get(hash) == None:
                        hash_lib[hash] = [y]
                    else:
                        hash_lib[hash].append(y)
            for h in hash_lib.items():
                if len(h[1]) > 1:
                    print('Hash:', h[0])
                    for f in h[1]:
                        i += 1
                        self.dubl[i] = (f, x[0])
                        print(f'{i}. {f}')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Directory is not specified')
    else:
        handler = FileHandler(sys.argv[1])
        handler.do()
        if handler.read_dubl():
            handler.do_dubl()
            if handler.read_del():
                handler.del_dubl_num()

