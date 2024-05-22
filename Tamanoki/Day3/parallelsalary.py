from decimal import Decimal, ROUND_HALF_UP

# func_salary.pyをインポート？？

import sys
args = sys.argv

salary =int(args[1])

def calcsalary(salary):
    if salary > 1000000:
        tax = (salary - 1000000)*0.2+1000000*0.1
    else:
        tax = salary*0.1

    tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
    allowance = salary - tax
    return allowance,tax

args = sys.argv
# args = ["pararellsasaly.py","10000","100000"]

for salary in args[1:]
    allowance,tax = calcsalary(salary)
    print("支給額:"+str(allowance)+"、税額:"+str(tax), end = "")
