#引数設定
import sys
args = sys.argv
num = int(args[1])

#ファイルを開く
with open("sheep.txt", mode="w", encoding="utf-8") as sheep :
    #繰り返し処理
    for i in range(num):
        ##ファイルに書き込む
        sheep.write(f"ひつじが{i+1}匹\n")