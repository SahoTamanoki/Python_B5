#引数設定
import sys
args = sys.argv
num = int(args[1])
i = 2
p = []

#素因数分解の処理
while num != 1 : #約数がある
    if num % i == 0: #iで割り切れるとき
        while num % i == 0: #iで割り切れなくなるまで
            num = num / i   
        p.append(i)
    else:i += 1

#出力
print(p)