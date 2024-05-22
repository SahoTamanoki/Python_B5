import sys
args = sys.argv

text = args[1]
num = int(args[2])

text = args[1]
sentence = text.split()
print(sentence[num-1], end = "") 