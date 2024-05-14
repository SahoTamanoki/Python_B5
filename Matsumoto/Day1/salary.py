from decimal import Decimal, ROUND_HALF_UP
import sys

MILLION = 1000000

salary = int(sys.argv[1])
if salary > MILLION:
    tax = (salary - MILLION)*0.2 + MILLION*0.1
else:
    tax = salary * 0.1

tax = Decimal(tax).quantize(Decimal(0), rounding=ROUND_HALF_UP)
print(f"支給額:{salary - tax}、税額:{tax}", end="")
