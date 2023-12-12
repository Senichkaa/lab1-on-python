import colorama
from colorama import Fore


class ProcessColor:
    """
    The ProcessColor class manages color-related functionality using the colorama module.

    Attributes:
    - colors (dict): A dictionary containing color numbers and their corresponding names.

    Methods:
    - __init__(): Initializes a new ProcessColor instance.
    - show_colorway(): Displays the available color options.
    - get_colorway(): Retrieves the available color options as a dictionary.

    Example Usage:
    >>> color_processor = ProcessColor()
    >>> color_processor.show_colorway()
    >>> available_colors = color_processor.get_colorway()
    """

    def __init__(self):
        """
        Initializes a new ProcessColor instance.

        This initializes the colorama module and creates a dictionary of color names.

        Returns:
        - None
        """
        colorama.init(autoreset=True)
        self.colors = dict(enumerate(sorted(Fore.__dict__.keys())))

    def show_colorway(self):
        """
        Displays the available color options.

        Prints the list of color options along with their corresponding numbers.

        Returns:
        - None
        """
        for color in self.colors:
            print(str(color) + ". " + self.colors[color])

    def get_colorway(self):
        """
        Retrieves the available color options as a dictionary.

        Returns:
        - dict: A dictionary containing color numbers and their corresponding names.
        """
        return self.colors
