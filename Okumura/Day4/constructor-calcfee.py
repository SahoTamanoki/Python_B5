class CalcFee:
    def __init__(self) -> None:
        self.shipping_fee = 1000
        self.tax_rate = 0.08
        self.value = 0
    
    def addItem(self, price):
        ''' 商品の値段を加算する '''
        self.value += price
    
    def calc(self):
        ''' 最終的な料金を計算する '''
        total = self.value + self.shipping_fee
        tax = math.ceil(total*self.tax_rate)
        v = math.ceil(total + tax)
        return v
    
fee1 = CalcFee()
fee1.addItem(500)
print(fee1.calc(),"円")

fee2 = CalcFee()
fee2.shipping_fee = 1500
fee2.addItem(800)
fee2.addItem(500)
print(fee2.calc(),"円")
