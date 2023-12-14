import unittest
import os
from file_system import FileSystem

class TestStatePersistence(unittest.TestCase):
    def setUp(self):
        # Set up a basic file system
        self.fs = FileSystem()
        self.state_file = "test_state.json"

    def tearDown(self):
        # Clean up the state file after tests
        if os.path.exists(self.state_file):
            os.remove(self.state_file)

    def test_saving_state_of_file_system(self):
        self.fs.touch("testFile.txt")
        self.fs.mkdir("testDir")
        self.fs.save_state(self.state_file)
        self.assertTrue(os.path.exists(self.state_file), "State file should exist after saving")

    def test_loading_saved_state(self):
        self.fs.touch("testFile.txt")
        self.fs.save_state(self.state_file)
        new_fs = FileSystem()
        new_fs.load_state(self.state_file)
        self.assertIn("testFile.txt", new_fs.ls(), "Loaded state should contain the saved file")

    def test_loading_from_non_existent_state_file(self):
        new_fs = FileSystem()
        with self.assertRaises(FileNotFoundError):
            new_fs.load_state("non_existent_state.json")

if __name__ == '__main__':
    unittest.main()
