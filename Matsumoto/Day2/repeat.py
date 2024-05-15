import sys

num = int(sys.argv[1])
current = 0
while current < 100:
    current += num
    if current == 100:
        print("Just 100!", end="")
        exit(0)
        
print("Over!", end="")
