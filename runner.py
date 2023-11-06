import os


def choose_lab():
    while True:
        try:
            lab_number = int(input("Введіть номер лабораторної роботи (1-4): "))
            if 1 <= lab_number <= 4:
                return lab_number
            else:
                print("Введений номер не відповідає жодній лабораторній роботі (1-4).")
        except ValueError:
            print("Введіть номер лабораторної роботи у відповідному форматі.")


# Отримання номера лабораторної роботи від користувача
lab_number = choose_lab()

# Побудова шляху до вибраного файлу лабораторної роботи
lab_file_path = os.path.join(f"lab{lab_number}", f"lab{lab_number}.py")

if os.path.isfile(lab_file_path):
    # Запуск вибраного файлу з використанням кодування 'utf-8'
    with open(lab_file_path, "r", encoding="utf-8") as lab_file:
        exec(lab_file.read())
else:
    print(f"Файл для лабораторної роботи {lab_number} не знайдено.")
