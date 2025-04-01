import unittest
import os
import tempfile
import pandas as pd
from csv_transformer import CSVTransformer
import zipfile

class TestCSVTransformer(unittest.TestCase):
    def setUp(self):
        # Cria um CSV temporário para ser carregado nos testes
        self.temp_dir = tempfile.TemporaryDirectory()
        self.csv_path = os.path.join(self.temp_dir.name, "test_data.csv")
        df = pd.DataFrame({
            "Col1": ["val1", "val2"],
            "Col2": ["AMB", "OD"]
        })
        df.to_csv(self.csv_path, index=False)

    def tearDown(self):
        # apaga o diretório temporário
        self.temp_dir.cleanup()

    def test_load_csv(self):
        transformer = CSVTransformer(self.csv_path)
        df = transformer.load_csv()
        self.assertListEqual(list(df.columns), ["Col1", "Col2"])
        self.assertEqual(len(df), 2)

    def test_apply_replacements_success(self):
        transformer = CSVTransformer(self.csv_path)
        transformer.load_csv()
        transformer.apply_replacements("Col2", {"AMB": "Seg. Ambulatorial", "OD": "Seg. Odontológica"})

        self.assertIn("Seg. Ambulatorial", transformer.df["Col2"].values)
        self.assertIn("Seg. Odontológica", transformer.df["Col2"].values)

    def test_apply_replacements_no_column(self):
        transformer = CSVTransformer(self.csv_path)
        transformer.load_csv()
        with self.assertRaises(ValueError) as context:
            transformer.apply_replacements("InvalidCol", {"AMB": "Algo"})
        self.assertIn("Coluna 'InvalidCol' não encontrada", str(context.exception))

    def test_save_csv(self):
        transformer = CSVTransformer(self.csv_path)
        transformer.load_csv()
        
        transformer.apply_replacements("Col2", {"AMB": "Amb"})
        new_csv_path = os.path.join(self.temp_dir.name, "saved_data.csv")
        transformer.save_csv(new_csv_path)
        self.assertTrue(os.path.exists(new_csv_path))

        df_loaded = pd.read_csv(new_csv_path)
        self.assertIn("Amb", df_loaded["Col2"].values)

    def test_compress_csv(self):
        transformer = CSVTransformer(self.csv_path)
        zip_path = os.path.join(self.temp_dir.name, "test_zip.zip")
        transformer.compress_csv(zip_path)
        self.assertTrue(os.path.exists(zip_path))
        
        with zipfile.ZipFile(zip_path, 'r') as zf:
            self.assertIn("test_data.csv", zf.namelist())

if __name__ == '__main__':
    unittest.main()
