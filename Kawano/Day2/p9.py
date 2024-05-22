# 引数設定
import sys
args = sys.argv

# リストを格納
animals = ["giraffe", "tiger", "zebra", "elephant", "lion"]
# 挿入(第1引数の場所に第2引数の値を)
animals.insert(int(args[1]),args[2])
# 削除
animals.pop()
# 昇順に並び替え
animals.sort()
# 出力
print(animals,end="")