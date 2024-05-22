#リストの作成
a = [1,"a",2,"b",3]
a

#リストの中身の取り出し方
a[1]
a[-1] #後ろから1番目
len(a) #要素の数を出す
a.append("c") #リストの最後に要素を追加

#if文
a = 30
b = 20
if a < b:
    print("aはbより小さいです。")
elif a == b:
    print("aはbより等しいです")
else:
    print("aはbより大きいです")

a = 30
b = 20
if a < b:
    print("aはbより小さいです。")
a + b #if文が当てはまらなくてもa + bをする


#for文…要素を変数に代入して処理を繰り返す
# for 変数 in データの塊（リストやrange）:
#　　　処理内容

a = [1,2,3,4,5]
for i in a:
    print(i)