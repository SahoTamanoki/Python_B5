
# 例外処理の生成(nが1未満だとエラーとする)
def _validate_int(n):
    if n < 1:
        raise "Error: 1以上の整数を指定してください"
    return n

# totalは入力値を加算していく変数(初期値:0)
total = 0
n = int(input())
# 例外処理の実行
_validate_int(n)

# 100
while total < 100:
     total += n
     print(total)
if total == 100:
    print("Just 100!", end="")
else:
    print("Over!", end="")


#-------------------------------------------
#import sys
#args = sys.argv
#
#total = 0
#a = int(args[1])
#
#while total < 100:
#     total += a
#else:
#    if total == 100:
#        print("Just 100!", end="")
#    else:
#        print("Over!", end="")