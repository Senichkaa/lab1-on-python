from color_utils import color_applying, colors
from random import choice

def generate_outer_rectangle(width, height, symbol_color):
    rectangle = [[" " for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            if j == 0 or i == 0:
                rectangle[i][j] = symbol_color
    return rectangle

def generate_middle_rectangles(width, height, symbol_color):
    middle_rectangles = []
    if width > 2 and height > 2:
        offset = 1
        for _ in range(height // 2 - 1):
            rectangle = [
                [" " for _ in range(width)] for _ in range(height)
            ]
            for i in range(height):
                for j in range(width):
                    if i == 0 and (j == 0 or j == width - 1):
                        rectangle[i][j] = symbol_color
                    elif i == height - 1 and j == 0:
                        rectangle[i][j] = symbol_color
            middle_rectangles.append((rectangle, offset))
            offset += 1
    return middle_rectangles

def generate_inner_rectangle(width, height, symbol_color):
    rectangle = [[" " for _ in range(width)] for _ in range(height)]
    if width > 2 and height > 2:
        offset_right = (width // 2) + 3
        offset_down = height // 2
        for i in range(height):
            for j in range(width):
                if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                    rectangle[i][j] = symbol_color
                if (
                    i >= offset_down
                    and i < height - offset_down
                    and j >= offset_right
                    and j < width - offset_right
                ):
                    rectangle[i][j] = " "
    return rectangle
