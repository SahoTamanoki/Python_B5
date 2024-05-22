#自販機にある商品と値段の格納
from_drink_to_price = {"お茶":110, "コーヒー":100, "ソーダ":160, "コーンポタージュ":130}
#お釣りの初期値格納
from_currency_to_count = {"5000円":0, "1000円":0, "500円":0, "100円":0, "50円":0, "10円":0}
#格納商品の出力と投入金額の入力促し
for drink_name in from_drink_to_price.keys():
    print(f"{drink_name}:{from_drink_to_price[drink_name]}\n")
user_money = int(input("投入金額を入力してください"))

#入力金額の正否判定
upper_money = 10000
while user_money > upper_money:
    user_money = int(input(f"{upper_money}を超える金額は投入できません。再度投入金額を入力してください"))
if user_money < min(from_drink_to_price.values()):
    while user_money >= 500:
        user_money -= 500
        count_500 += 1
    
