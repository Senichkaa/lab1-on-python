
import source.core.lab1.lab1 as lab1
import source.core.lab2.lab2 as lab2
import source.core.lab3.lab3 as lab3
import source.core.lab4.lab4 as lab4
import source.core.lab5.lab5 as lab5
import source.core.lab6.lab6 as lab6
import source.core.lab7.lab7 as lab7
import source.core.lab8.lab8 as lab8


def choose_lab():
    while True:
        lab_number = int(input("Select a number of laboratory (1-8): "))
        if 1 <= lab_number <= 8:
            if lab_number == 1:
                lab1.main()
            elif lab_number == 2:
                lab2.main()
            elif lab_number == 3:
                lab3.main()
            elif lab_number == 4:
                lab4.main()
            elif lab_number == 5:
                lab5.main()
            elif lab_number == 6:
                lab6.main()
            elif lab_number == 7:
                lab7.main()
            elif lab_number == 8:
                lab8.main()
            elif lab_number == 0:
                break
        else:
            print("Введений номер не відповідає жодній лабораторній роботі (1-8)")


if __name__ == "__main__":
    choose_lab()
