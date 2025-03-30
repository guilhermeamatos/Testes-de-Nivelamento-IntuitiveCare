# scraper.py

from bs4 import BeautifulSoup
import logging

class Scraper:
    """
    Classe que processa o HTML e extrai links para arquivos PDF.
    Possui métodos para retornar todos os links e para filtrar os links
    com base em uma lista de nomes fornecida.
    """
    def __init__(self, html: str):
        """
        Inicializa a classe e cria o objeto BeautifulSoup a partir do HTML.
        """
        self.html = html
        self.soup = BeautifulSoup(html, "html.parser")
    
    def extract_all_pdf_links(self) -> list:
        """
        Retorna todos os links que apontam para arquivos PDF encontrados no HTML.
        
        Returns:
            list: Lista de URLs com extensão .pdf.
        """
        pdf_links = [a['href'] for a in self.soup.find_all('a', href=True) 
                     if a['href'].lower().endswith('.pdf')]
        if not pdf_links:
            logging.warning("Nenhum link de PDF foi encontrado no HTML.")
        return pdf_links

    def extract_pdf_links_by_names(self, names: list) -> list:
        """
        Retorna os links de arquivos PDF filtrados com base em uma lista de nomes.
        
        Args:
            names (list): Lista de strings com os nomes ou parte dos nomes que devem ser filtrados.
        
        Returns:
            list: Lista de URLs filtradas que contêm pelo menos uma das strings especificadas.
        """
        all_links = self.extract_all_pdf_links()
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
            # Se algum dos nomes fornecidos estiver presente no link, adiciona à lista filtrada.
            if any(name.lower() in link_lower for name in names):
                filtered_links.append(link)
        return filtered_links