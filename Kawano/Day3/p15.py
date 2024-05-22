import sys
args = sys.argv

try:
    distanceFromTokyo = {"東京":0.00, "品川":6.78, "新横浜":25.54, "名古屋":342.02, "京都":476.31,"新大阪":515.35}
    distance = distanceFromTokyo[args[2]] - distanceFromTokyo[args[1]]
    distance = round(distance, 2)
    distance = abs(distance)
    print(distance, end="")
except:
    print("のぞみの停車駅を引数に設定してください",end="")


# # kyoris = {"東京":0.00,"品川":6.78,"新横浜":25.54,"名古屋":342.02,"京都":476.31,"新大阪":515.35}
# kyori = kyoris[args[2]] - kyoris[args[1]]
# kyori_floated = round(kyori,2)
# kyori_last = abs(kyori_floated)
# print(kyori_last,end="")