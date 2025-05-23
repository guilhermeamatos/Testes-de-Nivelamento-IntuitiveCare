import unittest
from scraper import Scraper

class TestScraper(unittest.TestCase):
    def setUp(self):
        # HTML de exemplo com três links de PDF
        self.html = """
        <html>
            <body>
                <a href="document_anexo_i.pdf">Anexo I</a>
                <a href="document_anexo_ii.pdf">Anexo II</a>
                <a href="document_other.pdf">Other Document</a>
            </body>
        </html>
        """
        self.scraper = Scraper(self.html)
    
    def test_extract_all_links_by_extension(self):
        expected_links = [
            "document_anexo_i.pdf",
            "document_anexo_ii.pdf",
            "document_other.pdf"
        ]
        links = self.scraper.extract_all_links_by_extension("pdf")
        self.assertEqual(links, expected_links)

    def test_extract_links_by_names(self):
        expected_links = [
            "document_anexo_i.pdf",
            "document_anexo_ii.pdf"
        ]
        links = self.scraper.extract_links_by_names(["anexo_i", "anexo_ii"], "pdf")
        self.assertEqual(links, expected_links)

if __name__ == '__main__':
    unittest.main()
