import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--payment', type=int)
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
args = parser.parse_args()

if args.interest is not None:
    nominal = args.interest / (12 * 100)


def error_msg():
    print('Incorrect parameters')
    

def diff_payment(principal, periods):
    payments_sum = 0
    for i_ in range(periods):
        print('Month {}: paid out {}'
              .format(i_ + 1, math.ceil(principal / periods + nominal * (principal - principal * i_ / periods))))
        payments_sum += math.ceil(principal / periods + nominal * (principal - principal * i_ / periods))
    print('')
    print('Overpayment: {}'.format(payments_sum - principal))


def convert_months(months_amount):
    payment_years = math.ceil(months_amount) // 12
    payment_months = math.ceil(months_amount) % 12

    if payment_years > 1:
        years_string = 'years'
    else:
        years_string = 'year'

    if payment_months > 1:
        months_string = 'months'
    else:
        months_string = 'month'

    if payment_years == 0:
        return 'You need {} {} to repay this credit!'.format(payment_months, months_string)
    elif payment_months == 0:
        return 'You need {} {} to repay this credit!'.format(payment_years, years_string)
    else:
        return 'You need {} {} and {} {} to repay this credit!'\
            .format(payment_years, years_string, payment_months, months_string)


def annuity_time(payment, principal):
    months = math.log(payment / (payment - nominal * principal), 1 + nominal)
    print(convert_months(months))
    print('Overpayment: {}'.format(payment * math.ceil(months) - principal))


def annuity_repayment(principal, periods):
    monthly_pay = int(math.ceil(principal * ((nominal * (1 + nominal) ** periods) / ((1 + nominal) ** periods - 1))))
    print('Your annuity payment = {}!'.format(monthly_pay))
    print('Overpayment: {}'.format(monthly_pay * periods - principal))


def annuity_principal(payment, periods):
    credit_principal = payment / ((nominal * (1 + nominal) ** periods) / ((1 + nominal) ** periods - 1))
    print('Your credit principal = {}!'.format(math.floor(credit_principal)))
    print('Overpayment: {}'.format(payment * periods - math.floor(credit_principal)))


if args.type is None:
    error_msg()
elif args.type == 'diff':
    if (args.principal and args.periods and args.interest) is not None \
            and args.principal > 0 and args.periods > 0 and args.interest > 0:
        diff_payment(args.principal, args.periods)
    else:
        error_msg()
elif args.type == 'annuity':
    if (args.principal and args.periods and args.interest) is not None \
            and args.principal > 0 and args.periods > 0 and args.interest > 0:
        annuity_repayment(args.principal, args.periods)
    elif (args.payment and args.principal and args.interest) is not None \
            and args.payment > 0 and args.principal > 0 and args.interest > 0:
        annuity_time(args.payment, args.principal)
    elif (args.payment and args.periods and args.interest) is not None \
            and args.payment > 0 and args.periods > 0 and args.interest > 0:
        annuity_principal(args.payment, args.periods)
    else:
        error_msg()
