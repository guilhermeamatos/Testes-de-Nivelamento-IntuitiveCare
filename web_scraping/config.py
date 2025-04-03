# config.py

# URL que será acessada para o scraping
URL_BASE = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

# Diretório onde os PDFs baixados serão armazenados
OUTPUT_DIR = "./web_scraping/downloaded_pdfs"

# Nome do arquivo zip final que conterá os PDFs baixados
ZIP_NAME = "./web_scraping/anexos.zip"

# Timeout para requisições HTTP (em segundos)
TIMEOUT = 10
