import sys
import func_salary

args = sys.argv
calcsalary = func_salary.calcsalary
salary_list = [int(args[1]),int(args[2]),int(args[3])]

for salary in salary_list:
    calcsalary(salary)
