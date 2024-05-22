#チャレンジ問題1
#解法1-超ゴリ押し
import sys
args = sys.argv
num = int(args[1])
i = 2
primary = [0]
while num != 1:
    if num % i == 0:
        while num % i != 0:
            num = num / i
        primary.append(i)
    i += 1
primary.remove(0)
print(primary)
    