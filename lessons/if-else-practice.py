choice: int = int(input("enter a number: "))

if choice < 50: 
    if choice < 25:
        print("A")
        quit()
    else:
        print("B")
        quit()

if choice > 75:
    print("C")
    quit()
else:
    print("D")
