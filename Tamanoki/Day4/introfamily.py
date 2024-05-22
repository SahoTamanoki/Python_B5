from introduce import Intro

#基底クラスに「intro」を持つ派生クラスの定義
class IntroFam(Intro):
    def __init__(self, name, age, cat_name): #メゾット
        # オリジナルのintroduce.pyから、nameとageを取り込む。 基底クラスのメゾットを呼び出す。
        super().__init__(name, age)
        self.cat_name = cat_name

#飼い猫の名前を編集するメゾット
    def cat_out(self):
        cattxt = "飼い猫の名前は、" +self.cat_name + "です"
        return cattxt
    
