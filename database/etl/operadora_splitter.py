import os
import pandas as pd

def load_csv_file(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path, delimiter=';', encoding='utf-8', dtype=str)

def remove_extra_spaces(df: pd.DataFrame) -> pd.DataFrame:
    return df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

def check_missing_columns(df: pd.DataFrame, required_columns: list) -> list:
    return [col for col in required_columns if col not in df.columns]

def filter_columns(df: pd.DataFrame, required_columns: list) -> pd.DataFrame:
    missing = check_missing_columns(df, required_columns)
    if missing:
        print(f"Faltando as colunas: {missing}")
        return pd.DataFrame()
    return df[required_columns]

def clean_phone_columns(df: pd.DataFrame) -> pd.DataFrame:
    if 'DDD' in df.columns:
        df['DDD'] = df['DDD'].astype(str).str.split('.').str[0]
    if 'Telefone' in df.columns:
        df['Telefone'] = df['Telefone'].astype(str).str.split('.').str[0]
    return df

def save_dataframe(df: pd.DataFrame, file_path: str):
    df.to_csv(file_path, index=False, sep=';', encoding='utf-8')
    print(f"Arquivo salvo em: {file_path}")

def main():
    base_dir = os.path.join("..", "data")
    input_file = os.path.join(base_dir, "Relatorio_cadop.csv")
    operadora_file = os.path.join(base_dir, "operadora.csv")
    endereco_file = os.path.join(base_dir, "endereco.csv")
    contato_file = os.path.join(base_dir, "contato.csv")
    
    df = load_csv_file(input_file)
    df = remove_extra_spaces(df)
    
    required_columns_operadora = ['Registro_ANS', 'CNPJ', 'Razao_Social', 'Nome_Fantasia', 
                                  'Modalidade', 'Representante', 'Data_Registro_ANS']
    required_columns_endereco = ['Logradouro', 'Numero', 'Complemento', 'Bairro', 'Cidade', 'UF', 'CEP']
    required_columns_contato = ['DDD', 'Telefone', 'Fax', 'Endereco_eletronico', 'Registro_ANS']
    
    missing_operadora = check_missing_columns(df, required_columns_operadora)
    missing_endereco = check_missing_columns(df, required_columns_endereco)
    missing_contato = check_missing_columns(df, required_columns_contato)
    
    if missing_operadora:
        print(f"Faltando as colunas no CSV para 'operadora': {missing_operadora}")
    if missing_endereco:
        print(f"Faltando as colunas no CSV para 'endereco': {missing_endereco}")
    if missing_contato:
        print(f"Faltando as colunas no CSV para 'contato': {missing_contato}")
    
    df_operadora = filter_columns(df, required_columns_operadora)
    df_endereco = filter_columns(df, required_columns_endereco)
    df_contato = filter_columns(df, required_columns_contato)
    
    if not df_endereco.empty:
        df_endereco['Registro_ANS'] = df['Registro_ANS']
        save_dataframe(df_endereco, endereco_file)
    
    if not df_contato.empty:
        df_contato['Registro_ANS'] = df['Registro_ANS']
        df_contato = clean_phone_columns(df_contato)
        save_dataframe(df_contato, contato_file)
    
    if not df_operadora.empty:
        save_dataframe(df_operadora, operadora_file)
    
    if df_operadora.empty and df_endereco.empty and df_contato.empty:
        print("Não foi possível salvar os arquivos devido à falta de colunas essenciais no CSV.")

if __name__ == "__main__":
    main()
