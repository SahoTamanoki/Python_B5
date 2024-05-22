import sys
args = sys.argv
i = int(args[1])
animal = args[2]

animal_names = ["giraffe","tiger","zebra","elephant","lion"]
animal_names.insert(i, animal)

animal_names.pop()
animal_names.sort()
print(animal_names, end="")