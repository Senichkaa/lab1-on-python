import os
import sys

# Отримання поточного каталогу, де розташований runner.py
current_directory = os.path.dirname(os.path.abspath(__file__))

# Додайте шлях до папки 'lab5' та папки 'lab8' до шляху пошуку модулів
sys.path.append(os.path.join(current_directory, "lab5"))
sys.path.append(os.path.join(current_directory, "lab8"))


def choose_lab():
    while True:
        try:
            lab_number = int(input("Select a number of laboratory (1-8): "))
            if 1 <= lab_number <= 8:
                return lab_number
            else:
                print("Введений номер не відповідає жодній лабораторній роботі (1-8)")
        except ValueError:
            print("Введіть номер лабораторної роботи у відповідному форматі.")


def run_lab(lab_number):
    if lab_number == 8:
        lab_file_path = os.path.join("lab8", "lab8.py")
    else:
        lab_file_path = os.path.join(f"lab{lab_number}", f"lab{lab_number}.py")

    if os.path.isfile(lab_file_path):
        try:
            with open(lab_file_path, "r", encoding="utf-8") as lab_file:
                exec(lab_file.read())
        except Exception as e:
            print(f"Помилка при виконанні файлу: {str(e)}")
    else:
        print(f"Файл для лабораторної роботи {lab_number} не знайдено.")


if __name__ == "__main__":
    lab_number = choose_lab()
    run_lab(lab_number)
