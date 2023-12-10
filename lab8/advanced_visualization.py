import seaborn as sns
import matplotlib.pyplot as plt
from data_loader import DataLoader
from data_preprocessor import DataPreprocessor
import os

csv_file_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "data", "generated_data.csv")
)

loader = DataLoader(csv_file_path=csv_file_path)
data = loader.data

preprocessor = DataPreprocessor(loader)
preprocessor.preprocess()


class AdvancedVisualizer:
    def __init__(self, data):
        self.data = data

    def advanced_visualizations(self):
        numeric_data = self.data.select_dtypes(include="number")

        plt.figure(figsize=(12, 8))
        sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
        plt.title("Correlation Heatmap")
        plt.show()


advanced_visualizer = AdvancedVisualizer(data)
advanced_visualizer.advanced_visualizations()
