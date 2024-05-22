from introduce import Intro
import sys
args = sys.argv

name = args[1]
age = args[2]

kawano = Intro(name,age)
print(kawano.name_out())
print(kawano.age_out())
