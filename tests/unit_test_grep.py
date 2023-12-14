import unittest
from file_system import FileSystem

class TestGrep(unittest.TestCase):
    def setUp(self):
        # Set up a basic directory structure with files
        self.fs = FileSystem()
        self.fs.mkdir("testDir")
        self.fs.cd("testDir")
        self.fs.touch("file1.txt")
        self.fs.echo("file1.txt", "Hello World")
        self.fs.touch("file2.txt")
        self.fs.echo("file2.txt", "Another file with different content")
        self.fs.cd("/")

    def test_searching_for_text_pattern_in_files(self):
        self.fs.cd("testDir")
        results = self.fs.grep("Hello")
        self.assertIn("file1.txt", results, "File containing the pattern should be found")

    def test_searching_for_pattern_not_present_in_any_file(self):
        self.fs.cd("testDir")
        results = self.fs.grep("Nonexistent Pattern")
        self.assertEqual(len(results), 0, "No files should be found for a nonexistent pattern")

    def test_searching_in_directory_with_no_files(self):
        self.fs.mkdir("emptyDir")
        self.fs.cd("emptyDir")
        results = self.fs.grep("Any Pattern")
        self.assertEqual(len(results), 0, "No files should be found in an empty directory")

if __name__ == '__main__':
    unittest.main()
