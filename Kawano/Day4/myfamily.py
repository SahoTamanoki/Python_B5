from introfamily import IntroFam
import sys
args = sys.argv
name = args[1]
age = args[2]
catname = args[3]

cat1 = IntroFam(name, age, catname)
print(cat1.name_out()) #
print(cat1.age_out())
print(cat1.cat_out())
