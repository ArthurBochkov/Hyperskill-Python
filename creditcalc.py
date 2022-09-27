import argparse
import math

class CreditCalc:

    def __init__(self, type, payment, principal, periods, interest):

        if payment != None:
            payment = int(payment)
        if principal != None:
            principal = int(principal)
        if periods != None:
            periods = int(periods)
        if interest != None:
            interest = float(interest) / 12 / 100

        if principal == None:
            if type == 'annuity':
                principal = math.ceil(payment * (pow(1 + interest, periods) - 1) / interest / pow(1 + interest, periods))
            print(f'Your loan principal = {principal}!')

        elif payment == None:
            if type == 'annuity':
                payment = math.ceil(principal * interest * pow(1 + interest, periods) / (pow(1 + interest, periods) - 1))
                print(f'Your annuity payment = {payment}!')
            elif type == 'diff':
                m = 1
                all_d = 0
                while m <= periods:
                    d = math.ceil(principal / periods + interest * (principal - principal * (m - 1) / periods))
                    print(f'Month 1: payment is {d}')
                    all_d += d
                    m += 1
                print()
                print(f'Overpayment = {all_d - principal}')

        elif periods == None:
            if self.check(principal, payment, interest):
                pass
            elif type == 'annuity':
                periods = math.ceil(math.log(payment / (payment - interest * principal), 1 + interest))
                year = math.floor(periods / 12)
                month = periods % 12
                print('It will take', end='')
                if year > 0:
                    print(f' {year} year{"s" if year > 1 else ""}', end='')
                    if month > 0:
                        print(' and', end='')
                if month > 0:
                    print(f' {month} month{"s" if month > 1 else ""}', end='')
                print(' to repay this loan!')
                print(f'Overpayment = {payment * periods - principal}')

        elif interest == None:
            print('Incorrect parameters')

    def check(self, *params):
        for x in params:
            if x == None:
                print('Incorrect parameters')
                return True
        return False

parser = argparse.ArgumentParser()
parser.add_argument('-type', '--type', choices=['annuity', 'diff'], help='Incorrect parameters')
parser.add_argument('-payment', '--payment', default=None)
parser.add_argument('-principal', '--principal', default=None)
parser.add_argument('-periods', '--periods', default=None)
parser.add_argument('-interest', '--interest', default=None)
args = parser.parse_args()

calc = CreditCalc(args.type, args.payment, args.principal, args.periods, args.interest)


