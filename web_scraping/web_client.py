# web_client.py

import requests
import logging

class WebClient:
    """
    Classe para acessar URLs e retornar seu conteúdo HTML.
    
    Essa classe pode ser reutilizada para qualquer projeto que precise
    fazer requisições HTTP e obter o conteúdo de páginas.
    """
    def __init__(self, timeout: int, headers: dict = None):
        self.timeout = timeout
        self.headers = headers or {"User-Agent": "Mozilla/5.0"}

    def fetch_html(self, url: str) -> str:
        """
        Realiza uma requisição GET na URL e retorna o HTML.
        
        Args:
            url (str): URL da página a ser acessada.
        
        Returns:
            str: Conteúdo HTML ou uma string vazia em caso de erro.
        """
        try:
            response = requests.get(url, timeout=self.timeout, headers=self.headers)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            logging.error(f"Erro ao acessar {url}: {e}")
            return ""
