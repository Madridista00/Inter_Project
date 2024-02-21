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


print("Shesadzlebeli moqmedebebis chamonatvali.")
print("1.Mimateba")
print("2.Gamokleba")
print("3.Gamravleba")
print("4.Gayofa")

while True:
    # momxmareblis archevani
    choice = input("Airchiet shesasrulebeli moqmedebis shesabamisi ricxvi - (1/2/3/4): ")

    # momxmareblis archevanis shemowmeba
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Sheiyvanet pirveli ricxvi: "))
            num2 = float(input("Sheiyvanet meore ricxvi: "))
        except ValueError:
            print("Araswori monacemi. Gtxovt sheiyvanot ricxvi.")
            continue

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
    