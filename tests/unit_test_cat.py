import unittest
from file_system import FileSystem

class TestCat(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem()
        self.fs.touch("testFile.txt")
        self.fs.echo("testFile.txt", "Hello, World!")

    def test_displaying_contents_of_existing_file(self):
        content = self.fs.cat("testFile.txt")
        self.assertEqual(content, "Hello, World!", "Content of the file should be displayed correctly")

    def test_attempting_to_display_contents_of_non_existent_file(self):
        response = self.fs.cat("nonExistentFile.txt")
        self.assertEqual(response, "File not found", "Should return 'File not found' for a non-existent file")

    def test_displaying_file_with_special_characters_or_spaces_in_name(self):
        filename = "special @file!.txt"
        expected_content = "Special content"
        self.fs.touch(filename)
        self.fs.echo(filename, expected_content)
        content = self.fs.cat(filename)
        self.assertEqual(content, expected_content, "Should handle files with special characters or spaces in name")

if __name__ == '__main__':
    unittest.main()
