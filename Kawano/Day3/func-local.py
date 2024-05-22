value = 100

def changeValue():
    global value
    value = 20
    print(f"value = {value}")

changeValue()
print(f"value = {value}")