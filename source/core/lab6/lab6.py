import unittest
import sys

from importlib.machinery import SourceFileLoader

sys.path.append(
    r"C:\Users\super\Desktop\3kurs\1sem\smp\lab1-on-python\source\core\lab2"
)

lab2_module = SourceFileLoader(
    "calculator",
    r"C:\Users\super\Desktop\3kurs\1sem\smp\lab1-on-python\source\core\lab2\lab2.py",
).load_module()

lab2_module2 = SourceFileLoader(
    "history",
    r"C:\Users\super\Desktop\3kurs\1sem\smp\lab1-on-python\source\core\lab2\lab2.py",
).load_module()


class CalculatorTests(unittest.TestCase):
    def setUp(self):
        self.calculator = lab2_module.Calculator()
        self.history = lab2_module2.History()

    def test_addition(self):
        self.calculator.value1 = 5
        self.calculator.value2 = 3
        self.calculator.operator = "+"
        self.calculator.calculation()
        self.assertEqual(self.calculator.result, 8)

    def test_subtraction(self):
        self.calculator.value1 = 5
        self.calculator.value2 = 3
        self.calculator.operator = "-"
        self.calculator.calculation()
        self.assertEqual(self.calculator.result, 2)

    def test_multiplication(self):
        self.calculator.value1 = 5
        self.calculator.value2 = 3
        self.calculator.operator = "*"
        self.calculator.calculation()
        self.assertEqual(self.calculator.result, 15)

    def test_division(self):
        self.calculator.value1 = 6
        self.calculator.value2 = 2
        self.calculator.operator = "/"
        self.calculator.calculation()
        self.assertEqual(self.calculator.result, 3)

    def test_division_by_zero(self):
        self.calculator.value1 = 6
        self.calculator.value2 = 0
        self.calculator.operator = "/"
        with self.assertRaises(ZeroDivisionError):
            self.calculator.calculation()

    def test_save_to_memory(self):
        self.history.save_to_memory(42)
        self.assertEqual(self.history.memory, [42])

    def test_add_to_history(self):
        self.history.add_to_history(2, "+", 3, 5)
        self.assertEqual(self.history.history, [(2, "+", 3, 5)])

    def test_view_history_no_records(self):
        with self.subTest("No records"):
            expected_output = "History of calculations:"
            if not self.history.history:
                expected_output += " No records"
            self.assertMultiLineEqual(self.history.view_history(), expected_output)

    def test_view_history_with_records(self):
        with self.subTest("With records"):
            self.history.add_to_history(5, "+", 7, 12)
            self.history.add_to_history(10, "-", 3, 7)
            expected_output = "History of calculations:\n5 + 7 = 12\n10 - 3 = 7"
            self.assertMultiLineEqual(self.history.view_history(), expected_output)


def main():
    unittest.main()
