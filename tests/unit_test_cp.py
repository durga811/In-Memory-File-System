import unittest
from file_system import FileSystem

class TestCp(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem()
        self.fs.touch("testFile.txt")
        self.fs.mkdir("sourceDir")
        self.fs.cd("sourceDir")
        self.fs.touch("fileInDir.txt")
        self.fs.cd("/")
        self.fs.mkdir("destDir")

    def test_copying_file_from_one_directory_to_another(self):
        self.fs.cp("/sourceDir/fileInDir.txt", "/destDir")
        self.fs.cd("destDir")
        self.assertIn("fileInDir.txt", self.fs.ls(), "File should be copied to the destination directory")

    def test_copying_directory(self):
        self.fs.cp("sourceDir", "destDir")
        self.fs.cd("destDir")
        self.assertIn("sourceDir", self.fs.ls(), "Directory should be copied to the destination directory")

    def test_copying_to_non_existent_destination(self):
        response = self.fs.cp("testFile.txt", "/nonExistentDir")
        self.assertEqual(response, "Destination path not found", "Should return an error for non-existent destination")

    def test_copying_non_existent_file_or_directory(self):
        response = self.fs.cp("nonExistent.txt", "/destDir")
        self.assertEqual(response, "Item not found", "Should return an error for non-existent file or directory")

if __name__ == '__main__':
    unittest.main()
