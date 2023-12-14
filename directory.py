class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.contents = [] 

    def add_file(self, file):
        self.contents.append(file)

    def add_directory(self, directory):
        self.contents.append(directory)

    def list_contents(self):
        return [item.name for item in self.contents]
