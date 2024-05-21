class Intro:
    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
    
    def name_out(self) -> str:
        nametxt = "私の名前は、" + self.name + "です"
        return nametxt

    def age_out(self) -> str:
        agetxt = "年齢は、" + self.age + "歳です"
        return agetxt
