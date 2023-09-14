import math

memory = []
print("Starting...")


while True:
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
        chooseOperator = input("Enter an arithmetic operator you prefer: ")

        if chooseOperator not in ["+", "-", "*", "/", "^", "√", "%"]:
            print(
                "Invalid operator has been chosen. Please, follow the list and try one more time!. Please, reboot the program."
            )
            break
        else:
            if chooseOperator == "+":
                result = value1 + value2
                print(result)
            elif chooseOperator == "-":
                result = value1 - value2
                print(result)
            elif chooseOperator == "*":
                result = value1 * value2
                print(result)
            elif chooseOperator == "/":
                if value1 == 0 or value2 == 0:
                    print("You can not divide by zero")
                else:
                    result = value1 / value2
                    print(result)
            elif chooseOperator == "^":
                result = value1**value2
                print(result)
            elif chooseOperator == "√":
                print("Alert! the square root working only with first number!")
                result = math.sqrt(value1)
                print(result)
            elif chooseOperator == "%":
                result = (value1 / value2) * 100
                print(result)

        saveIntoMemory = input("Do you want to save a result in memory? (Y/N): ")
        if saveIntoMemory.lower() == "y":
            memory.append(result)
            print(result)
            break

    moreCalc = input("Do you want make more calculations? (Y/N): ")
    if moreCalc.lower() != "y":
        print("Disposing...")
        break
    # else:
    #     value1 = float(input("Enter your first value: "))
    #     value2 = float(input("Enter your second value: "))

if memory is not None:
    print(f"Memory: {memory}")
