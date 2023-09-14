import math

print("Starting...")

value1 = float(input("Enter your first value: "))
value2 = float(input("Enter your second value: "))

while True:
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    print("5. ^")
    print("6. √")
    print("7. %")
    chooseOperator = input("Enter a number of your arithmetic operator: ")

    if chooseOperator not in ["+", "-", "*", "/", "^", "√", "%"]:
        print(
            "Invalid operator has been chosen. Please, follow the list and try one more time!. Please, reboot the program."
        )
        break
    else:
        if chooseOperator == "+":
            print(value1 + value2)
        elif chooseOperator == "-":
            print(value1 - value2)
        elif chooseOperator == "*":
            print(value1 * value2)
        elif chooseOperator == "/":
            if value1 == 0 or value2 == 0:
                print("You can not divide by zero")
            else:
                print(value1 / value2)
        elif chooseOperator == "^":
            print(value1**value2)
        elif chooseOperator == "√":
            print("Alert! the square root working only with first number!")
            print(math.sqrt(value1))
        elif chooseOperator == "%":
            print((value1 / value2) * 100)

    moreCalc = input("Do you want make more calculations? (Y/N): ")
    if moreCalc.lower() != "y":
        print("Disposing...")
        break
    else:
        value1 = float(input("Enter your first value: "))
        value2 = float(input("Enter your second value: "))
