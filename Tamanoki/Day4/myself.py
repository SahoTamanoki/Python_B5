# introduce.pyを取り込む
from introduce import Intro

import sys
args = sys.argv

name = args[1]
age  = args[2]

# インスタンスを作成
outtext = Intro(name, age)
print(outtext.name_out()) #名前を表示
print(outtext.age_out())  #年齢を表示