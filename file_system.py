from helper import FileSystemHelper
from directory import Directory
from file import File
import copy

class FileSystem(FileSystemHelper):
    def __init__(self):
        self.root = Directory("root")
        self.current_directory = self.root
#mkdir
    def mkdir(self, dir_name):
        # for cheking for invalid characters in the directory name (i assuming  that '/',"\\" shoud not in directory name it may confuse with paths)
        if '/' in dir_name or '\\' in dir_name:
            return "Invalid directory name"
        if any(item.name == dir_name for item in self.current_directory.contents):
            return "Directory already exists"
        new_dir = Directory(dir_name, self.current_directory)
        self.current_directory.add_directory(new_dir)
#touch
    def touch(self, file_name):
        # same rule as i applied to directories
        if '/' in file_name or '\\' in file_name:
            return "Invalid file name"
        if any(item.name == file_name for item in self.current_directory.contents):
            return "File already exists"
        new_file = File(file_name)
        self.current_directory.add_file(new_file)
#ls
    def ls(self):
        return self.current_directory.list_contents()
#cat
    def cat(self, file_name):
        for item in self.current_directory.contents:
            if isinstance(item, File) and item.name == file_name:
                return item.content
        return "File not found"
#echo
    def echo(self, text, file_name, append=False):
        for item in self.current_directory.contents:
            if isinstance(item, File) and item.name == file_name:
                if append:
                    item.content += text
                else:
                    item.content = text
                return
        return "File not found"

#rm
    def rm(self, name):
        if name == "root":
            return "Cannot remove root directory"
        for item in self.current_directory.contents:
            if item.name == name:
                self.current_directory.contents.remove(item)
                return
        return "File or directory not found"
#mv
    def mv(self, source_path, destination_path):
        # Resolve the full path of the source
        source_full_path = self._resolve_full_path(source_path)
        source_dir_path, _, source_item_name = source_full_path.rpartition('/')
        source_dir = self._find_directory(source_dir_path) if source_dir_path else self.current_directory

        # Finding the item to move
        item_to_move = None
        for item in source_dir.contents:
            if item.name == source_item_name:
                item_to_move = item
                source_dir.contents.remove(item)
                break

        if item_to_move is None:
            return "Item not found"

        # Resolve the full path of the destination
        destination_full_path = self._resolve_full_path(destination_path)
        destination_dir = self._find_directory(destination_full_path)
        if destination_dir is None:
            return "Destination path not found"

        # moving item to dest location
        destination_dir.contents.append(item_to_move)

#cp
    def cp(self, source_path, destination_path):
        # Resolve the full path of the source
        source_full_path = self._resolve_full_path(source_path)
        source_dir_path, _, source_item_name = source_full_path.rpartition('/')
        source_dir = self._find_directory(source_dir_path) if source_dir_path else self.current_directory

        # finding the item to copy
        item_to_copy = None
        for item in source_dir.contents:
            if item.name == source_item_name:
                item_to_copy = copy.deepcopy(item)
                break

        if item_to_copy is None:
            return "Item not found"

        # Resolve the full path of the destination
        destination_full_path = self._resolve_full_path(destination_path)
        destination_dir = self._find_directory(destination_full_path)
        if destination_dir is None:
            return "Destination path not found"

        # coping to dest location
        destination_dir.contents.append(item_to_copy)
#cd

    def cd(self, path):
        if path == ".." and self.current_directory.name == "root":
            return "You are already in the root directory."
        new_directory = self._find_directory(path)
        if new_directory is None:
            return "Directory not found"
        self.current_directory = new_directory

    
    
 #grep
    def grep(self, pattern):
        found = []
        for item in self.current_directory.contents:
            if isinstance(item, File) and pattern in item.content:
                found.append(item.name)

        return found

    


