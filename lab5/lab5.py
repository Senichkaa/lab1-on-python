from rect import RectangleArt
from color_utils import color_selecting, colors

if __name__ == "__main__":
    console_length = 200

    while True:
        print("Options: ")
        print("1. Draw a cube")
        print("2. Draw a parallelepiped")
        print("0. Exit")

        choice = input("Select an option: ")

        if choice == "0":
            print("Exit the program.")
            break
        elif choice not in ["1", "2"]:
            print("Invalid option select. Try again")
            continue
        if choice in ["1", "2"]:
            if choice == "1":
                while True:
                    length = input(
                        "Enter the length of the cube (Your choose must be >= or = 4): "
                    )
                    try:
                        length = int(length)
                        if length < 4:
                            print("Length must be >= or = to 4")
                        else:
                            break
                    except ValueError:
                        print("Please enter a valid number")
            if choice == "2":
                while True:
                    length = input(
                        "Enter the length of the parallelepiped (must be a number >= or = to 4): "
                    )
                    width = input(
                        "Enter the width of the parallelepiped (must be a number >= or = to 4): "
                    )
                    try:
                        length = int(length)
                        width = int(width)
                        if length < 4 or width < 4:
                            print("Length and width must be >= or = to 4. Try again")
                        else:
                            break
                    except ValueError:
                        print("Please enter a valid number")
            print()
            while True:
                color_choice = color_selecting()

                if choice == "1":
                    rectangle_art = RectangleArt(
                        length,
                        length,
                        outer_color=color_choice,
                        middle_color=color_choice,
                        inner_color=color_choice,
                    )
                elif choice == "2":
                    rectangle_art = RectangleArt(
                        length,
                        width,
                        outer_color=color_choice,
                        middle_color=color_choice,
                        inner_color=color_choice,
                    )
                print()
                while True:
                    alignment = input("Select alignment (left, center, right): ")
                    if alignment not in ["left", "center", "right"]:
                        print(
                            "Error: Incorrect alignment. Please choose the correct option."
                        )
                    else:
                        if alignment == "left":
                            print("Left alignment:")
                            rectangle_art.align_art(alignment, console_length)
                        elif alignment == "center":
                            print("Center alignment:")
                            rectangle_art.align_art(alignment, console_length)
                        elif alignment == "right":
                            print("Right alignment:")
                            rectangle_art.align_art(alignment, console_length)
                        break
                while True:
                    manipulate_choice = input(
                        "Do you want to change your figure? (yes or no): "
                    ).lower()
                    if manipulate_choice == "yes":
                        manipulation_type = input(
                            "Enter the type of change: 1. scale: "
                        )
                        if manipulation_type == "1":
                            scale_factor = float(input("Enter the scale factor: "))
                            rectangle_art.scale_figure(scale_factor)
                            rectangle_art.draw_combined_rectangles()
                            rectangle_art.align_art(alignment, console_length)
                        else:
                            print("Error: Invalid change type.")
                    else:
                        break
                convert_2D = input("Want to turn 3D art into 2D? (yes or no): ").lower()
                if convert_2D == "yes":
                    rectangle_art.convert_to_2d()
                save_choice = input(
                    "Do you want to save the generated ASCII art to a file? (yes or no): "
                ).lower()
                if save_choice == "yes":
                    file_name = input("Enter a file name to save the ASCII art: ")
                    rectangle_art.save_file(file_name)
                continue_choice = input(
                    "Do you want to continue drawing? (yes or no): "
                ).lower()
                if continue_choice.lower() == "no":
                    print("Exit the program.")
                    break
            break
        break
