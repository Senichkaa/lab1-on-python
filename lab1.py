print("hello world")

value1 = float(input("Enter your first value: "))
value2 = float(input("Enter your second value: "))

print("1. +")
print("2. -")
print("3. *")
print("4. /")
chooseOperator = input("Enter a number of your arithmetic operator:")

if chooseOperator not in ["+", "-", "*", "/"]:
    print(
        "Invalid operator has been chosen. Please, follow the list and try one more time!"
    )
else:
    if chooseOperator == "+":
        print(value1 + value2)
    elif chooseOperator == "-":
        print(value1 - value2)
    elif chooseOperator == "*":
        print(value1 * value2)
    elif chooseOperator == "/":
        print(value1 / value2)

# print(res)
