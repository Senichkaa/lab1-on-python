import os
from source.core.lab8.data_loader import DataLoader
from source.core.lab8.data_preprocessor import DataPreprocessor
import matplotlib.pyplot as plt


class BasicVisualizer:
    def __init__(self, data):
        self.data = data

    def visualize(self):
        plt.plot(self.data["age"], self.data["job"], "o")
        plt.xlabel("Age")
        plt.ylabel("Job")
        plt.title("Basic Visualization")

