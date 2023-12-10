import unittest
import requests_mock
from unittest.mock import patch
from lab7 import ConsoleApp


class ConsoleAppTests(unittest.TestCase):
    def setUp(self):
        self.api_url = "https://jsonplaceholder.typicode.com"
        self.api_key = None
        self.app = ConsoleApp(self.api_url, self.api_key)

    def test_make_api_request_successful(self):
        response_data = {"key": "value"}
        with requests_mock.Mocker() as m:
            m.get(
                "https://jsonplaceholder.typicode.com/posts",
                json=response_data,
                status_code=200,
            )
            result = self.app.make_api_request("posts")
        self.assertEqual(result, response_data)

    def test_make_api_request_failure(self):
        with requests_mock.Mocker() as m:
            m.get("https://jsonplaceholder.typicode.com/posts", status_code=404)
            with self.assertRaises(Exception) as context:
                self.app.make_api_request("posts")
            self.assertEqual(
                str(context.exception), "API Request Failed. Status Code: 404"
            )

    def test_display_list_data(self):
        # Перевірка виведення даних списку на екран
        with patch("builtins.print") as mock_print:
            data = [["value1", "value2"], ["value3", "value4"]]
            self.app.display_list_data(data, "green", "bold")

            expected_output = (
                "╒════════╤════════╕\n"
                "│ value1 │ value2 │\n"
                "├────────┼────────┤\n"
                "│ value3 │ value4 │\n"
                "╘════════╧════════╛"
            )
            mock_print.assert_called_once_with(expected_output)

    def test_display_table_data(self):
        # Перевірка виведення даних словника на екран
        with patch("builtins.print") as mock_print:
            data = {"key1": "value1", "key2": "value2"}
            self.app.display_table_data(data, "green", "bold")

            # Очікуємо, що виклик print буде містити певні патерни (ваш вихід може трошки відрізнятися)
            expected_calls = [
                "│   key1 │   key2 │",
                "│ value1 │ value2 │",
                "╘════════╧════════╛",
            ]

            # Перевірка, чи кожен очікуваний виклик є у списку викликів print
            for expected_call in expected_calls:
                self.assertIn(
                    expected_call,
                    "".join([call[1][0] for call in mock_print.mock_calls]),
                )

    def test_save_json(self):
        data = {"key": "value"}
        with patch("builtins.open", create=True) as mock_open:
            with patch("json.dump") as mock_dump:
                self.app.save_json(data)
        mock_open.assert_called_once_with("output.json", "w")
        mock_dump.assert_called_once_with(data, mock_open().__enter__(), indent=2)

    def test_save_csv(self):
        data = [["header1", "header2"], [1, "a"], [2, "b"]]
        with patch("builtins.open", create=True) as mock_open:
            with patch("csv.writer") as mock_writer:
                self.app.save_csv(data)
        mock_open.assert_called_once_with("output.csv", "w", newline="")
        mock_writer.assert_called_once_with(mock_open().__enter__())
        mock_writer.return_value.writerows.assert_called_once_with(data)

    def test_save_txt(self):
        data = "This is a test."
        with patch("builtins.open", create=True) as mock_open:
            with patch("builtins.print") as mock_print:
                self.app.save_txt(data)
        mock_open.assert_called_once_with("output.txt", "w")
        mock_open().__enter__().write.assert_called_once_with(data)
        mock_print.assert_called_once_with("Data saved to output.txt")

    def test_parse_user_input(self):
        user_input = "get posts -c green -f json"
        expected_result = {
            "endpoint": "posts",
            "params": {},
            "format": "json",
            "headers_color": "green",
            "headers_font": "bold",
        }
        result = self.app.parse_user_input(user_input)
        self.assertEqual(result, expected_result)

    def test_handle_errors(self):
        with patch("builtins.print") as mock_print:
            self.app.handle_errors("Test error message")
        mock_print.assert_called_once_with("Error: Test error message")


if __name__ == "__main__":
    unittest.main()
