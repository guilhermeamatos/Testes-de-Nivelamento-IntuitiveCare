import pdfplumber
import pandas as pd
import os

class PDFExtractor:
    """
    Extrai tabelas de um PDF e as salva em CSV.
    """
    def __init__(self, skip_header_in_subsequent_pages=True):
        self.skip_header_in_subsequent_pages = skip_header_in_subsequent_pages

    def extract_table(self, pdf_path: str) -> list:
        """
        Extrai as linhas de tabela do PDF.
        Retorna uma lista de listas, onde a primeira sub-lista é o cabeçalho.
        """
        all_rows = []
        with pdfplumber.open(pdf_path) as pdf:
            first_page = True
            for page in pdf.pages:
                table = page.extract_table()
                if table:
                    processed = self._process_table(table, first_page)
                    all_rows.extend(processed)
                    first_page = False
        return all_rows

    def _process_table(self, table: list, is_first_page: bool) -> list:
        """
        Processa os dados de uma página. Se não for a primeira página e
        skip_header_in_subsequent_pages for True, ignora a primeira linha.
        """
        return table if is_first_page else (table[1:] if self.skip_header_in_subsequent_pages else table)

    def save_table_to_csv(self, table_data: list, csv_path: str) -> pd.DataFrame:
        """
        Converte a lista de listas em um DataFrame e salva em CSV.
        """
        if not table_data:
            raise ValueError("Nenhuma linha de tabela foi fornecida para salvar.")
        header, rows = table_data[0], table_data[1:]
        df = pd.DataFrame(rows, columns=header)
        os.makedirs(os.path.dirname(csv_path), exist_ok=True)
        df.to_csv(csv_path, index=False)
        return df
