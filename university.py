class University:

    rate = {'Biotech':(1,2),
            'Chemistry':(2,),
            'Engineering':(4,3),
            'Mathematics':(3,),
            'Physics':(1,3)}

    def __init__(self):
        self.applicants = None
        self.departments_name = None
        self.departments = {}
        self.max_student = None
        self.line = None

    def find_students(self, dep, num):
            for x in self.applicants:
                if len(self.departments.setdefault(dep, [])) < self.max_student and x[8] == False and x[self.line] == dep:
                    self.departments.setdefault(dep, []).append(  [   max((lambda x:sum(x) / len(x))([x[i] for i in University.rate[dep]]), x[9])     , x[0]])
                    x[8] = True

    def start(self):
        self.max_student = int(input())
        with open('applicants.txt', 'r') as f:
            self.applicants = [[x[0] + ' ' + x[1], float(x[2]), float(x[3]), float(x[4]), float(x[5]), x[7], x[8], x[9], False, float(x[6]) ] for x in [x.rstrip('\n').split() for x in f.readlines()]]

        self.departments_name = set(x[5] for x in self.applicants).union(set(x[6] for x in self.applicants)).union(set(x[7] for x in self.applicants))
        self.departments_name = sorted(list(self.departments_name))

        for dep in self.departments_name:
            self.departments[dep] = []
        print(self.applicants)
        for n in [5, 6, 7]:
            self.line = n
            for dep in self.departments_name:
                if dep == 'Biotech':
                    self.applicants.sort(key=lambda x: (-max((x[2] + x[1])/2,x[9]), x[0]) )
                    self.find_students(dep, 2)
                if dep == 'Chemistry':
                    self.applicants.sort(key=lambda x: (- max(x[2],x[9]), x[0]))
                    self.find_students(dep, 2)
                if dep == 'Physics':
                    self.applicants.sort(key=lambda x: (-max((x[1] + x[3])/2,x[9]), x[0]))
                    self.find_students(dep, 1)
                if dep == 'Mathematics':
                    self.applicants.sort(key=lambda x: (-max(x[3],x[9]), x[0]))
                    self.find_students(dep, 3)
                if dep == 'Engineering':
                    self.applicants.sort(key=lambda x: (-max((x[4] + x[3])/2,x[9]), x[0]))
                    print(self.applicants)
                    self.find_students(dep, 4)

        for x in self.departments_name:
            with open(x + '.txt', 'w') as f:
                self.departments[x].sort(key=lambda x:(-x[0], x[1]))
                for y in self.departments[x]:
                    f.write(f'{y[1]} {y[0]}\n')


if __name__ == '__main__':
    u = University()
    u.start()