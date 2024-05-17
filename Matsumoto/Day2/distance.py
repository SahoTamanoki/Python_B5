from decimal import Decimal
import sys

FROM_STATION_TO_DISTANCE = {
    "東京": 0.00, "品川": 6.78, "新横浜": 25.54,
    "名古屋": 342.02, "京都": 476.31, "新大阪": 515.35
}

station_from = sys.argv[1]
station_to = sys.argv[2]
distance = abs(FROM_STATION_TO_DISTANCE[station_from] -
               FROM_STATION_TO_DISTANCE[station_to])

distance = Decimal(str(distance)).quantize(Decimal("0.00"))
print(distance, end="")
