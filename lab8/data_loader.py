import os
import pandas as pd

# Отримайте абсолютний шлях до файлу
csv_file_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "data", "generated_data.csv")
)


class DataLoader:
    def __init__(self, csv_file_path=csv_file_path):
        self.data = pd.read_csv(csv_file_path)
