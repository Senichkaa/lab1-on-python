from source.core.lab5.rect import RectangleArt
from source.core.lab5.color_utils import color_selecting, colors


def main() -> None:
    console_length = 200

    while True:
        print("Options: ")
        print("1. Draw a cube")
        print("0. Exit")

        choice = input("Select an option: ")

        if choice == "0":
            print("Exit the program.")
            break
        elif choice not in ["1"]:
            print("Invalid option select. Try again")
            continue
        if choice in ["1"]:
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
                print()
                while True:
                    alignment = input(
                        "Select alignment. Available: left/center/right: "
                    )
                    if alignment not in ["left", "center", "right"]:
                        print("Invalid align. Please choose the correct option.")
                    else:
                        if alignment == "left":
                            print("Left align:")
                            rectangle_art.align_art(alignment, console_length)
                        elif alignment == "center":
                            print("Center align:")
                            rectangle_art.align_art(alignment, console_length)
                        elif alignment == "right":
                            print("Right align:")
                            rectangle_art.align_art(alignment, console_length)
                        break
                while True:
                    manipulate_choice = input(
                        "Do you want to change your figure? (yes/no): "
                    ).lower()
                    if manipulate_choice == "yes":
                        manipulation_type = input("Enter the type of change: 1.scale: ")
                        if manipulation_type == "1":
                            scale_factor = float(input("Enter the scale: "))
                            rectangle_art.scale_figure(scale_factor)
                            rectangle_art.draw_combined_rectangles()
                            rectangle_art.align_art(alignment, console_length)
                        else:
                            print("Error: Invalid type of change.")
                    else:
                        break
                convert_2D = input("Do you want to see 2D? (yes/no): ").lower()
                if convert_2D == "yes":
                    rectangle_art.convert_to_2d()
                save_choice = input(
                    "Do you want to save art to file? (yes/no): "
                ).lower()
                if save_choice == "yes":
                    file_name = input("Enter a file name to save: ")
                    rectangle_art.save_file(file_name)
                continue_choice = input("Want to continue drawing? (yes/no): ").lower()
                if continue_choice.lower() == "no":
                    print("Exit the program.")
                    break
            break
        break
