import unittest
from file_system import FileSystem

class TestMv(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem()
        self.fs.touch("testFile.txt")
        self.fs.mkdir("sourceDir")
        self.fs.mkdir("destDir")
        self.fs.cd("sourceDir")
        self.fs.touch("fileInDir.txt")
        self.fs.cd("/")

    def test_moving_file_from_one_directory_to_another(self):
        self.fs.mv("/sourceDir/fileInDir.txt", "/destDir")
        self.fs.cd("destDir")
        self.assertIn("fileInDir.txt", self.fs.ls(), "File should be moved to the destination directory")

    def test_moving_directory(self):
        self.fs.mv("sourceDir", "destDir")
        self.fs.cd("destDir")
        self.assertIn("sourceDir", self.fs.ls(), "Directory should be moved into the destination directory")

    def test_moving_to_non_existent_destination(self):
        response = self.fs.mv("testFile.txt", "/nonExistentDir")
        self.assertEqual(response, "Destination path not found", "Should return an error for non-existent destination")

    def test_moving_non_existent_file_or_directory(self):
        response = self.fs.mv("nonExistent.txt", "/destDir")
        self.assertEqual(response, "Item not found", "Should return an error for non-existent file or directory")

if __name__ == '__main__':
    unittest.main()
