enargy =3
while enargy > 0:
    print("+ 走る")
    print(" I energy =", enargy)
    enargy -= 1;
else:
    print("+ 止まる")

# repeat.py

total = 0
while True:
    try:
        num = int(input("整数を入力してください（終了する場合は0を入力）: "))
        total += num
        if total == 100:
            print("Just １００！")
            break
        elif total > 100:
            print("Over!")
            break
    except ValueError:
        print("無効な入力です。整数を入力してください。")
