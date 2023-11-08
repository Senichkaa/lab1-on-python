import os
import sys

# Додайте шлях до папки 'lab5' до шляху пошуку модулів
sys.path.append("lab5")


def choose_lab():
    while True:
        try:
            lab_number = int(input("Select a number of laboratory (1-6): "))
            if 1 <= lab_number <= 6:
                return lab_number
            else:
                print("Введений номер не відповідає жодній лабораторній роботі (1-6)")
        except ValueError:
            print("Введіть номер лабораторної роботи у відповідному форматі.")


# Отримання номера лабораторної роботи від користувача
lab_number = choose_lab()

# Отримання поточного каталогу, де розташований runner.py
current_directory = os.path.dirname(os.path.abspath(__file__))

# Побудова шляху до вибраного файлу лабораторної роботи
lab_file_path = os.path.join(
    current_directory, f"lab{lab_number}", f"lab{lab_number}.py"
)

if os.path.isfile(lab_file_path):
    try:
        with open(lab_file_path, "r", encoding="utf-8") as lab_file:
            exec(lab_file.read())
    except Exception as e:
        print(f"Помилка при виконанні файлу: {str(e)}")
else:
    print(f"Файл для лабораторної роботи {lab_number} не знайдено.")
