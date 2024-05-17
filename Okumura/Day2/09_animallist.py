animals = ["giraffe", "tiger", "zebra", "elephant", "lion"]

animals.insert(1,'buffalo')
animals.pop()
# del animals[len(animals) - 1]
animals.sort()

print(animals)

#-------------------
#import sys
#args = sys.argv
#
#animals = ["giraffe", "tiger", "zebra", "elephant", "lion"]
#
#animals.insert(int(args[1]),str(args[2]))
#del animals[len(animals) - 1]
#animals.sort()
#
#print(animals, end="")