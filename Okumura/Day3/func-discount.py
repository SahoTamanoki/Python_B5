def calcValue(who, hour, count, value):
    info = "割引なし"
    if (hour == 14) and (count >= 3):
        value *= 0.9
        info = "1割引"
    elif (hour == 15) and (count >= 3):
        value *= 0.8
        info = "2割引"
    
    value = int(value)
    print ("{0}さんは{1}={2}円".format(who,info,value))