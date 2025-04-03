import os
import sys
import logging
import zipfile
import shutil
from urllib.parse import urljoin

def configurar_sys_path():
    projeto_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    if projeto_raiz not in sys.path:
        sys.path.insert(0, projeto_raiz)

configurar_sys_path()

from web_scraping.web_client import WebClient
from web_scraping.scraper import Scraper
from web_scraping.utils import download_file

def extrair_csv_do_zip(caminho_zip, diretorio_saida):
    """Extrai os arquivos CSV de um ZIP para o diretório de saída."""
    try:
        with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
            for info in zip_ref.infolist():
                if info.filename.lower().endswith('.csv'):
                    zip_ref.extract(info, diretorio_saida)
                    logging.info("Extraído CSV: %s", info.filename)
    except zipfile.BadZipFile:
        logging.error("Arquivo ZIP inválido: %s", caminho_zip)

def processar_ano(url, ano, dir_download, dir_extraido, cliente):
    """Faz o download e extrai os ZIPs de um ano específico."""
    logging.info("Processando ano: %s", ano)
    html = cliente.fetch_html(url)
    if not html:
        logging.error("Falha ao obter HTML de: %s", url)
        return

    scraper = Scraper(html)
    links_zip = scraper.extract_all_links_by_extension("zip")
    logging.info("Links ZIP encontrados para %s: %s", ano, links_zip)

    os.makedirs(dir_download, exist_ok=True)
    os.makedirs(dir_extraido, exist_ok=True)

    for link in links_zip:
        url_completa = link if link.startswith("http") else urljoin(url, link)
        nome_zip = os.path.basename(url_completa)
        caminho_download = os.path.join(dir_download, nome_zip)
        if download_file(url_completa, caminho_download):
            logging.info("Download concluído: %s", nome_zip)
            extrair_csv_do_zip(caminho_download, dir_extraido)
        else:
            logging.error("Falha no download: %s", url_completa)

def baixar_csv_operadoras(dir_extraido):
    """Faz o download do CSV de operadoras e o salva no diretório de saída."""
    url_csv = "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/Relatorio_cadop.csv"
    caminho_csv = os.path.join(dir_extraido, "Relatorio_cadop.csv")
    if download_file(url_csv, caminho_csv):
        logging.info("Download do CSV de operadoras concluído: %s", caminho_csv)
    else:
        logging.error("Falha no download do CSV de operadoras a partir de: %s", url_csv)

def limpar_diretorio_download(dir_download):
    """Remove o diretório de downloads."""
    if os.path.exists(dir_download):
        shutil.rmtree(dir_download)
        logging.info("Diretório removido: %s", dir_download)

def main():
    logging.basicConfig(level=logging.INFO)

    url_2023 = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2023/"
    url_2024 = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2024/"
    timeout = 30
    cliente = WebClient(timeout=timeout)

    dir_download = os.path.abspath(os.path.join(os.path.dirname(__file__), "downloaded_zips"))
    dir_extraido = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))

    processar_ano(url_2023, 2023, dir_download, dir_extraido, cliente)
    processar_ano(url_2024, 2024, dir_download, dir_extraido, cliente)
    baixar_csv_operadoras(dir_extraido)
    limpar_diretorio_download(dir_download)

    logging.info("Processamento concluído.")

if __name__ == '__main__':
    main()
