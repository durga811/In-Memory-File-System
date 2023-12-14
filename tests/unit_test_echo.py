import unittest
from file_system import FileSystem

class TestEcho(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem()
        self.fs.touch("testFile.txt")

    def test_writing_text_to_existing_file(self):
        self.fs.echo("Hello, World!", "testFile.txt")
        content = self.fs.cat("testFile.txt")
        self.assertEqual(content, "Hello, World!", "Text should be written to the existing file")

    def test_writing_text_to_non_existent_file(self):
        response = self.fs.echo("Sample Text", "nonExistentFile.txt")
        self.assertEqual(response, "File not found", "Should return an error for non-existent file")

    def test_appending_text_to_existing_file(self):
        self.fs.echo("Hello", "testFile.txt")
        self.fs.echo(", World!", "testFile.txt", append=True)
        content = self.fs.cat("testFile.txt")
        self.assertEqual(content, "Hello, World!", "Text should be appended to the existing file")

if __name__ == '__main__':
    unittest.main()
