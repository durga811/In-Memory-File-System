
# In-Memory File System

## Overview
This project implements a basic in-memory file system in Python. It simulates several common file system operations such as creating directories and files, navigating through directories, displaying and modifying file contents, and more.

## Features
- Directory and file creation (`mkdir`, `touch`)
- Navigation within the file system (`cd`)
- Listing contents of directories (`ls`)
- Displaying and editing file contents (`cat`, `echo`)
- Moving and copying files/directories (`mv`, `cp`)
- Deleting files/directories (`rm`)
- Searching within files (`grep`)
- State persistence (saving and loading file system state)

## Additional Features and Improvements
1. **Enhanced File Writing**:
   - Writing to an existing file with `echo` replaces its content.
     ```bash
     echo "New content" > example.txt
     ```
   - Appending content to an existing file using `echo` with a `True` flag.
     ```bash
     echo "New content that I want to add to the file" > example.txt True
     ```
2. **Improved State Persistence**:
   - `load_n_save_state` command allows loading the previous state and saving current modifications.
     ```bash
     python main.py load_n_save_state
     ```

## Implementation Details
- **Data Structures**: The file system utilizes classes `Directory` and `File` to represent directories and files, respectively. Directories can contain multiple files and subdirectories.
- **Design Decisions**: 
  - The file system is entirely in-memory for quick access.
  - A hierarchical structure is used, similar to typical file systems.
  - State persistence is implemented using JSON serialization.
- **Error Handling**: The system handles common error cases such as invalid paths or operations on non-existent files/directories.

## Setup and Usage
### Prerequisites
- *Python* installed in your system
(Else Download from *https://www.python.org/downloads/*)

### Running the File System
1. Clone the repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Run the file system using the command:
   ```bash
   python main.py
   ```

### Basic Commands
- `mkdir <directory_name>`: Create a new directory.
  ```bash
  mkdir newDir
  ```
- `touch <file_name>`: Create a new file.
  ```bash
  touch example.txt
  ```
- `ls`: List contents of the current directory.
  ```bash
  ls
  ```
- `cd <path>`: Change the current directory.
  ```bash
  cd newDir
  ```
- `cat <file_name>`: Display the contents of a file.
  ```bash
  cat example.txt
  ```
- `echo <text> > <file_name>`: Write text to a file.
  ```bash
  echo "Hello, World!" > example.txt
  ```
- `mv <source> <destination>`: Move a file or directory.
  ```bash
  mv example.txt newDir/
  ```
- `cp <source> <destination>`: Copy a file or directory.
  ```bash
  cp newDir/example.txt example_copy.txt
  ```
- `rm <name>`: Remove a file or directory.
  ```bash
  rm oldFile.txt
  ```
- `grep <pattern>`: Search for a pattern in files.
  ```bash
  grep "Hello"
  ```

### Editing File Content
To edit the content of a file, use the `echo` command:
```bash
echo "New content" > example.txt
```

### Running Unit Tests
To run unit tests for a specific function, use the following command structure:
```bash
python -m unittest tests.unit_test_<functionality>
```
For example, to test the `mkdir` functionality:
```bash
python -m unittest tests.unit_test_mkdir
```

##

