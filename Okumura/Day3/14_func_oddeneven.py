

def judgeOddeneven(a,b,c):
    numbers = [a,b,c]
    for num in numbers:
        if int(num) % 2 == 0:
            print(str(num) + 'は偶数')
        else:
            print(str(num) + 'は奇数')

args = ["func_oddeneven.py",2,3,4]
judgeOddeneven(int(args[1]),int(args[2]),int(args[3]))



# import sys
# args = sys.argv

# #関数を定義
# def calcvalue(num):
#     #あまりを算出
#     mod = num % 2

#     #あまりの値から奇数偶数判定
#     if mod != 0:
#         print(str(num) + "は奇数")
#     else:
#         print(str(num) + "は偶数")

# calcvalue(int(args[1]))
# calcvalue(int(args[2]))
# calcvalue(int(args[3]))