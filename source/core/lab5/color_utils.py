# color_utils.py
colors = {
    'white': '\u001b[97m',
    'green': '\u001b[92m',
    'cyan': '\u001b[96m',
    'red': '\u001b[91m',
    'blue': '\u001b[94m',
    'yellow': '\u001b[93m',
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

def color_selecting():
    print("Available colors: white, green, cyan, red, blue, yellow, multi")
    color_choice = input("Select text color: ").lower()
    return color_choice

def color_applying(text, color):
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
