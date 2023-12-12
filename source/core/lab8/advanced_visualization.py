import seaborn as sns
import matplotlib.pyplot as plt
from source.core.lab8.data_loader import DataLoader
from source.core.lab8.data_preprocessor import DataPreprocessor
import os



class AdvancedVisualizer:
    def __init__(self, data):
        self.data = data

    def advanced_visualizations(self):
        numeric_data = self.data.select_dtypes(include="number")

        plt.figure(figsize=(12, 8))
        sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
        plt.title("Correlation Heatmap")

