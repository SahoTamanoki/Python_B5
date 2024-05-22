import sys
args = sys.argv

n= int(args[1])

# mode = "w"...上書き保存　mode = "a"...全部消して、最後に追加していく
with open("sheep.txt", mode = "w", encoding="utf-8") as f:
    for i in range(1,n+1):
        i = str(i)
        f.write("ひつじが"+i+"匹\n") #改行は、\n