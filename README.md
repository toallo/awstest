# Filesystem Tool Task Implementation

This repository demonstrates comprehensive filesystem tool capabilities through a practical Python implementation.

## Overview

The `server.py` file implements a `FilesystemToolTask` class that showcases various filesystem operations including reading, writing, listing, copying, searching, and managing files and directories.

## Features

### Core Filesystem Operations

1. **Directory Management**
   - Create directories with parent path creation
   - List directory contents with metadata
   - Navigate directory structures

2. **File Operations**
   - Write files with automatic parent directory creation
   - Read files with proper error handling
   - Copy files between locations
   - Delete files safely
   - Get detailed file information (size, timestamps, type)

3. **Search Capabilities**
   - Search for files using patterns (e.g., `*.txt`, `*.json`)
   - Recursive file discovery
   - Pattern matching across directory trees

4. **Error Handling**
   - Comprehensive try-catch blocks for all operations
   - Detailed error messages and logging
   - Graceful handling of missing files/directories
   - Operation status tracking

5. **Logging and Reporting**
   - Timestamp all operations
   - Track operation status (SUCCESS, ERROR, WARNING)
   - Generate JSON execution summary reports
   - Real-time console output

## Usage

### Basic Usage

Run the demonstration script:

```bash
python server.py
```

This will execute a comprehensive demonstration that:
1. Creates a directory structure (`data/`, `logs/`, `config/`, `backups/`)
2. Writes various types of files (text, JSON, markdown, logs)
3. Reads and displays file contents
4. Lists directory contents with metadata
5. Retrieves detailed file information
6. Copies files to backup locations
7. Searches for files by pattern
8. Generates an execution summary report

### Using the FilesystemToolTask Class

You can also import and use the class in your own code:

```python
from server import FilesystemToolTask

# Initialize with custom workspace
task = FilesystemToolTask(workspace_dir="./my_workspace")

# Create directories
task.create_directory("data/input")
task.create_directory("data/output")

# Write a file
task.write_file("data/input/example.txt", "Hello, World!")

# Read a file
content = task.read_file("data/input/example.txt")
print(content)

# List directory
files = task.list_directory("data")
for file in files:
    print(f"{file['name']}: {file['size']} bytes")

# Get file info
info = task.get_file_info("data/input/example.txt")
print(f"Modified: {info['modified']}")

# Copy file
task.copy_file("data/input/example.txt", "data/output/example.txt")

# Search for files
txt_files = task.search_files("*.txt")
print(f"Found {len(txt_files)} text files")

# Delete file
task.delete_file("data/output/example.txt")
```

## Output

When you run the demonstration, you'll see:

1. **Console Output**: Real-time logging of all operations with status indicators
2. **Created Files**: A complete filesystem workspace with sample files
3. **Summary Report**: A JSON file (`logs/execution_summary.json`) containing detailed execution statistics

### Sample Output Structure

```
filesystem_workspace/
├── data/
│   ├── sample.txt
│   └── notes.md
├── config/
│   └── settings.json
├── logs/
│   ├── app.log
│   └── execution_summary.json
└── backups/
    ├── sample_backup.txt
    └── settings_backup.json
```

## Class Methods

### FilesystemToolTask Methods

- `__init__(workspace_dir)`: Initialize with a workspace directory
- `create_directory(dir_path)`: Create a directory
- `write_file(file_path, content, mode)`: Write content to a file
- `read_file(file_path, mode)`: Read content from a file
- `list_directory(dir_path)`: List directory contents with metadata
- `copy_file(src_path, dest_path)`: Copy a file
- `delete_file(file_path)`: Delete a file
- `get_file_info(file_path)`: Get detailed file information
- `search_files(pattern, search_dir)`: Search for files matching a pattern
- `run_demonstration()`: Execute the full demonstration
- `log_result(operation, status, details)`: Log operation results

## Error Handling

All methods include comprehensive error handling:

- **File Not Found**: Returns `None` or `False` with error logging
- **Permission Errors**: Caught and logged with details
- **Path Errors**: Parent directories created automatically when needed
- **General Exceptions**: All unexpected errors are caught and logged

## Requirements

- Python 3.6+
- Standard library only (no external dependencies)

## License

This is a demonstration implementation for educational purposes.
