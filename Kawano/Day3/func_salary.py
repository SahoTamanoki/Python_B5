from decimal import Decimal, ROUND_HALF_UP
#給与計算のモジュール作成
def calcsalary(salary):
    million = 1000000
    if salary > million:
        tax = (salary-million)*0.2 + million * 0.1
    else: 
        tax = salary * 0.1
    tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
    supply = salary - tax
    return (tax, supply)
    