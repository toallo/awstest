# Filesystem Tool Task - Usage Guide

## Quick Start

### Run the Main Demonstration
```bash
python3 server.py
```

This will create a `filesystem_workspace` directory and demonstrate all core filesystem operations.

### Run the Example Usage Script
```bash
python3 example_usage.py
```

This creates an `example_workspace` with a sample project structure.

### Test Error Handling
```bash
python3 test_error_handling.py
```

This demonstrates robust error handling for various edge cases.

### Advanced Examples
```bash
python3 advanced_example.py
```

This shows advanced patterns like versioned backups, file organization, and batch operations.

## Available Scripts

### 1. server.py (Main Implementation)
The core implementation of the `FilesystemToolTask` class with a comprehensive demonstration.

**Features:**
- Create directories with automatic parent creation
- Write files (text and binary)
- Read files with error handling
- List directory contents with metadata
- Copy files between locations
- Delete files safely
- Get detailed file information
- Search files by pattern
- Complete operation logging

**Output:**
- Creates `filesystem_workspace/` directory
- Sample files in data/, config/, logs/, backups/
- Execution summary JSON report

### 2. example_usage.py
Practical examples of using the FilesystemToolTask class programmatically.

**Demonstrates:**
- Creating project structures
- Writing configuration files
- Reading and displaying files
- Listing directories with icons
- Getting file metadata
- Copying files
- Searching by file type
- Writing log files

**Output:**
- Creates `example_workspace/` directory
- Project structure with src/, tests/, docs/, build/
- Configuration and documentation files

### 3. test_error_handling.py
Tests error handling for various failure scenarios.

**Tests:**
- Reading non-existent files
- Listing non-existent directories
- Getting info for missing files
- Copying non-existent files
- Deleting missing files
- Recovery after errors

**Output:**
- Creates `test_workspace/` directory
- Shows graceful error handling
- Displays error statistics

### 4. advanced_example.py
Advanced usage patterns and complex operations.

**Demonstrates:**
- Versioned file backups with timestamps
- Organizing files by extension
- Creating project snapshots with metadata
- Generating directory structure reports
- Batch file operations
- Recursive directory scanning

**Output:**
- Creates `advanced_workspace/` directory
- Complex directory hierarchy
- Generated reports and snapshots

## Class API Reference

### FilesystemToolTask Class

#### Constructor
```python
task = FilesystemToolTask(workspace_dir="./my_workspace")
```

#### Methods

**create_directory(dir_path: str) -> bool**
- Creates a directory with all parent directories
- Parameters: `dir_path` - relative path to create
- Returns: `True` if successful, `False` otherwise

**write_file(file_path: str, content: str, mode: str = 'w') -> bool**
- Writes content to a file
- Parameters: 
  - `file_path` - relative path to file
  - `content` - content to write
  - `mode` - 'w' for text, 'wb' for binary
- Returns: `True` if successful, `False` otherwise

**read_file(file_path: str, mode: str = 'r') -> Optional[str]**
- Reads content from a file
- Parameters:
  - `file_path` - relative path to file
  - `mode` - 'r' for text, 'rb' for binary
- Returns: File content or `None` if error

**list_directory(dir_path: str = ".") -> Optional[List[Dict]]**
- Lists directory contents with metadata
- Parameters: `dir_path` - relative path to directory
- Returns: List of dictionaries with file/directory info

**copy_file(src_path: str, dest_path: str) -> bool**
- Copies a file from source to destination
- Parameters:
  - `src_path` - source file path
  - `dest_path` - destination file path
- Returns: `True` if successful, `False` otherwise

**delete_file(file_path: str) -> bool**
- Deletes a file
- Parameters: `file_path` - relative path to file
- Returns: `True` if successful, `False` otherwise

**get_file_info(file_path: str) -> Optional[Dict]**
- Gets detailed file information
- Parameters: `file_path` - relative path to file
- Returns: Dictionary with file metadata

**search_files(pattern: str, search_dir: str = ".") -> Optional[List[str]]**
- Searches for files matching a pattern
- Parameters:
  - `pattern` - glob pattern (e.g., "*.txt")
  - `search_dir` - directory to search in
- Returns: List of matching file paths

## Common Use Cases

### 1. Creating a Project Structure
```python
task = FilesystemToolTask("./myproject")
task.create_directory("src")
task.create_directory("tests")
task.create_directory("docs")
task.write_file("README.md", "# My Project\n")
```

### 2. Backing Up Configuration
```python
task.copy_file("config/settings.json", "backups/settings_backup.json")
```

### 3. Finding All Python Files
```python
python_files = task.search_files("*.py")
for file in python_files:
    print(f"Found: {file}")
```

### 4. Reading and Processing Files
```python
content = task.read_file("data/input.txt")
if content:
    processed = content.upper()
    task.write_file("data/output.txt", processed)
```

### 5. Generating Reports
```python
files = task.list_directory("src")
report = f"Found {len(files)} files\n"
for file in files:
    report += f"- {file['name']} ({file['size']} bytes)\n"
task.write_file("reports/file_report.txt", report)
```

## Error Handling

All methods include comprehensive error handling:

- **Missing files/directories**: Returns `None` or `False` with error logging
- **Permission errors**: Caught and logged
- **Path errors**: Parent directories created automatically
- **Exceptions**: All errors caught and logged without crashing

Check operation results:
```python
if task.write_file("test.txt", "content"):
    print("Success!")
else:
    print("Failed - check logs")
```

## Logging

All operations are logged with:
- Timestamp (ISO format)
- Operation name
- Status (SUCCESS, ERROR, WARNING)
- Details message

Access logs:
```python
for result in task.results:
    print(f"{result['timestamp']}: {result['operation']} - {result['status']}")
```

## Best Practices

1. **Always check return values** for critical operations
2. **Use relative paths** within the workspace
3. **Create parent directories** automatically using write_file
4. **Handle None/False returns** gracefully
5. **Review operation logs** for debugging
6. **Use appropriate file modes** ('w' for text, 'wb' for binary)
7. **Clean up temporary files** when done

## Troubleshooting

**Q: Files not appearing?**
- Check the workspace directory path
- Verify operations returned True/success
- Review logs in task.results

**Q: Permission errors?**
- Ensure write permissions on workspace directory
- Check file ownership

**Q: Path errors?**
- Use forward slashes in paths
- Keep paths relative to workspace
- Parent directories are created automatically

## Examples Output

Run all examples to see:
- `filesystem_workspace/` - Main demonstration output
- `example_workspace/` - Basic usage examples
- `test_workspace/` - Error handling tests
- `advanced_workspace/` - Advanced patterns

All directories contain sample files, logs, and reports demonstrating the capabilities.

## Requirements

- Python 3.6 or higher
- Standard library only (no external dependencies)

## Support

For more information, see:
- `README.md` - Overview and features
- Source code comments in `server.py`
- Example scripts for practical demonstrations
