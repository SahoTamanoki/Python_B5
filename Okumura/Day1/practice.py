# mynameout.py
import sys
args = sys.argv

name = args[1]
print('Hello ' + name + ' !',end="")

# culc.py
import sys
args = sys.argv

cul_args = int(args[1]) + int(args[2]) + int(args[3])

print(cul_args,end="")

# outtext.py
import sys
args = sys.argv

food = args[1]
print("I don't like " + '"' + food +'"', end="")

# inputname.py
name = input("What's your name? ")
print( 'Hello, ' + name + "!" )

# oddeven.py
import sys
args = sys.argv

num = int(args[1])

if num % 2 == 0:
    print('偶数', end="")
else:
    print('奇数', end="")
    

# test.py
import sys
args = sys.argv

a = int(args[1])
b = int(args[2])
c = int(args[3])

if a >= 70 and b >= 70 and c >= 70:
        print('合格', end="")
elif a + b + c >= 220:
    if a >= 50 and b >= 50 and c >= 50:
        print('合格', end="")
    else:
        print('不合格', end="")
else:
    print('不合格', end="")

# salary.py
import sys
args = sys.argv

salary = int(args[1])

if salary > 1000000:
     tax = round((salary - 1000000) * 0.2) + round(1000000 * 0.1)
     paid = salary - tax
else:
     tax = round(salary * 0.1)
     paid = round(salary - tax)

print('支給額:' + str(paid) + '、' + '税額:' + str(tax),end="")