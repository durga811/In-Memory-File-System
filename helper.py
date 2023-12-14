import json
from directory import Directory
from file import File

class FileSystemHelper:
    # fom making full path
    def _resolve_full_path(self, path):
        if not path.startswith('/'):
            return self.get_current_path() + '/' + path
        return path
    
    def _find_directory(self, path):
        # Handling "~" as root
        if path == "~":  
          return self.root
    
        if path.startswith("/"):
            current = self.root
            path_components = path.strip("/").split("/")
        else:
            current = self.current_directory
            path_components = path.split("/")

        for part in path_components:
            if not part or part == ".":
                continue
            elif part == "..":
                if current.parent is not None:
                    current = current.parent
            else:
                found = False
                for item in current.contents:
                    if isinstance(item, Directory) and item.name == part:
                        current = item
                        found = True
                        break
                if not found:
                    return None

        return current
    
#for Saving State
    def save_state(self, file_path):
        state = self._serialize_directory(self.root)
        with open(file_path, 'w') as file:
            json.dump(state, file, indent=4)

    def _serialize_directory(self, directory):
        dir_data = {'name': directory.name, 'type': 'directory', 'contents': []}
        for item in directory.contents:
            if isinstance(item, Directory):
                dir_data['contents'].append(self._serialize_directory(item))
            elif isinstance(item, File):
                dir_data['contents'].append({'name': item.name, 'type': 'file', 'content': item.content})
        return dir_data
    
#for Loading State

    def load_state(self, file_path):
        with open(file_path, 'r') as file:
            state = json.load(file)
        self.root = self._deserialize_directory(state)
        self.current_directory = self.root

    def _deserialize_directory(self, dir_data):
        directory = Directory(dir_data['name'])
        for item in dir_data['contents']:
            if item['type'] == 'directory':
                sub_dir = self._deserialize_directory(item)
                sub_dir.parent = directory
                directory.contents.append(sub_dir)
            elif item['type'] == 'file':
                file = File(item['name'], item['content'])
                directory.contents.append(file)
        return directory
    
#gets current path
    def get_current_path(self):
        path = []
        current = self.current_directory
        while current and current.name != "root":
            path.append(current.name)
            current = current.parent
        return '/' + '/'.join(reversed(path)) if path else '/'