import sys

args = sys.argv
# n = args[1]
n = int(input())

with open('./Okumura/Day5/files/sheep.txt','w') as f:
    for i in range(1,n + 1):
        i = str(i)
        f.write("ひつじが" + str(i) + "匹\n")