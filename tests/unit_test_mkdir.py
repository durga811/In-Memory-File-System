import unittest
from file_system import FileSystem

class TestMkdir(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem()

    def test_create_new_directory_in_root(self):
        self.fs.mkdir("newDir")
        self.assertIn("newDir", self.fs.ls(), "Directory should be created in root")

    def test_create_new_directory_in_subdirectory(self):
        self.fs.mkdir("parentDir")
        self.fs.cd("parentDir")
        self.fs.mkdir("childDir")
        self.assertIn("childDir", self.fs.ls(), "Directory should be created in subdirectory")

    def test_create_existing_directory(self):
        self.fs.mkdir("existingDir")
        response = self.fs.mkdir("existingDir")
        self.assertEqual(response, "Directory already exists", "Should not create a directory that already exists")

    def test_create_directory_with_invalid_name(self):
        response = self.fs.mkdir("invalid/name")
        self.assertIsNotNone(response, "Should return an error message for invalid directory name")

if __name__ == '__main__':
    unittest.main()
