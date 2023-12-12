import os
import sys

# Додаємо шлях до каталогу 'lab4' до шляху пошуку модулів
sys.path.append(os.path.join(os.path.dirname(__file__), "lab4"))

from source.core.lab4.logic import AsciiArtProcessor


def main() -> None:
    symbol_set = {
        "@": "lab4/arts/art_symbol_at_sign.txt",
        "#": "lab4/arts/art_symbol_hash.txt",
        "*": "lab4/arts/art_symbol_star.txt",
        "%": "lab4/arts/art_symbol_percent.txt",
        "&": "lab4/arts/art_symbol_ampersand.txt",
    }

    while True:
        selected_symbol = input("Select a symbol (@, #, *, %, &): ")
        if selected_symbol not in symbol_set:
            print("Error! Invalid symbol.")
            continue

        file_path = symbol_set[selected_symbol]
        processor = AsciiArtProcessor(file_path)

        while True:
            color = processor.color_selecting()
            if color is None:
                print("Error! Invalid color choice.")
                continue

            while True:
                text = processor.text_validate()

                while True:
                    alignment = input(
                        "Choose text align (left, center, right): "
                    ).lower()
                    if alignment not in ["left", "center", "right"]:
                        print("Error! Invalid text align.")
                    else:
                        break

                while True:
                    try:
                        max_width = int(input("Enter maximum width: "))
                        if max_width <= 0:
                            print("Error. Maximum width must be a int > 0.")
                        else:
                            break
                    except ValueError as e:
                        print(e)

                while True:
                    try:
                        print("The result of ASCII art:")
                        processor.print_art(text, alignment, max_width, color)

                        save_choice = input(
                            "Do you want to save the ASCII art(.txt) (yes/no): "
                        ).lower()
                        if save_choice == "yes":
                            output_file_name = input(
                                "Enter the file name to save to(.txt): "
                            )
                            processor.save_file(
                                processor.print_art(text, alignment, max_width, color),
                                output_file_name,
                            )
                            print("ASCII art saved to", output_file_name)

                        continue_choice = input(
                            "Do you want to continue and draw new ASCII art? (yes/no): "
                        ).lower()
                        if continue_choice != "yes":
                            exit()  # Exit the program

                        break
                    except ValueError as e:
                        print(e)
                        max_width = int(input("Enter maximum width: "))
