import pandas as pd
import os


input_dir = 'C:/Users/guilh/Desktop/Testes-de-Nivelamento-IntuitiveCare/database/data/'

files_to_process = [
    '1T2023.csv', '1T2024.csv', '2t2023.csv', '2T2024.csv',
    '3T2023.csv', '3T2024.csv', '4T2023.csv', '4T2024.csv'
]

def convert_to_string(df):
    return df.applymap(str).applymap(lambda x: x.strip())

def replace_comma_with_dot(df, columns):
    for col in columns:
        df[col] = df[col].str.replace(',', '.')
    return df
def process_csv(file_path, columns_to_replace_comma):
    df = pd.read_csv(file_path, delimiter=';', encoding='utf-8', dtype=str)
    df = convert_to_string(df)
    df = replace_comma_with_dot(df, columns_to_replace_comma)
    df['REG_ANS'] = df['REG_ANS'].str.strip()  # Garantir que REG_ANS não perca zeros à esquerda
    return df

# Função para filtrar os registros válidos com base no Registro_ANS da operadora
def filter_valid_records(df, registro_ans_set):
    return df[df['REG_ANS'].isin(registro_ans_set)]


def process_selected_files(input_dir, operadora_file, files_to_process, columns_to_replace_comma):
    df_operadora = pd.read_csv(operadora_file, delimiter=';', encoding='utf-8', dtype=str)
    df_operadora['Registro_ANS'] = df_operadora['Registro_ANS'].str.strip()
    registro_ans_set = set(df_operadora['Registro_ANS'])
    print(f"Total de registros únicos em Registro_ANS: {len(registro_ans_set)}")

    for file in files_to_process:
        file_path = os.path.join(input_dir, file)

        if os.path.exists(file_path):
            print(f"Processando o arquivo: {file}")

            df = process_csv(file_path, columns_to_replace_comma)
            df_valid = filter_valid_records(df, registro_ans_set)

            if not df_valid.empty:
                output_file = os.path.join(input_dir, file.replace('.csv', '_validos.csv'))
                df_valid.to_csv(output_file, index=False, sep=';', encoding='utf-8')
                print(f"Arquivo corrigido com registros válidos salvo em: {output_file}")
            else:
                print(f"Arquivo {file} não contém registros válidos.")
        else:
            print(f"O arquivo {file} não foi encontrado no diretório.")

columns_to_replace_comma = ['VL_SALDO_INICIAL', 'VL_SALDO_FINAL']

operadora_file = os.path.join(input_dir, 'operadora.csv')

process_selected_files(input_dir, operadora_file, files_to_process, columns_to_replace_comma)
