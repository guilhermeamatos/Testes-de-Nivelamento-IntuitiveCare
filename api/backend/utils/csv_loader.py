# server/utils/csv_loader.py
import pandas as pd
import os

def load_csv_data():
    base_path = os.path.abspath(os.path.dirname(__file__))
    csv_path = os.path.join(base_path, '../../../database/data/Relatorio_cadop.csv')
    print("Caminho do CSV:", csv_path)
    
    try:
        data = pd.read_csv(csv_path, sep=';', engine='python', dtype=str)
        data = data.fillna('')
        print("CSV carregado com sucesso. Total de registros:", len(data))
        return data
    except Exception as e:
        print(f"Erro ao carregar o CSV: {e}")
        return pd.DataFrame()  

if __name__ == "__main__":
    df = load_csv_data()
    print(df.head())
