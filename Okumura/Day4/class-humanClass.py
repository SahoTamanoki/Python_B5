class Human:
    '''人間を表すクラス'''

    def search(self, place):
        '''周りを見る処理'''
        pass
    
    def take(self, food):
        '''物をつかむ処理'''
        self.food = food
        pass
    
    def open_mouth(self):
        '''口を開ける処理'''
        pass

    def eat(self):
        '''食物を食べる処理'''
        print(self.food + "を食べました")


hito = Human()
hito.take("Banana")
hito.eat

hito2 = Human()
hito2.take("ラーメン")
hito2.eat
