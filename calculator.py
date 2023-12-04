while True : 
    user = str(input("Enter your name : "))
    print(" hallo " + user )
    x = float(input("plese Enter frist num ?")) 
    symbol = input("symbol " + " ")
    y = float(input("plese Enter second num?"))
    try :
        if  symbol == "+" :
            print(x+y)
        elif symbol == "-" : 
            print(x-y)
        elif symbol == "/": 
            print(x // y)
        elif symbol == "*" : 
            print(x*y)
        else :
            print(" only symbol ")
    except ZeroDivisionError:
        print("no division 0")
    except ValueError : 
        print("only number")
    finally :
        print("thanks for use my calculator  " + user)
    user = str(input("are u want calculat angin ? (yes / no ): ")).lower()
    if user != "yes" : 
        break 
