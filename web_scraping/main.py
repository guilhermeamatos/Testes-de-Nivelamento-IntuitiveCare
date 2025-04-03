import os
import logging
from config import URL_BASE, OUTPUT_DIR, ZIP_NAME, TIMEOUT
from web_client import WebClient
from scraper import Scraper
from utils import download_file, create_zip

def main():
    logging.basicConfig(level=logging.INFO)

    EXTENSAO_ARQUIVO = "pdf" 
    FILTROS_NOME = ["anexo_i", "anexo_ii"]  

    client = WebClient(timeout=TIMEOUT)
    html_content = client.fetch_html(URL_BASE)
    if not html_content:
        logging.error("Erro ao obter o conteúdo HTML.")
        return

    scraper = Scraper(html_content)
    all_links = scraper.extract_all_links_by_extension(EXTENSAO_ARQUIVO)
    logging.info("Links .%s encontrados: %s", EXTENSAO_ARQUIVO, all_links)

    target_links = scraper.extract_links_by_names(FILTROS_NOME, EXTENSAO_ARQUIVO)
    logging.info("Links filtrados: %s", target_links)

    if not target_links:
        logging.error("Nenhum link correspondente aos filtros foi encontrado.")
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    downloaded_files = []
    for link in target_links:
        filename = os.path.join(OUTPUT_DIR, os.path.basename(link))
        if download_file(link, filename):
            downloaded_files.append(filename)
        else:
            logging.warning("Falha ao baixar: %s", link)

    if downloaded_files:
        create_zip(downloaded_files, ZIP_NAME)
        logging.info("Arquivos compactados em: %s", ZIP_NAME)
    else:
        logging.warning("Nenhum arquivo baixado.")

if __name__ == '__main__':
    main()
