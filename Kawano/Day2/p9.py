import sys
args = sys.argv
animals = ["giraffe", "tiger", "zebra", "elephant", "lion"]
animals.insert(int(args[1]),args[2])
animals.pop()
animals.sort()
print(animals,end="")