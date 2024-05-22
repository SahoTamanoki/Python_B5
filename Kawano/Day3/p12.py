import sys
args = sys.argv
text = args[1]
num = int(args[2]) - 1
text = text.split()
print(text[num])