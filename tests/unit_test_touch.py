import unittest
from file_system import FileSystem

class TestTouch(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem()

    def test_create_new_file_in_root(self):
        self.fs.touch("newFile.txt")
        self.assertIn("newFile.txt", self.fs.ls(), "File should be created in root")

    def test_create_new_file_in_subdirectory(self):
        self.fs.mkdir("testDir")
        self.fs.cd("testDir")
        self.fs.touch("newFile.txt")
        self.assertIn("newFile.txt", self.fs.ls(), "File should be created in subdirectory")

    def test_create_existing_file(self):
        self.fs.touch("existingFile.txt")
        response = self.fs.touch("existingFile.txt")
        self.assertEqual(response, "File already exists", "Should not create a file that already exists")

    def test_create_file_with_invalid_name(self):
        response = self.fs.touch("invalid/name.txt")
        self.assertIsNotNone(response, "Should return an error message for invalid file name")

if __name__ == '__main__':
    unittest.main()
