usernameInput = input("username :")
passwordInput = input("Password :")
if usernameInput == "Thanakrit22" and passwordInput == "yoyo2211":
    print(" Your username and your password is correct")
    print("--------Welcome to YoYo shop--------  ")
    print("____________________________________")
    print(" 1. Vat Calculator")
    print(" 2. Price Calculator")
    userSelected = int(input(">>"))
    if userSelected == 1:
        price = int(input("Price (KR)"))
        Vat = 7
        result = price + (price * 7 / 100)
        print(result)
        print("___________________________________")
        print("Thanks you!!!!!")
    elif userSelected == 2:
        price1 = int(input("First Product Price :"))
        price2 = int(input("Second Product Price :"))
        print(price1 + price2)
        print("____________________________________")
        print("Thanks you!!!!!")
else:
    print (" Your username and your password is incorrect,please try again!!!!")