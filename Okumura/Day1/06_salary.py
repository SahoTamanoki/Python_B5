# salary.py
import sys
args = sys.argv

salary = int(args[1])

if salary > 1000000:
     tax = round((salary - 1000000) * 0.2) + round(1000000 * 0.1)
     paid = salary - tax
else:
     tax = round(salary * 0.1)
     paid = round(salary - tax)

print('支給額:' + str(paid) + '、' + '税額:' + str(tax),end="")
