import sys

num = int(sys.argv[1])
if num%2 == 0:
    print("偶数", end="")
else:
    print("奇数", end="")
