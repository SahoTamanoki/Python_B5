import sys
args = sys.argv

date = args[1]
adult_num  = int(args[2])
children_num  = int(args[3])

year = int(date[ :4])
month = int(date[4:6]) 
day = int(date[6:8])
weekday = calendar.weekday(year,month,day)


if day <=4:
    fee = adult_num * 2000 + children_num * 1200
    print(fee)

else:
    fee = adult_num * 2400 + children_num * 1500
    print(fee)


