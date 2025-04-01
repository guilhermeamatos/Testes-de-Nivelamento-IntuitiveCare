import os
import logging
from pdf_extractor import PDFExtractor
from csv_transformer import CSVTransformer

def extract_csv(pdf_path: str, csv_path: str) -> None:
    """
    Extrai os dados do PDF e salva em um arquivo CSV.
    
    Args:
        pdf_path (str): Caminho do arquivo PDF.
        csv_path (str): Caminho onde o CSV será salvo.
    """
    extractor = PDFExtractor(skip_header_in_subsequent_pages=True)
    table_data = extractor.extract_table(pdf_path)
    extractor.save_table_to_csv(table_data, csv_path)
    logging.info(f"CSV extraído e salvo em: {csv_path}")

def transform_and_compress_csv(csv_path: str, zip_path: str) -> None:
    """
    Carrega, transforma e compacta o CSV.
    
    Realiza substituições nos valores das colunas 'OD' e 'AMB'.
    
    Args:
        csv_path (str): Caminho do CSV a ser transformado.
        zip_path (str): Caminho do arquivo ZIP de saída.
    """
    transformer = CSVTransformer(csv_path)
    transformer.load_csv()
    logging.info(f"Colunas carregadas: {list(transformer.df.columns)}")
    
    if "OD" in transformer.df.columns:
        transformer.apply_replacements("OD", {"OD": "Seg. Odontológica"})
        logging.info("Substituição aplicada na coluna 'OD'")
    else:
        logging.warning("Coluna 'OD' não encontrada.")
    
    if "AMB" in transformer.df.columns:
        transformer.apply_replacements("AMB", {"AMB": "Seg. Ambulatorial"})
        logging.info("Substituição aplicada na coluna 'AMB'")
    else:
        logging.warning("Coluna 'AMB' não encontrada.")
    
    transformer.save_csv()
    transformer.compress_csv(zip_path)
    logging.info(f"CSV transformado e compactado em: {zip_path}")

def main() -> None:
    logging.basicConfig(level=logging.INFO)
    
    base_dir = os.path.dirname(__file__)
    pdf_path = os.path.join(base_dir, "..", "web_scraping", "downloaded_pdfs", "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf")
    csv_path = os.path.join(base_dir, "data", "output", "rol_procedimentos.csv")
    zip_path = os.path.join(base_dir, "Teste_Guilherme.zip")
    
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    
    try:
        extract_csv(pdf_path, csv_path)
    except Exception as e:
        logging.error(f"Erro na extração do PDF: {e}")
        return
    
    try:
        transform_and_compress_csv(csv_path, zip_path)
    except Exception as e:
        logging.error(f"Erro na transformação do CSV: {e}")

if __name__ == "__main__":
    main()
