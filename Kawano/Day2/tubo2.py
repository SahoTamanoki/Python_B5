while True:
    user = int(input("坪数を教えてください"))
    if user == "" or user == 0:break
    tubo = int(user)
    m2 = tubo * 3.31
    s = f"{tubo}坪は{m2}平方メートルです"
    print(s)
