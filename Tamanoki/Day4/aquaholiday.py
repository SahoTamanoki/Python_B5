import sys
args = sys.argv

date = args[1]
adult_num  = int(args[2])
child_num  = int(args[3])

year = int(date[ :4])
month = int(date[4:6]) 
day = int(date[6:8])  
weekday = calendar.weekday(year,month,day)


if day <=4 and :
    fee = adult_num * 2000 + child_num * 1200
    print(fee)

elif day > 4 or "祝日":
    fee = adult_num * 2400 + child_num * 1500
    print(fee)


