# scraper.py

from bs4 import BeautifulSoup
import logging

class Scraper:
    """
    Classe que processa o HTML e extrai links para arquivos com extensões específicas.
    Possui métodos para retornar todos os links de uma determinada extensão e
    para filtrar os links com base em uma lista de nomes fornecida.
    """
    def __init__(self, html: str):
        """
        Inicializa a classe e cria o objeto BeautifulSoup a partir do HTML.
        """
        self.html = html
        self.soup = BeautifulSoup(html, "html.parser")
    
    def extract_all_links_by_extension(self, extension: str) -> list:
        """
        Retorna todos os links que apontam para arquivos com a extensão especificada encontrados no HTML.
        
        Args:
            extension (str): Extensão do arquivo (ex: 'pdf', 'docx', etc.)
        
        Returns:
            list: Lista de URLs com a extensão especificada.
        """
        extension = extension.lower().lstrip('.')  # Remove '.' se houver
        file_links = [a['href'] for a in self.soup.find_all('a', href=True) 
                      if a['href'].lower().endswith(f'.{extension}')]
        if not file_links:
            logging.warning(f"Nenhum link com extensão .{extension} foi encontrado no HTML.")
        return file_links

    def extract_links_by_names(self, names: list, extension: str) -> list:
        """
        Retorna os links de arquivos filtrados com base em uma lista de nomes e extensão.
        
        Args:
            names (list): Lista de strings com os nomes ou parte dos nomes que devem ser filtrados.
            extension (str): Extensão do arquivo a ser buscado.
        
        Returns:
            list: Lista de URLs filtradas que contêm pelo menos uma das strings especificadas.
        """
        all_links = self.extract_all_links_by_extension(extension)
        return self.__filter_links_by_names(all_links, names)

    def __filter_links_by_names(self, links: list, names: list) -> list:
        """
        Método privado que filtra uma lista de links com base em uma lista de nomes.
        
        Args:
            links (list): Lista de URLs a serem filtradas.
            names (list): Lista de strings para comparação com os links.
        
        Returns:
            list: Lista de URLs filtradas que contêm pelo menos uma das strings especificadas.
        """
        filtered_links = []
        for link in links:
            link_lower = link.lower()
            if any(name.lower() in link_lower for name in names):
                filtered_links.append(link)
        return filtered_links
