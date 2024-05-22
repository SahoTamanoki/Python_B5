#四捨五入モジュールのインポート
from decimal import Decimal, ROUND_HALF_UP

#引数設定
import sys
args = sys.argv
salary = int(args[1])


#税額計算
tax_line = 1000000 ##基準の設定
if salary > tax_line:                                                     
    tax = (salary - tax_line)*0.2 + tax_line*0.1                          ##100万以上の部分は2%
else:                                                                   
    tax = salary*0.1                                                    
tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)   ##小数点以下四捨五入

#支給額算出
supply = salary - tax

#出力
print(f"支給額:{supply}、税額:{tax}",end = "")