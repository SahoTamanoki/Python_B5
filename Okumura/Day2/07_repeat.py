total = 0
a = int(input())

# Problem: 1未満の整数だと、無限ループになる
while total < 100:
     total += a
     print(total)
# 出力する
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