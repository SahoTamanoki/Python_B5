import sys

sentence = sys.argv[1]
idx = int(sys.argv[2])
splitted = sentence.split()
print(splitted[idx-1], end="")
