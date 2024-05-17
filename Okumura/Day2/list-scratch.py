a = [10, 22, 30, 45]
print(type(a),a)

## tuple
number = ( 1, 2, 3 )

## set
colors = { "red" , "red" , "blue" }

fluits = set({ "orange" , "mango" , "mango" })

## culculate
box1 = {"ハンマー", "釘", "ペンチ"}
box2 = {"ハンマー"}

print(box1 - box2) # 釘、ペンチ
print('ベンチ' in box1) # True