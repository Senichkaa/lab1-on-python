import math


class AppCalculator:
    """
    The AppCalculator class represents a simple calculator application.

    Attributes:
    - result (float): The result of the latest calculation.

    Methods:
    - __init__(): Initializes a new AppCalculator instance.
    - get_input_num(prompt: str): Get a valid float input from the user.
    - input_numbers(): Get two valid float numbers from the user.
    - choose_operator(): Get a valid arithmetic operator from the user.
    - calculation(value1: float, value2: float): Perform the calculation based on the selected operator.
    - more_calculations(): Ask the user if they want to perform more calculations.
    - run(): Run the calculator application.

    Example Usage:
    >>> calculator = AppCalculator()
    >>> calculator.run()
    """

    def __init__(self):
        """
        Initializes a new AppCalculator instance.

        This initializes the result attribute.

        Returns:
        - None
        """
        self.result = 0.0

    def get_input_num(self, prompt):
        """
        Get a valid float input from the user.

        Parameters:
        - prompt (str): The prompt to display for input.

        Returns:
        - float: The valid float entered by the user.
        """
        while True:
            try:
                value = float(input(prompt))
                return value
            except ValueError:
                print("Please enter a valid number.")

    def input_numbers(self):
        """
        Get two valid float numbers from the user.

        Returns:
        - tuple(float, float): The two valid float numbers entered by the user.
        """
        try:
            value1 = float(input("Enter your first value: "))
            value2 = float(input("Enter your second value: "))
            return value1, value2
        except ValueError:
            print("Invalid input for numbers.")
            return None

    def choose_operator(self):
        """
        Get a valid arithmetic operator from the user.

        Prints a list of valid operators and continues prompting until a valid
        operator is entered.

        Returns:
        - None
        """
        while True:
            self.operator = input(
                "Enter an arithmetic operator you prefer: + - * / ^ √ % : "
            )
            if self.operator not in ["+", "-", "*", "/", "^", "√", "%"]:
                print(
                    "Invalid operator has been chosen. Please, follow the list and try one more time!. Please, reboot the program."
                )
                break
            else:
                break

    def calculation(self, value1, value2):
        """
        Perform the calculation based on the selected operator.

        Parameters:
        - value1 (float): The first value for the calculation.
        - value2 (float): The second value for the calculation.

        Returns:
        - None
        """
        if self.operator == "+":
            self.result = value1 + value2
        elif self.operator == "-":
            self.result = value1 - value2
        elif self.operator == "*":
            self.result = value1 * value2
        elif self.operator == "/":
            if value2 == 0:
                raise ZeroDivisionError("You cannot divide by zero")
            self.result = value1 / value2
        elif self.operator == "^":
            self.result = value1**value2
        elif self.operator == "√":
            print("Alert! the square root works only with the first number!")
            self.result = math.sqrt(value1)
        elif self.operator == "%":
            self.result = (value1 / value2) * 100

    @staticmethod
    def more_calculations(self):
        """
        Ask the user if they want to perform more calculations.

        Returns:
        - bool: True if the user wants to perform more calculations, False otherwise.
        """
        more_calc = input("Do you want to make more calculations? (Y/N): ")
        return more_calc.lower() == "y"

    def run(self):
        """
        Run the calculator application.

        Performs a sequence of calculations based on user input until the user
        decides to stop.

        Returns:
        - None
        """
        print("Starting...")
        while True:
            values = self.input_numbers()
            self.choose_operator()
            self.calculation(*values)

            if not self.more_calculations():
                print("Disposing...")
                break
