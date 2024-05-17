def calcsalary(salary):
    if salary > 1000000:
        tax = round((salary - 1000000) * 0.2) + round(1000000 * 0.1)
        paid = salary - tax
    else:
        tax = round(salary * 0.1)
        paid = round(salary - tax)
    print("給与:", salary, "、支給額:", paid, "、税額:", tax)