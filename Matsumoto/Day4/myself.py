from introduce import Intro
import sys

name = sys.argv[1]
age = sys.argv[2]

intro = Intro(name, age)
print(intro.name_out())
print(intro.age_out())
