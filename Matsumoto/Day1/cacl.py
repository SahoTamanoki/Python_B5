import sys

args = sys.argv
sum = 0
for arg in args[1:]:
    sum += int(arg)

print(sum, end="")
