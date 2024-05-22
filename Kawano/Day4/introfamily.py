from  introduce import Intro
class IntroFam(Intro) :
    '''飼い猫の名前を定義する'''
    def __init__(self, name, age, catname):
        super().__init__(name, age)
        self.catname = catname

    def cat_out(self):
        catnametxt = "飼い猫の名前は、"+ self.catname + "です"
        return catnametxt
    
