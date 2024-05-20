from decimal import Decimal, ROUND_HALF_UP

MILLION = 1000000

def calcsalary(salary):
    if salary > MILLION:
        tax = (salary - MILLION)*0.2 + MILLION*0.1
    else:
        tax = salary * 0.1

    tax = Decimal(str(tax)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
    allowance = salary - tax
    return allowance, tax
