from color_pick import ProcessColor
from file_processes import FileProcess


class AsciiArtSets:
    """
    The AsciiArtSets class facilitates user interaction for creating and customizing ASCII art.

    Methods:
    - select_width(): Get the width for the ASCII art from the user.
    - select_align(alignment: str): Get the alignment for the ASCII art from the user.
    - select_color(): Get the color choice for the ASCII art from the user.
    - select_symbol(prompt: str = "Choose a symbol: "): Get the symbol for the ASCII art from the user.
    - save_file(result: str): Ask the user if they want to save the ASCII art to a file.

    Example Usage:
    >>> ascii_art_settings = AsciiArtSets()
    >>> width = ascii_art_settings.select_width()
    >>> alignment_function = ascii_art_settings.select_align("center")
    >>> color_choice = ascii_art_settings.select_color()
    >>> symbol = ascii_art_settings.select_symbol()
    >>> ascii_art_settings.save_file("ASCII ART CONTENT")
    """

    @staticmethod
    def select_width():
        """
        Get the width for the ASCII art from the user.

        Returns:
        - int: The width for the ASCII art.
        """
        return int(input("Enter the width of the ASCII art: "))

    @staticmethod
    def select_align(alignment):
        """
        Get the alignment for the ASCII art from the user.

        Parameters:
        - alignment (str): The alignment option ("left", "center", or "right").

        Returns:
        - function: The selected alignment function.
        """
        while True:
            try:
                chosen_alignment = (
                    str.center
                    if alignment == "center"
                    else str.rjust
                    if alignment == "right"
                    else lambda x, width: x
                )
                if chosen_alignment not in ["left", "center", "right"]:
                    raise ValueError("Error! Invalid alignment.")
                return chosen_alignment
            except ValueError:
                print("Invalid input. Please enter a valid alignment.")

    @staticmethod
    def select_color():
        """
        Get the color choice for the ASCII art from the user.

        Returns:
        - str: The selected color choice.
        """
        colors = ProcessColor().get_colorway()
        print("Available colors:")
        ProcessColor().show_colorway()
        while True:
            try:
                color_choice = input("Select a color by entering its ordinal number: ")
                if color_choice not in colors:
                    raise ValueError("Invalid color choice")
                return color_choice
            except ValueError:
                print("Incorrect color choice")

    @staticmethod
    def select_symbol(prompt="Choose a symbol: "):
        """
        Get the symbol for the ASCII art from the user.

        Parameters:
        - prompt (str): The prompt to display for symbol input.

        Returns:
        - str: The selected symbol.
        """
        return input(prompt)

    @staticmethod
    def save_file(result):
        """
        Ask the user if they want to save the ASCII art to a file.

        Parameters:
        - result (str): The ASCII art to save.

        Returns:
        - None
        """
        option = input("Save the art? yes/no: ")
        if option.lower() == "yes":
            filename = input("Enter the file name: ")
            file_processor = FileProcess(filename)
            file_processor.save_to_file(result)
