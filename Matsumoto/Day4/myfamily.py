from introfamily import IntroFam
import sys

args = sys.argv
name = args[1]
age = args[2]
cat = args[3]

intro_fam = IntroFam(name, age, cat)
print(intro_fam.name_out())
print(intro_fam.age_out())
print(intro_fam.cat_out())