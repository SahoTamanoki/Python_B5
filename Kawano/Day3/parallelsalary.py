#引数の設定
import sys
args = sys.argv
#給与計算のモジュール使用
from func_salary import calcsalary

for salary in args[1:]:
    tax,supply= calcsalary(int(salary))
    # supply = calcsalary(salary)[1]
    print(f"税額は{tax}、支給額は{supply}です。")