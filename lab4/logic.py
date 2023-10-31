class AsciiArtProcessor:
    def __init__(self, file_path):
        self.ascii_dict = self.load_art(file_path)

    def load_art(self, file_path, encoding="utf-8"):
        # Завантажує ASCII-арт з файлу
        ascii_dict = {}
        with open(file_path, "r", encoding=encoding) as file:
            content = file.read().strip().split('@symbol::')
            for item in content:
                lines = item.strip().split('\n')
                if lines:
                    symbol = lines[0]
                    ascii_dict[symbol] = [line.strip('^$') for line in lines[1:]]
        return ascii_dict   


    def text_validate(self):
        # Перевірка введеного тексту на допустимі символи
        while True:
            text = input("Enter a word or phrase: ")
            if all(c in self.ascii_dict or c == ' ' for c in text):
                return text
            else:
                print("Error. The input contains invalid characters. Please enter a valid phrase.")

    def color_selecting(self):
        # Вибір кольору тексту користувачем
        print("Available colors: white, green, cyan, red, blue, yellow, multi")
        color_choice = input("Select text color: ").lower()
        return color_choice

    def color_applying(self, text, color):
    # Застосування кольору до тексту
        colors = {
            'white': '\u001b[97m',
            'green': '\u001b[92m',
            'cyan': '\u001b[96m',
            'red': '\u001b[91m',
            'blue': '\u001b[94m',
            'yellow': '\u001b[93m',
            'yellow': '\u001b[95m',
            'multi': [
                '\u001b[97m',
                '\u001b[92m',
                '\u001b[96m',
                '\u001b[91m',
                '\u001b[94m',
                '\u001b[93m',
                '\u001b[95m'
            ]
        }
        reset_color = '\u001b[0m'
        
        if color == 'multi':
            colored_text = ''
            color_index = 0
            for char in text:
                color_code = colors['multi'][color_index % len(colors['multi'])]
                colored_text += color_code + char
                color_index += 1
            colored_text += reset_color
            return colored_text
        elif color in colors:
            return colors[color] + text + reset_color
        else:
            return text  # Повертаємо текст без зміни, якщо вибраний невідомий колір

    def print_art(self, text, alignment, max_width, color):
    # Виведення ASCII-арт на екран
        if not text:
         return []

        output_lines = [""] * 6
        for symbol in text:
            if symbol == ' ':
                for i in range(6):
                    output_lines[i] += ' '
            elif symbol in self.ascii_dict:
                symbol_lines = self.ascii_dict[symbol]
                for i in range(6):
                    output_lines[i] += symbol_lines[i]

        if len(output_lines[0]) > max_width:
            raise ValueError("Error. Maximum width is too small for the input phrase.")

        align_func = str.center if alignment == 'center' else str.rjust if alignment == 'right' else lambda x, width: x

        colored_output_lines = [self.color_applying(align_func(line, max_width), color) for line in output_lines]

        for line in colored_output_lines:
            print(line)

        return colored_output_lines


    def save_file(self, output_lines, output_file_name):
        # Збереження ASCII-арт в текстовий файл
        with open(output_file_name, 'w') as file:
            file.writelines(line + '\n' for line in output_lines)