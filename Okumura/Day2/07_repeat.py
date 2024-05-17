total = 0
a = int(input())

while total < 100:
     total += a
     print(total)
else:
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