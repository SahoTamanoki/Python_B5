import sys
args = sys.argv

#引数を変数に代入
hm_class = args[1]              #値下げ対象の種別
price_down = int(args[2])   #値下げ額

#品目（品名と価格）を辞書型で定義
hinmoku = {"リンゴ":80 , "みかん":198, "バナナ":150, "ビール":360, "日本酒":580, "ラーメン":380, "うどん":128, "パスタ":258}

#区分ごとの定義
fruits = ("リンゴ", "みかん", "バナナ")            #果物類をタプルで定義
alcohol = ("ビール", "日本酒")                         #酒類をタプルで定義
noodles = ("ラーメン", "うどん", "パスタ")   #麺類をタプルで定義

#ここ以降にプログラムを書く
hm_input = ["果物類", "酒類", "麺類"]
hm_dic = {"果物類":fruits, "酒類":alcohol, "麺類":noodles}
for i in range(len(hm_input)):
    if hm_class == hm_input[i]:
        for j in range(int(len(hm_dic[hm_class]))):
            if hinmoku[hm_dic[hm_class][j]] > price_down:
                hinmoku[hm_dic[hm_class][j]] -= price_down
            else: hinmoku[hm_dic[hm_class][j]] = 1
print(hinmoku)
# if hm_class == "果物類":
#     for i in range(int(len(fruits))):
#         if hinmoku[fruits[i]] > price_down:
#             hinmoku[fruits[i]] -= price_down
#         else: hinmoku[fruits[i]] = 1
# elif hm_class == "酒類":
#     for i in range(int(len(alcohol))):
#         if hinmoku[alcohol[i]] > price_down:
#             hinmoku[alcohol[i]] -= price_down
#         else: hinmoku[alcohol[i]] = 1
# elif hm_class == "麺類":
#     for i in range(int(len(noodles))):
#         if hinmoku[noodles[i]] > price_down:
#             hinmoku[noodles[i]] -= price_down
#         else: hinmoku[noodles[i]] = 1
# print(hinmoku,end="")

