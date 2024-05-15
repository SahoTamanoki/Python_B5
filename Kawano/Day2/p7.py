#引数設定
import sys
args = sys.argv
#足し算開始前の前提
repeat = int(args[1])
total = 0
#繰り返し開始
while total < 100:
    total = total + repeat
    if total == 100:
        print("Just 100!",end="")
    elif total > 100:
        print("Over!",end="")
    else:
        print(total)