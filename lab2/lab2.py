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

    # Старт програми, а саме виконання всіх блоків-функцій описаних вище
    def run(self):
        print("Starting...")
        while True:
            self.input_numbers()

# Основна частина програми
if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
