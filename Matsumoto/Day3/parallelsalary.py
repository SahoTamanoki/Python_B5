import sys
import func_salary

MILLION = 1000000

args = sys.argv

for salary in args[1:]:
    allowance, tax = func_salary.calcsalary(salary)
    print(f"給与:{salary}、支給額:{allowance}、税額:{tax}")
