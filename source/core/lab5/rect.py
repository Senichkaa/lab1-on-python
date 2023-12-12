from source.core.lab5.color_utils import color_applying, colors
from source.core.lab5.rect_generate import (
    generate_inner_rectangle,
    generate_middle_rectangles,
    generate_outer_rectangle,
)
from random import choice
import os


class RectangleArt:
    def __init__(
        self,
        width,
        height,
        outer_color="cyan",
        middle_color="green",
        inner_color="yellow",
        symbol_count=1,
        symbol_color="*",
    ):
        if width < 1 or height < 1:
            print("Error: Rectangle dimensions are less than 1.")
        else:
            self.width = width
            self.height = height
            self.outer_rectangle_color = outer_color
            self.middle_rectangle_color = middle_color
            self.inner_rectangle_color = inner_color
            self.symbol_count = symbol_count
            self.symbol_color = symbol_color
            self.outer_rectangle = generate_outer_rectangle(width, height, symbol_color)
            self.middle_rectangles = generate_middle_rectangles(
                width, height, symbol_color
            )
            self.inner_rectangle = generate_inner_rectangle(width, height, symbol_color)

    def set_outer_rectangle_color(self, color):
        self.outer_rectangle_color = color

    def set_middle_rectangle_color(self, color):
        self.middle_rectangle_color = color

    def set_inner_rectangle_color(self, color):
        self.inner_rectangle_color = color

    def combine_rectangles(self):
        combined_width = int((((self.width + self.height) / 2) + self.width) * 3)
        combined_height = int(((self.height + self.width) / 2) + self.height)

        combined_matrix = [
            [" " for _ in range(combined_width)] for _ in range(combined_height)
        ]

        for i in range(self.height):
            for j in range(self.width):
                combined_matrix[i][int(j * 3)] = self.outer_rectangle[i][j]

        middle_offset = 0
        for middle_rectangle, offset in self.middle_rectangles:
            for i in range(self.height):
                for j in range(self.width):
                    combined_matrix[i + offset][int(j * 3) + offset] = middle_rectangle[
                        i
                    ][j]
                middle_offset = offset

        inner_offset = middle_offset + 1
        for i in range(self.height):
            for j in range(self.width):
                combined_matrix[i + inner_offset][
                    int(j * 3) + inner_offset
                ] = self.inner_rectangle[i][j]

        return combined_matrix

    def draw_combined_rectangles(self):
        outer_color = choice(colors["multi"])
        middle_color = choice(colors["multi"])
        inner_color = choice(colors["multi"])

        for i in range(self.height):
            for j in range(self.width):
                # if self.outer_rectangle[i][j] == self.symbol_color:
                #     self.outer_rectangle[i][j] = color_applying(
                #         self.symbol_color, outer_color
                #     )
                if self.middle_rectangles:
                    for rect, offset in self.middle_rectangles:
                        if rect[i][j] == self.symbol_color:
                            rect[i][j] = color_applying(self.symbol_color, middle_color)

        if self.inner_rectangle:
            for i in range(self.height):
                for j in range(self.width):
                    if self.inner_rectangle[i][j] == self.symbol_color:
                        self.inner_rectangle[i][j] = color_applying(
                            self.symbol_color, inner_color
                        )

    def align_art(self, alignment, console_length):
        combined_matrix = self.combine_rectangles()
        max_length = max(len("".join(row)) for row in combined_matrix)

        if alignment == "center":
            for row in combined_matrix:
                print("".join(row).center(console_length))
        elif alignment == "right":
            for row in combined_matrix:
                print("".join(row).rjust(console_length))
        elif alignment == "left":
            for row in combined_matrix:
                print("".join(row))

    def scale_figure(self, scale_factor):
        if scale_factor <= 0:
            print("Error: Scale factor must be greater than 0.")
            return

        new_width = int(self.width * scale_factor)
        new_height = int(self.height * scale_factor)

        if new_width < 1 or new_height < 1:
            print("Error: Scaled dimensions are less than 1.")
            return

        self.width = new_width
        self.height = new_height

        self.outer_rectangle = generate_outer_rectangle(
            self.width, self.height, self.symbol_color
        )
        self.inner_rectangle = generate_inner_rectangle(
            self.width, self.height, self.symbol_color
        )
        self.middle_rectangles = generate_middle_rectangles(
            self.width, self.height, self.symbol_color
        )

    def convert_to_2d(self):
        print("Converting 3D art to 2D...")
        for row in self.inner_rectangle:
            print("  ".join(row))

    def save_file(self, output_file_name):
        # Збереження ASCII-арт в текстовий файл у папку "output"
        output_folder = "output"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        output_file_path = os.path.join(output_folder, output_file_name)

        with open(output_file_path, "w") as f:
            combined_matrix = self.combine_rectangles()
            for row in combined_matrix:
                f.write("".join(row) + "\n")

        print("ASCII-арт збережено у файлі '{}'.".format(output_file_path))
