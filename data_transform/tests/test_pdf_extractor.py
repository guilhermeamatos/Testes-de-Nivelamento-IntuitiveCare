import unittest
from unittest.mock import MagicMock, patch
import os
import pandas as pd
import tempfile
from pdf_extractor import PDFExtractor

class TestPDFExtractor(unittest.TestCase):
    @patch("pdf_extractor.pdfplumber.open")
    def test_extract_table_no_tables(self, mock_pdfplumber):
        # Simula um PDF sem tabelas
        mock_pdf = MagicMock()
        mock_pdf.pages = []
        mock_pdfplumber.return_value.__enter__.return_value = mock_pdf
        
        extractor = PDFExtractor(skip_header_in_subsequent_pages=True)
        table_data = extractor.extract_table("fake_path.pdf")
        self.assertEqual(table_data, [], "Esperava uma lista vazia quando não há páginas ou tabelas.")

    @patch("pdf_extractor.pdfplumber.open")
    def test_extract_table_with_header_skip_subsequent(self, mock_pdfplumber):
        # Simula um PDF com 2 páginas, cada uma contendo uma tabela
        # Primeira página: Table -> [["Header1", "Header2"], ["val1", "val2"]]
        # Segunda página: Table -> [["Header1", "Header2"], ["val3", "val4"]]
        # skip_header_in_subsequent_pages=True -> ignora "Header1,Header2" da segunda página
        page1 = MagicMock()
        page1.extract_table.return_value = [
            ["Header1", "Header2"],
            ["val1", "val2"]
        ]
        page2 = MagicMock()
        page2.extract_table.return_value = [
            ["Header1", "Header2"],
            ["val3", "val4"]
        ]
        mock_pdf = MagicMock()
        mock_pdf.pages = [page1, page2]
        mock_pdfplumber.return_value.__enter__.return_value = mock_pdf
        
        extractor = PDFExtractor(skip_header_in_subsequent_pages=True)
        table_data = extractor.extract_table("fake_path.pdf")

        # Espera-se que a 1ª página tenha todo o conteúdo,
        # mas na 2ª página a primeira linha (cabeçalho repetido) seja ignorada
        expected = [
            ["Header1", "Header2"],
            ["val1", "val2"],
            ["val3", "val4"]  # sem o header repetido
        ]
        self.assertEqual(table_data, expected)

    @patch("pdf_extractor.pdfplumber.open")
    def test_extract_table_with_header_not_skipping(self, mock_pdfplumber):
        # Mesmo cenário, mas skip_header_in_subsequent_pages=False
        page1 = MagicMock()
        page1.extract_table.return_value = [
            ["H1", "H2"],
            ["val1", "val2"]
        ]
        page2 = MagicMock()
        page2.extract_table.return_value = [
            ["H1", "H2"],
            ["val3", "val4"]
        ]
        mock_pdf = MagicMock()
        mock_pdf.pages = [page1, page2]
        mock_pdfplumber.return_value.__enter__.return_value = mock_pdf
        
        extractor = PDFExtractor(skip_header_in_subsequent_pages=False)
        table_data = extractor.extract_table("fake_path.pdf")
        # Agora não removemos o cabeçalho na segunda página
        expected = [
            ["H1", "H2"],
            ["val1", "val2"],
            ["H1", "H2"],
            ["val3", "val4"]
        ]
        self.assertEqual(table_data, expected)

    def test_save_table_to_csv(self):
        extractor = PDFExtractor()
        # Tabela simulada
        table_data = [
            ["Col1", "Col2"],
            ["Data1", "Data2"],
            ["Data3", "Data4"]
        ]
        
        with tempfile.TemporaryDirectory() as tmpdir:
            csv_path = os.path.join(tmpdir, "test.csv")
            df = extractor.save_table_to_csv(table_data, csv_path)
            self.assertTrue(os.path.exists(csv_path))
            self.assertEqual(list(df.columns), ["Col1", "Col2"])
            self.assertEqual(len(df), 2)

    def test_save_table_to_csv_empty(self):
        extractor = PDFExtractor()
        with self.assertRaises(ValueError) as context:
            extractor.save_table_to_csv([], "path.csv")
        self.assertIn("Nenhuma linha de tabela", str(context.exception))

if __name__ == '__main__':
    unittest.main()
