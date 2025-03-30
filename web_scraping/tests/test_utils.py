import os
import tempfile
import unittest
import zipfile
from utils import create_zip

class TestUtils(unittest.TestCase):
    def test_create_zip(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            file1_path = os.path.join(tmpdir, "file1.txt")
            file2_path = os.path.join(tmpdir, "file2.txt")
            with open(file1_path, "w") as f:
                f.write("Hello")
            with open(file2_path, "w") as f:
                f.write("World")
            
            zip_path = os.path.join(tmpdir, "test.zip")
            create_zip([file1_path, file2_path], zip_path)
            
            self.assertTrue(os.path.exists(zip_path))
            with zipfile.ZipFile(zip_path, 'r') as zipf:
                namelist = zipf.namelist()
                self.assertIn("file1.txt", namelist)
                self.assertIn("file2.txt", namelist)

if __name__ == '__main__':
    unittest.main()
