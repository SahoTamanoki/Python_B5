# test.py
import sys
args = sys.argv

a = int(args[1])
b = int(args[2])
c = int(args[3])

if a >= 70 and b >= 70 and c >= 70:
        print('合格', end="")
elif a + b + c >= 220:
    if a >= 50 and b >= 50 and c >= 50:
        print('合格', end="")
    else:
        print('不合格', end="")
else:
    print('不合格', end="")
