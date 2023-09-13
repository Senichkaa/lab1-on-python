print("hello world")

value1 = ""
value2 = ""

print("Enter your values:")
input(value1)
input(value2)

print("1. +")
print("2. -")
print("3. *")
print("4. /")
chooseOperator = input("Enter a number of your arithmetic operator:")

if chooseOperator not in ["1", "2", "3", "4"]:
    print(
        "Invalid operator has been chosen. Please, follow the list and try one more time!"
    )
else:
    if chooseOperator == "1":
        print("Result of + is: ", value1 + value2)
    elif chooseOperator == "2":
        print("Result of - is: ", value1 - value2)
    elif chooseOperator == "3":
        print("Result of * is: ", value1 * value2)
    elif chooseOperator == "4":
        print("Result of / is: ", value1 / value2)


# if chooseOperator not in
