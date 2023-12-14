import unittest
from file_system import FileSystem

class TestRm(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem()
        self.fs.touch("testFile.txt")
        self.fs.mkdir("testDir")

    def test_removing_existing_file(self):
        self.fs.rm("testFile.txt")
        self.assertNotIn("testFile.txt", self.fs.ls(), "File should be removed")

    def test_removing_existing_directory(self):
        self.fs.rm("testDir")
        self.assertNotIn("testDir", self.fs.ls(), "Directory should be removed")

    def test_attempting_to_remove_non_existent_file_or_directory(self):
        response = self.fs.rm("nonExistent")
        self.assertEqual(response, "File or directory not found", "Should return an error for non-existent file or directory")

    def test_removing_root_directory(self):
        response = self.fs.rm("root")
        self.assertEqual(response, "Cannot remove root directory", "Should not allow removing the root directory")

if __name__ == '__main__':
    unittest.main()
