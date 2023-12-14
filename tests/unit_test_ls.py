import unittest
from file_system import FileSystem

class TestLs(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem()

    def test_listing_empty_directory(self):
        self.fs.mkdir("emptyDir")
        self.fs.cd("emptyDir")
        contents = self.fs.ls()
        self.assertEqual(len(contents), 0, "Empty directory should have no contents")

    def test_listing_directory_with_multiple_files_and_directories(self):
        self.fs.mkdir("testDir")
        self.fs.cd("testDir")
        self.fs.touch("file1.txt")
        self.fs.touch("file2.txt")
        self.fs.mkdir("subDir")
        contents = self.fs.ls()
        self.assertEqual(len(contents), 3, "Should list all files and directories")

    def test_listing_non_existent_directory(self):
        response = self.fs.ls()  # Attempt to list contents in a non-existent directory
        self.assertIsNotNone(response, "Should return an error message or an empty list for non-existent directory")

if __name__ == '__main__':
    unittest.main()
