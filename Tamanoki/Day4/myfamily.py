from introduce import Intro
from introfamily import IntroFam 

import sys
args = sys.argv

name = args[1]
age  = args[2]
cat_name = args[3]

# インスタンスを作成
outtext = IntroFam(name, age, cat_name)
print(outtext.name_out()) #名前を表示
print(outtext.age_out())  #年齢を表示
print(outtext.cat_out())

