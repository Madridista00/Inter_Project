"""
2.1 კალკულატორი
კალკულატორის ფუნქცია მომხმარებლებს საშუალებას აძლევს შეასრულონ ძირითადი არითმეტიკული მოქმედებები (+, -, *, /).
მომხმარებლებს შეუძლიათ შეიყვანონ ორი რიცხვი და შემდეგ აირჩიონ ოპერაცია შედეგის მისაღებად.
კალკულატორი ასევე შეიცავს შეყვანის ვალიდაციას არასწორი შეყვანების დასამუშავებლად.

"""

# ori ricxvis damatebis funqcia
def add(x, y):
    return x + y

# ori ricxvis gamoklebis funqcia
def subtract(x, y):
    return x - y

# ori ricxvis gamravlebis funqcia
def multiply(x, y):
    return x * y

# ori ricxvis gayofis funqcia
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Nulze gayofa sheudzlebelia!")
        return None
    return result


while True:
    num1 = num2 = ''

    while type(num1) not in (int, float):
        try:
            num1 = eval(input("Sheiyvanet pirveli ricxvi: "))
        except (NameError, SyntaxError):
            print("Please, enter a valid nimber...\n")

    while type(num2) not in (int, float):
        try:
            num2 = eval(input("Sheiyvanet meore ricxvi: "))
        except (NameError, SyntaxError):
            print("Please, enter a valid nimber...\n")

    print("Shesadzlebeli moqmedebebis chamonatvali.")
    print("1.Mimateba")
    print("2.Gamokleba")
    print("3.Gamravleba")
    print("4.Gayofa")

    # momxmareblis archevani
    choice = input("Airchiet shesasrulebeli moqmedebis shesabamisi ricxvi - (1/2/3/4): ")

    # momxmareblis archevanis shemowmeba
    if choice in ('1', '2', '3', '4'):
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
    
        elif choice == '4':
            result = divide(num1, num2)
            if result is not None:
                print(num1, "/", num2, "=", result)
        
        # momxmarebels tu surs kidev sheasrulos moqmedeba
        next_calculation = input("Kidev gsurt moqmedebis shesruleba? (ki/ara): ")
        if next_calculation == "ara":
          break
    else:
        print("Araswori monacemi")
print("Madloba, gisurvebt karg dges!")
    