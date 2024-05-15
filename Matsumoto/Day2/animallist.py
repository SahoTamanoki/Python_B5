import sys

idx = int(sys.argv[1])
animal = sys.argv[2]

animals = ["giraffe", "tiger", "zebra", "elephant", "lion"]
animals.insert(idx, animal)
animals.pop(-1)
animals.sort()

print(animals, end="")
