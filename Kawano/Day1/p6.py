from decimal import Decimal, ROUND_HALF_UP
import sys
args = sys.argv
salary = int(args[1])
if salary >1000000:
    tax = (salary - 1000000)*0.2 + 1000000*0.1
else:
    tax = salary*0.1
tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)

supply = salary - tax
print(f"支給額:{supply}、税額:{tax}",end = "")