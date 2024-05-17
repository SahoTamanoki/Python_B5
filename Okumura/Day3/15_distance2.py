from decimal import Decimal, ROUND_HALF_UP
import sys

# args = sys.argv
args = ["distanceerror.py","東京","静岡"]

list_station = {"東京":0.00, "品川":6.78, "新横浜":25.54, "名古屋":342.02, "京都":476.31, "新大阪":515.35}

try:
    if list_station[args[2]] > list_station[args[1]]:
        dist_station = list_station[args[2]] - list_station[args[1]]
    else:
        dist_station = list_station[args[1]] - list_station[args[2]]
    dist_station = Decimal(dist_station).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    print(str(dist_station), end="")
except:
    print("のぞみの停車駅を引数に設定してください",end="")
