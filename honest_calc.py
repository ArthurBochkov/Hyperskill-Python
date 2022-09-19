msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

def isdigit(s):
    try:
        if s != 'M':
            float(s)
        return True
    except:
        return False

def is_one_digit(x):
    x = float(x)
    return x == round(x) and len(str(int(x))) == 1

def check(v1, v2, v3):
    msg = ''
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (float(v1) == 1.0 or float(v2) == 1.0) and v3 == '*':
        msg += msg_7
    if (float(v1) == 0.0 or float(v2) == 0.0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg += msg_8
    if msg != '':
        msg = msg_9 + msg
    print(msg)


operation = {
    "+": (lambda x, y: x + y),
    "-": (lambda x, y: x - y),
    "*": (lambda x, y: x * y),
    "/": (lambda x, y: x / y),
}

memory = 0

while True:
    x, oper, y = input(msg_0).split()
    if not isdigit(x) or not isdigit(y):
        print(msg_1)
        continue

    if oper not in '+-*/':
        print(msg_2)
        continue

    if x == 'M':
        x = memory
    if y == 'M':
        y = memory

    check(x, y, oper)

    try:
        res = operation[oper](float(x), float(y))
        print(res)
    except ZeroDivisionError:
        print(msg_3)
        continue

    while True:
        answer = input(msg_4)
        if answer == 'y':

            if is_one_digit(res):
                while True:
                    answer = input(msg_10)
                    if answer == 'n' or answer == 'y':
                        break
                if answer == 'n':
                    break

            if is_one_digit(res):
                while True:
                    answer = input(msg_11)
                    if answer == 'n' or answer == 'y':
                        break
                if answer == 'n':
                    break

            if is_one_digit(res):
                while True:
                    answer = input(msg_12)
                    if answer == 'n' or answer == 'y':
                        break
                if answer == 'n':
                    break

            memory = res
            break
        elif answer == 'n':
            break

    while True:
        answer = input(msg_5)
        if answer == 'n' or answer == 'y':
            break
    if answer == 'n':
        break


