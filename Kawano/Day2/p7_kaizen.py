#引数・初期設定
import sys
args = sys.argv
repeat = int(args[1])
total = 0

#引数が負の数の場合処理を拒否
if repeat >0:
    ##繰り返し開始
    while total < 100:
        total = total + repeat
        if total == 100:
            print("Just 100!",end="")
        elif total > 100:
            print("Over!",end="")
        else:
            print(total)
else: print("正の整数を入力してください")