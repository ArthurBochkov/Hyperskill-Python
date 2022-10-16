print('How many pencils would you like to use:')
while True:
    try:
        pencils = int(input())
        if pencils < 0:
            print('The number of pencils should be numeric')
            continue
        elif pencils == 0:
            print('The number of pencils should be positive')
            continue
        break
    except:
        print('The number of pencils should be numeric')

print('Who will be the first (John, Jack):')
while True:
    first = input()
    if first not in ['John', 'Jack']:
        print("Choose between 'John' and 'Jack'")
        continue
    break

while pencils > 0:
    print('|' * pencils)

    while True:
        if first == 'John':
            num =  input((f'{first}\'s turn:'))
            if num not in ['1', '2', '3']:
                print("Possible values: '1', '2' or '3'")
                continue
            num = int(num)
        else:
            print(f'{first}\' turn:')
            num = (pencils - 1) % 4
            if num == 0:
                num = 1
            print(num)

        if num > pencils:
            print('Too many pencils were taken')
            continue
        break

    pencils -= num
    first = 'Jack' if first == 'John' else 'John'

    if pencils <= 0:
        print(f'{first} won!')
        break

