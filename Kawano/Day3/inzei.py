def inzei(price, sales, per):
    rate = per / 100
    ro = int(price*sales*rate)
    return ro

i = input("定価は？")
price = int(i)

i = input("発行部数は？")
sales = int(i)

i = input("印税率は？")
per = int(i)

v = inzei(price, sales, per)
print(f"印税は{v}円です。")


