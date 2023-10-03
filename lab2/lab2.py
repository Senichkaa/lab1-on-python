import math

class Calculator:
    # Конструктор з атрибутами класу 
    def __init__(self): 
        self.memory = []  # Інкапсуляція, що створює список пам'яті в класі
        self.history = []  # Інкапсуляція, що створює історію обчислень
        self.decimals = 2  # Інкапсуляція, що визначає кількість знаків після коми

    # Ввід чисел 
    def input_numbers(self):
        self.value1 = float(input("Enter your first value: "))
        self.value2 = float(input("Enter your second value: "))
        
    # Вибір дії над числами 
    def choose_operator(self):
        while True:
            print("1. +")
            print("2. -")
            print("3. *")
            print("4. /")
            print("5. ^")
            print("6. √")
            print("7. %")
            self.choose_operator = input("Enter an arithmetic operator you prefer: ")

            # Якщо некоректно - ерор в консоль + рестарт
            if self.choose_operator not in ["+", "-", "*", "/", "^", "√", "%"]:
                print(
                    "Invalid operator has been chosen. Please, follow the list and try one more time!. Please, reboot the program."
                )
                break
            else:
                break

    # Старт програми, а саме виконання всіх блоків-функцій описаних вище
    def run(self):
        print("Starting...")
        while True:
            self.input_numbers()
            self.choose_operator()

# Основна частина програми
if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
