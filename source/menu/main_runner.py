import os
import sys

sys.path.insert(0, "../")

from source.core.lab1 import lab1
from source.core.lab2 import lab2
from source.core.lab3 import lab3
from source.core.lab4 import lab4
from source.core.lab5 import lab5
from source.core.lab6 import lab6
from source.core.lab7 import lab7
from source.core.lab8 import lab8


class MainRunner:
    def choose_lab():
        while True:
            try:
                lab_number = int(input("Select a number of laboratory (1-8): "))
                if 1 <= lab_number <= 8:
                    return lab_number
                else:
                    print(
                        "Введений номер не відповідає жодній лабораторній роботі (1-8)"
                    )
            except ValueError:
                print("Введіть номер лабораторної роботи у відповідному форматі.")

    def run_lab(lab_number):
        labs = [None, lab1]

        if 1 <= lab_number <= 8:
            labs[lab_number].main()

    def run(self):
        while True:
            lab_number = self.choose_lab()

            if lab_number == 0:
                break

            self.run_lab(lab_number)
