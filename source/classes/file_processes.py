import pandas as pd
import os
import json


class FileProcess:
    """
    The FileProcess class handles file input/output operations, specifically for text and ASCII art data.

    Attributes:
    - save_file_path (str): The absolute path to the output file.
    - file_path (str): The relative path or filename for file operations.

    Methods:
    - __init__(output_path: str): Initializes a new FileProcess instance.
    - save_to_file(data: str): Saves a string of data to a text file.
    - save_art_to_file(data: list): Saves a list of strings (ASCII art) to a text file.
    - read_from_file(): Reads data from a text file and returns it as a dictionary.

    Example Usage:
    >>> processor = FileProcess("output.txt")
    >>> processor.save_to_file("Hello, World!")
    >>> data = processor.read_from_file()
    """

    def __init__(self, output_path):
        """
        Initializes a new FileProcess instance.

        Parameters:
        - output_path (str): The path to the output file.

        Returns:
        - None
        """
        self.save_file_path = os.path.join(os.getcwd(), "output", output_path)
        self.file_path = output_path

    def save_to_file(self, data):
        """
        Saves a string of data to a text file.

        Parameters:
        - data (str): The data to be saved.

        Returns:
        - None
        """
        try:
            with open(self.save_file_path, "w") as file:
                file.write(data)
                print(f"Data saved to the file: {self.save_file_path}")
        except:
            print(f"Data not saved to {self.save_file_path}")

    def save_art_to_file(self, data):
        """
        Saves a list of strings (ASCII art) to a text file.

        Parameters:
        - data (list): List of strings representing ASCII art.

        Returns:
        - None
        """
        try:
            with open(self.save_file_path, "w") as file:
                for line in data:
                    file.write(line + "\n")
            print(f"Art saved to the file: {self.save_file_path}")
        except:
            print(f"Art not saved to {self.save_file_path}")

    def read_from_file(self):
        """
        Reads data from a text file and returns it as a dictionary.

        Returns:
        - dict: A dictionary containing data read from the file.
        """
        try:
            with open(self.file_path, "r") as file:
                data = {}
                for line in file:
                    key, value = line.strip().split(": ")
                    data[key] = value
            print(f"Data loaded from the file: {self.file_path}")
            return data
        except FileNotFoundError:
            print(f"File with the name {self.file_path} not found")
            return {}
        except:
            print(f"Error reading the file: {self.file_path}")
            return {}
