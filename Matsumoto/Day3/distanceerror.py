import sys

FROM_STATION_TO_DISTANCE = {
    "東京": 0.00, "品川": 6.78, "新横浜": 25.54, "名古屋": 342.02, "京都": 476.31, "新大阪": 515.35
}

args = sys.argv

try:
    distance1 = FROM_STATION_TO_DISTANCE[args[1]]
    distance2 = FROM_STATION_TO_DISTANCE[args[2]]
    distance = abs(round(distance1 - distance2, 2))
    print(distance, end="")
except:
    print("のぞみの停車駅を引数に設定してください", end="")
