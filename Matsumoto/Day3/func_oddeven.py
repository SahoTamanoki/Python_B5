import sys

def calcvalue(num: int) -> None:
    if num%2 == 0:
        print(f"{num}は偶数")
    else:
        print(f"{num}は奇数")

args = sys.argv
for arg in args[1:]:
    calcvalue(int(arg))
