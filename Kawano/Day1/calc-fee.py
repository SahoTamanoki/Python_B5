#年齢別の値段
price_child= int(500)
price_adult = int(1000)
price_silver = int(700)
#年齢の入力
num_child = int(input("13歳未満の人数は？"))
num_adult = int(input("13歳~64歳の人数は？"))
num_silver = int(input("65歳以上の人数は？"))

#処理
if age >= 65:
    print(f"料金は{child}円です。")
elif age > 13:
    print(f"料金は{adult}円です。")
else:
    print(f"料金は{child}円です。")
