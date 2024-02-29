"""
2.1 კალკულატორი
კალკულატორის ფუნქცია მომხმარებლებს საშუალებას აძლევს შეასრულონ ძირითადი არითმეტიკული მოქმედებები (+, -, *, /).
მომხმარებლებს შეუძლიათ შეიყვანონ ორი რიცხვი და შემდეგ აირჩიონ ოპერაცია შედეგის მისაღებად.
კალკულატორი ასევე შეიცავს შეყვანის ვალიდაციას არასწორი შეყვანების დასამუშავებლად.

"""
# Function for addition
def add(x, y):
    return x + y

# Function for subtraction
def subtract(x, y):
    return x - y

# Function for multiplication
def multiply(x, y):
    return x * y

# Function for division
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None
    return result

while True:
    num1, num2 = None, None

    while num1 is None:
        try:
            num1 = float(input("Enter the first number: "))
        except ValueError:
            print("Please enter a valid number...")

    while num2 is None:
        try:
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Please enter a valid number...")

    while True:
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        try:
            choice = int(input("Enter choice (1/2/3/4): "))
        except ValueError:
            print("Invalid input. Please enter a valid choice.")
            continue

        if choice in (1, 2, 3, 4):
            if choice == 1:
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == 2:
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif choice == 3:
                print(num1, "*", num2, "=", multiply(num1, num2))
            elif choice == 4:
                result = divide(num1, num2)
                if result is not None:
                    print(num1, "/", num2, "=", result)
            
            while True:
                next_calculation = input("Do you want to perform another calculation with the same numbers? (yes/no): ")
                if next_calculation.lower() not in {"yes", "no"}:
                    print("Invalid choice. Please enter 'yes' or 'no'.")
                    continue
                else:
                    break
            if next_calculation.lower() != "yes":
                break
        else:
            print("Invalid input. Please enter a valid choice (1/2/3/4).")

    while True:
        exit_choice = input("Thank you for using the calculator! Do you want to exit? (yes/no): ")
        if exit_choice.lower() not in {"yes", "no"}:
            print("Invalid choice. Please enter 'yes' or 'no'.")
            continue
        else:
            break
    if exit_choice.lower() == "yes":
        break
print("Good Bye!")
    