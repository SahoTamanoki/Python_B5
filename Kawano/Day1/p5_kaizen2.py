class passing:
    '''合否を表すクラス'''
    def __init__(self,):
        pass

#引数の設定
import sys
args = sys.argv
a = int(args[1])
b = int(args[2])
c = int(args[3])

#合格基準の設定
total = a + b + c
def passing_standard(point):
    return (a >= point and b >= point and c >= point)

#合否の処理
if (total >= 220 or passing_standard(70)) and passing_standard(50):
    print("合格",end="")
else:
    print("不合格",end="")
