# utils.py

import os
import zipfile
import requests
import logging

def download_file(url: str, dest: str) -> bool:
    """
    Faz o download de um arquivo da URL e o salva no destino especificado.
    
    Args:
        url (str): URL do arquivo.
        dest (str): Caminho local para salvar o arquivo.
    
    Returns:
        bool: True se o download foi bem-sucedido, False caso contrário.
    """
    try:
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()
        with open(dest, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return True
    except requests.RequestException as e:
        logging.error(f"Erro ao baixar {url}: {e}")
        return False

def create_zip(files: list, output_zip: str) -> None:
    """
    Compacta uma lista de arquivos em um arquivo zip.
    
    Args:
        files (list): Lista de caminhos de arquivos a serem compactados.
        output_zip (str): Nome do arquivo zip de saída.
    """
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in files:
            if os.path.exists(file):
                zipf.write(file, os.path.basename(file))
