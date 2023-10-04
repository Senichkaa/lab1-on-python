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

            
    # Калькуляція чисел і помилки в разі неправильного вибору одного з числа
    def calculation(self):
        if self.choose_operator == "+":
            self.result = self.value1 + self.value2
        elif self.choose_operator == "-":
            self.result = self.value1 - self.value2
        elif self.choose_operator == "*":
            self.result = self.value1 * self.value2
        elif self.choose_operator == "/":
            if self.value1 == 0 or self.value2 == 0:
                print("You can not divide by zero")
            else:
                self.result = self.value1 / self.value2
        elif self.choose_operator == "^":
            self.result = self.value1**self.value2
        elif self.choose_operator == "√":
            print("Alert! the square root working only with the first number!")
            self.result = math.sqrt(self.value1)
        elif self.choose_operator == "%":
            self.result = (self.value1 / self.value2) * 100
            
    # Зміна числа після коми
    def change_decimals(self):
        change_decimals = input(
            f"Enter a number of decimals if you want to change the default parameter: "
        )
        if change_decimals:
            self.decimals = int(change_decimals)  # Інкапсуляція: змінна decimals змінюється в межах класу
            self.result = f"{self.result:.{self.decimals}f}"  # Поліморфізм: форматування результату залежно від decimals
            print(f"Result after changing: {self.result}")
            
    # Збереження в пам'ять
    def memory_save(self):
        save_into_memory = input("Do you want to save the result in memory? (Y/N): ")
        if save_into_memory.lower() == "y":
            self.memory.append(self.result)  # Інкапсуляція: робимо зміни в пам'яті через метод класу
            self.history.append((self.value1, self.choose_operator, self.value2, self.result))

    # Запит на перегляд історії та вивід значень
    def view_history(self):
        save_into_history = input("Do you want to view the history of your calculations? (Y/N): ")
        if save_into_history.lower() == "y":
            print("History of calculations:")
            for history_item in self.history:
                value1, choose_operator, value2, result = history_item
                print(f"{value1} {choose_operator} {value2} = {result}")
            if self.memory:
                print(f"Memory: {self.memory}")

    # Старт програми, а саме виконання всіх блоків-функцій описаних вище
    def run(self):
        print("Starting...")
        while True:
            self.input_numbers()
            self.choose_operator()
            self.calculation()
            self.change_decimals()
            self.memory_save()
            self.view_history()
            

    
# Основна частина програми
if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
