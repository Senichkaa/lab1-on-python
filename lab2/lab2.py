import math


class History:
    def __init__(self):
        self.memory = []  # Інкапсуляція, що створює список пам'яті в класі
        self.history = []  # Інкапсуляція, що створює історію обчислень

    def save_to_memory(self, result):
        self.memory.append(result)

    def add_to_history(self, value1, operator, value2, result):
        calculation = (value1, operator, value2, result)
        self.history.append(calculation)

    def view_history(self):
        if not self.history:
            return "History of calculations: No records"

        history_str = "History of calculations:"
        for calculation in self.history:
            history_str += f"\n{calculation[0]} {calculation[1]} {calculation[2]} = {calculation[3]}"

        return history_str


class Calculator:
    def __init__(self):
        self.history = (
            History()
        )  # Створюємо об'єкт класу History для зберігання історії та пам'яті
        self.decimals = 2  # Інкапсуляція, що визначає кількість знаків після коми

    def input_numbers(self):
        self.value1 = float(input("Enter your first value: "))
        self.value2 = float(input("Enter your second value: "))

    def choose_operator(self):
        while True:
            self.operator = input(
                "Enter an arithmetic operator you prefer: + - * / ^ √ % : "
            )
            # Якщо некоректно - ерор в консоль + рестарт
            if self.operator not in ["+", "-", "*", "/", "^", "√", "%"]:
                print(
                    "Invalid operator has been chosen. Please, follow the list and try one more time!. Please, reboot the program."
                )
                break
            else:
                break

    def calculation(self):
        if self.operator == "+":
            self.result = self.value1 + self.value2
        elif self.operator == "-":
            self.result = self.value1 - self.value2
        elif self.operator == "*":
            self.result = self.value1 * self.value2
        elif self.operator == "/":
            if self.value2 == 0:
                raise ZeroDivisionError("You cannot divide by zero")
            self.result = self.value1 / self.value2
        elif self.operator == "^":
            self.result = self.value1**self.value2
        elif self.operator == "√":
            print("Alert! the square root works only with the first number!")
            self.result = math.sqrt(self.value1)
        elif self.operator == "%":
            self.result = (self.value1 / self.value2) * 100

    def change_decimals(self):
        change_decimals = input(
            f"Enter a number of decimals if you want to change the default parameter: "
        )
        if change_decimals:
            self.decimals = int(change_decimals)
            self.result = f"{self.result:.{self.decimals}f}"
            print(f"Result after changing: {self.result}")

    def memory_save(self):
        save_into_memory = input("Do you want to save the result in memory? (Y/N): ")
        if save_into_memory.lower() == "y":
            self.history.save_to_memory(self.result)

    def more_calculations(self):
        more_calc = input("Do you want to make more calculations? (Y/N): ")
        return more_calc.lower() == "y"

    def run(self):
        print("Starting...")
        while True:
            self.input_numbers()
            self.choose_operator()
            self.calculation()
            self.change_decimals()
            self.memory_save()
            self.history.add_to_history(
                self.value1, self.operator, self.value2, self.result
            )
            if not self.more_calculations():
                print("Disposing...")
                break
        self.history.view_history()


if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
