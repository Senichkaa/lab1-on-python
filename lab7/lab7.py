import requests
import json
import csv
import os
from tabulate import tabulate


class ConsoleApp:
    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_key = api_key
        self.history = []

    def make_api_request(self, endpoint, params=None):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(
            f"{self.api_url}/{endpoint}", params=params, headers=headers
        )

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"API Request Failed. Status Code: {response.status_code}")

    def display_data(self, data, headers_color="green", headers_font="bold"):
        if isinstance(data, list):
            self.display_list_data(data, headers_color, headers_font)
        elif isinstance(data, dict):
            self.display_table_data(data, headers_color, headers_font)
        else:
            print(f"Unsupported data format: {type(data)}")

    def display_table_data(self, data, headers_color, headers_font):
        headers = [key for key in data.keys()]
        rows = [list(data.values())]  # Кожне значення у словнику буде окремим рядком

        print(
            tabulate(
                rows,
                headers=headers,
                tablefmt="fancy_grid",
                numalign=headers_color,
                stralign=headers_font,
            )
        )

    def display_list_data(self, data, headers_color, headers_font):
        print(
            tabulate(
                data,
                tablefmt="fancy_grid",
                numalign=headers_color,
                stralign=headers_font,
            )
        )

    def save_data(self, data, format):
        if format.lower() == "json":
            self.save_json(data)
        elif format.lower() == "csv":
            self.save_csv(data)
        elif format.lower() == "txt":
            self.save_txt(data)
        else:
            print(f"Unsupported format: {format}")

    def save_json(self, data):
        output_folder = "output"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        output_file_path = os.path.join(output_folder, "output.json")
        with open(output_file_path, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Data saved to {output_file_path}")

    def save_csv(self, data):
        output_folder = "output"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        output_file_path = os.path.join(output_folder, "output.csv")
        with open(output_file_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(data)
        print(f"Data saved to {output_file_path}")

    def save_txt(self, data):
        output_folder = "output"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        output_file_path = os.path.join(output_folder, "output.txt")
        with open(output_file_path, "w") as f:
            f.write(str(data))
        print(f"Data saved to {output_file_path}")

    def parse_user_input(self, user_input):
        # Простий приклад парсингу команди користувача
        # Припускаємо, що користувач вводить команду у вигляді 'get posts -c green -f json'
        parts = user_input.split()
        endpoint = parts[1]
        params = {}
        format_option = None
        headers_color = "green"
        headers_font = "bold"

        for i in range(2, len(parts), 2):
            if parts[i] == "-c":
                headers_color = parts[i + 1]
            elif parts[i] == "-f":
                format_option = parts[i + 1]

        return {
            "endpoint": endpoint,
            "params": params,
            "format": format_option,
            "headers_color": headers_color,
            "headers_font": headers_font,
        }

    def handle_errors(self, error_message):
        print(f"Error: {error_message}")

    def run(self):
        while True:
            user_input = input("Enter a command: ")

            if user_input.lower() == "exit":
                break

            try:
                parsed_input = self.parse_user_input(user_input)
                api_data = self.make_api_request(
                    parsed_input["endpoint"], parsed_input["params"]
                )
                self.display_data(
                    api_data,
                    parsed_input["headers_color"],
                    parsed_input["headers_font"],
                )
                self.save_data(api_data, parsed_input["format"])
                self.history.append({"input": user_input, "output": api_data})
            except Exception as e:
                self.handle_errors(str(e))


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com"
    api_key = None
    app = ConsoleApp(api_url, api_key)
    app.run()


# <команда> <ресурс> -c <колір> -f <формат>
# де:
# <команда> - операція, наприклад, get, create, update, delete.
# <ресурс> - ресурс API, наприклад, posts, users, comments.
# -c <колір> - параметр для вибору кольору виведення (необов'язковий).
# -f <формат> - параметр для вибору формату збереження результатів (необов'язковий). json csv txt
