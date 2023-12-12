import os
import pyfiglet
from termcolor import colored


def main() -> None:
    # Завдання 1: Введення користувача
    text = input("Введіть слово або фразу для перетворення в ASCII-арт: ")

    # Завдання 2: Бібліотека ASCII-арту
    def generate_ascii_art(text, font="standard"):
        try:
            ascii_art = pyfiglet.figlet_format(text, font=font)
            return ascii_art
        except Exception as e:
            return str(e)

    # Завдання 3: Вибір шрифту
    print("Доступні шрифти:")
    for font in pyfiglet.FigletFont.getFonts():
        print(font)
    selected_font = input(
        "Виберіть шрифт для ASCII-арту (напишіть назву шрифту або залиште порожнім для стандартного шрифту): "
    )

    # Завдання 4: Колір тексту
    colors = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]
    print("Доступні кольори:")
    for color in colors:
        print(color)
    selected_color = input(
        "Виберіть колір тексту для ASCII-арту (напишіть назву кольору або залиште порожнім для чорного кольору): "
    )

    # Завдання 7: Розмір ARTу
    width = int(input("Введіть ширину ASCII-арту: "))
    height = int(input("Введіть висоту ASCII-арту: "))

    # Завдання 8: Вибір символів
    character = input(
        "Введіть символ для відображення в ASCII-арті (за замовчуванням '@'): "
    )
    if not character:
        character = "@"

    # Завдання 9: Функція попереднього перегляду
    ascii_art_preview = generate_ascii_art(text, selected_font)
    print("\nПопередній перегляд ASCII-арту:")
    print(colored(ascii_art_preview, color=selected_color))

    # Завдання 10: Збереження у файл
    save_to_file = input("Зберегти ASCII-арт у файл? (y/n): ")
    if save_to_file.lower() == "y":
        file_name = input("Введіть ім'я файлу для збереження ('.txt'): ")
        if not file_name.endswith(".txt"):
            file_name += ".txt"

        output_folder = "output"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        file_path = os.path.join(output_folder, file_name)
        with open(file_path, "w") as file:
            file.write(generate_ascii_art(text, selected_font))

        print("ASCII-арт збережено у файлі '{}'.".format(file_path))
    else:
        print("ASCII-арт не збережено.")
