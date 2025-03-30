import unittest
import requests
from unittest.mock import patch, MagicMock
from web_client import WebClient

class TestWebClient(unittest.TestCase):
    @patch('web_client.requests.get')
    def test_fetch_html_success(self, mock_get):
        # Simula uma resposta bem-sucedida
        mock_response = MagicMock()
        mock_response.text = "<html>Test</html>"
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        client = WebClient(timeout=5)
        html = client.fetch_html("https://example.com")
        self.assertEqual(html, "<html>Test</html>")

    @patch('web_client.requests.get')
    def test_fetch_html_failure(self, mock_get):
        # Simula uma exceção ao fazer a requisição
        mock_get.side_effect = requests.RequestException("Error")
        client = WebClient(timeout=5)
        html = client.fetch_html("https://example.com")
        self.assertEqual(html, "")

if __name__ == '__main__':
    unittest.main()
