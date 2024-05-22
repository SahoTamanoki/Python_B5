import sys
args = sys.argv

#関数を定義
def calcvalue(num):
    #あまりを算出
    mod = num % 2

    #あまりの値から奇数偶数判定
    if mod != 0:
        print(str(num) + "は奇数")
    else:
        print(str(num) + "は偶数")

#繰り返し処理
for i in range(1,len(args)):
    num = int(args[i])
    calcvalue(num)

#解法2
import sys
args = sys.argv

def oddeven(i):
    if i >= len(args):
        return 
    if int(args[i]) % 2 == 0:
        print(f"{args[i]}は偶数")
    elif int(args[i]) % 2 == 1:
        print(f"{args[i]}は奇数")
    oddeven(i+1)

oddeven(1)
