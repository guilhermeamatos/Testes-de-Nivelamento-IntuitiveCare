import pandas as pd
import zipfile
import os

class CSVTransformer:
    """
    Classe para transformação genérica de arquivos CSV.
    
    Funcionalidades:
      - Carregar um CSV em um DataFrame.
      - Aplicar substituições em uma coluna específica.
      - Salvar o DataFrame atualizado em um arquivo CSV.
      - Compactar o CSV em um arquivo ZIP.
    """
    def __init__(self, csv_path: str):
        """
        Inicializa a instância com o caminho do CSV.
        
        Args:
            csv_path (str): Caminho para o arquivo CSV.
        """
        self.csv_path = csv_path
        self.df = None

    def load_csv(self) -> pd.DataFrame:
        """
        Carrega o CSV no DataFrame.
        
        Returns:
            pd.DataFrame: DataFrame com os dados carregados.
        """
        self.df = pd.read_csv(self.csv_path)
        return self.df

    def apply_replacements(self, column: str, replacements: dict) -> pd.DataFrame:
        """
        Aplica substituições nos valores de uma coluna usando um mapeamento.
        
        Args:
            column (str): Nome da coluna a ser transformada.
            replacements (dict): Mapeamento no formato {valor_original: novo_valor}.
        
        Returns:
            pd.DataFrame: DataFrame com as substituições aplicadas.
        
        Raises:
            ValueError: Se a coluna não for encontrada no DataFrame.
        """
        if self.df is None:
            self.load_csv()
        if column not in self.df.columns:
            raise ValueError(f"Coluna '{column}' não encontrada no CSV.")
        self.df[column] = self.df[column].replace(replacements)
        return self.df

    def save_csv(self, output_path: str = None) -> str:
        """
        Salva o DataFrame atual em um arquivo CSV.
        
        Args:
            output_path (str, opcional): Caminho para salvar o CSV. Se None, sobrescreve o arquivo original.
        
        Returns:
            str: Caminho onde o CSV foi salvo.
        
        Raises:
            ValueError: Se o DataFrame ainda não foi carregado ou está vazio.
        """
        if self.df is None:
            raise ValueError("DataFrame vazio. Carregue ou transforme o CSV antes de salvar.")
        if output_path is None:
            output_path = self.csv_path
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        self.df.to_csv(output_path, index=False)
        return output_path

    def compress_csv(self, zip_name: str, csv_to_compress: str = None) -> str:
        """
        Compacta o arquivo CSV em um ZIP.
        
        Args:
            zip_name (str): Nome do arquivo ZIP de saída.
            csv_to_compress (str, opcional): Caminho do CSV a ser compactado. Se None, utiliza self.csv_path.
        
        Returns:
            str: Nome do arquivo ZIP criado.
        """
        if csv_to_compress is None:
            csv_to_compress = self.csv_path
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zf:
            zf.write(csv_to_compress, os.path.basename(csv_to_compress))
        return zip_name
