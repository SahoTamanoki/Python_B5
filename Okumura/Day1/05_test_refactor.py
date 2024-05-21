# test.py
# python "Day2/05_test_refactor.py" 10 40 59
import sys
args = sys.argv

def ExceptionError(args):
    if len(args) > 4:
        raise "Error: 引数を3以下にしてください"
    for n in args:
        if n > 0 and n > 100:
            raise "Error: 点数は0~100点で入力してください"



def ScoreChecker(args):
    for i, n in enumerate(args):
        if args[i + 1] >= 70:
            x += 1
            i += 1
        elif args[i + 1] >= 50:
            y += 1
            i += 1
        else:
            i += 1
    if sum(args) >= 220:
        y += 1
    return x,y

def ResultPrint(x,y):
    if x == 3:
        return "合格"
    elif y == 4:
        return "合格"
    else:
        return "不合格"

x = 0
y = 0

ExceptionError(args)
ScoreChecker(args)
ResultPrint(x,y)



# if args[1] >= 70 and args[2] >= 70 and args[3] >= 70:
#     print('合格', end="")
# elif args[1] >= 50 and args[2] >= 50 and args[3] >= 50:
#     if args[1] + args[2] + args[3] >= 220:
#         print('合格', end="")
#     else:
#         print('不合格', end="")
# else:
#     print('不合格', end="")
