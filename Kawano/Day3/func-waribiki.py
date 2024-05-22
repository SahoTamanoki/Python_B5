def calcValue(who, hour, count, value):
    info = "割引なし"
    if (hour == 14) and (count >= 3):
        value *= 0.9
        info = "1割引き"
    elif (hour == 15) and (count >= 3):
        value *= 0.8
        info = "2割引"

    value = int(value)
    print(f"{who}さんは{info}で{value}円")

calcValue("A", 15, 3, 1200)
calcValue("B", 14, 5, 2000)