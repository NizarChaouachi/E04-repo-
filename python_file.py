while True:    
    try:
        n1 = int(input("enter a number: "))
        n2 = int(input("enter a number: "))

        print(n1 + n2)
        break
    except ValueError:
        print("wrong input please enter a number.")

