from data_loader import DataLoader
from data_visualizations import VisualizationSelector
from data_preprocessor import DataPreprocessor
from data_explorer import DataExplorer
from base_visualization import BasicVisualizer
from advanced_visualization import AdvancedVisualizer
from subplots import MultipleSubplots
from export import Exporter


def run_lab():
    # Ініціалізуємо об'єкт DataLoader
    loader = DataLoader()

    explorer = DataExplorer(loader.data)
    explorer.explore_data()

    visual_selector = VisualizationSelector(loader.data)
    visual_selector.choose_visualizations()

    # Завдання 5: Підготовка даних
    preprocessor = DataPreprocessor(loader)
    preprocessor.preprocess()

    # Завдання 6: Базова візуалізація
    basic_visualizer = BasicVisualizer(preprocessor.processed_data)
    basic_visualizer.visualize()

    # Завдання 7: Розширені візуалізації
    advanced_visualizer = AdvancedVisualizer(preprocessor.processed_data)
    advanced_visualizer.advanced_visualizations()

    # Завдання 8: Декілька піддіаграм
    subplots_creator = MultipleSubplots(preprocessor.processed_data)
    subplots_creator.create_subplots()

    # Завдання 9: Експорт і обмін
    exporter = Exporter(preprocessor.processed_data)
    exporter.export_visualization(file_format="png")


if __name__ == "__main__":
    run_lab()
