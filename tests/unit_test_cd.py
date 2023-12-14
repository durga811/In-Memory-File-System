import unittest
from file_system import FileSystem

class TestCd(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem()
        self.fs.mkdir("testDir")
        self.fs.cd("testDir")
        self.fs.mkdir("subDir")
        self.fs.cd("/")

    def test_changing_to_subdirectory(self):
        self.fs.cd("testDir")
        self.assertEqual(self.fs.get_current_path(), "/testDir", "Should change to the specified subdirectory")

    def test_changing_to_parent_directory_using_dots(self):
        self.fs.cd("testDir")
        self.fs.cd("..")
        self.assertEqual(self.fs.get_current_path(), "/", "Should change to the parent directory")

    def test_changing_to_non_existent_directory(self):
        response = self.fs.cd("nonExistentDir")
        self.assertEqual(response, "Directory not found", "Should return an error for non-existent directory")

    def test_changing_to_root_directory_using_slash_or_tilde(self):
        self.fs.cd("testDir")
        self.fs.cd("/")
        self.assertEqual(self.fs.get_current_path(), "/", "Should change to the root directory using /")
        self.fs.cd("testDir")
        self.fs.cd("~")
        self.assertEqual(self.fs.get_current_path(), "/", "Should change to the root directory using ~")

if __name__ == '__main__':
    unittest.main()
