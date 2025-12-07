# Filesystem MCP Tool Demonstration

This demonstration showcases practical usage of the filesystem MCP (Model Context Protocol) tool for various file operations.

## Overview

The Model Context Protocol (MCP) provides standardized interfaces for tools to interact with systems. This demonstration focuses on the filesystem tool, which enables controlled and secure file operations.

## Features Demonstrated

### 1. Basic File Operations
- **Writing Text Files**: Create and write content to text files
- **Reading Text Files**: Read and retrieve file contents
- **Appending to Files**: Add content to existing files

### 2. Structured Data Operations
- **JSON Writing**: Serialize and write JSON data
- **JSON Reading**: Parse and read JSON data with validation

### 3. Directory Operations
- **Creating Directories**: Create single and nested directories
- **Listing Contents**: Enumerate files and directories
- **Navigation**: Work with subdirectories

### 4. File Metadata
- **Existence Checks**: Verify if files exist
- **File Information**: Retrieve size, timestamps, and properties
- **Type Detection**: Identify files vs directories

### 5. File Manipulation
- **Copying Files**: Duplicate files to new locations
- **Deleting Files**: Remove files with proper error handling
- **Moving/Renaming**: Relocate files within the filesystem

### 6. Advanced Operations
- **Content Search**: Search for patterns within files
- **Batch Operations**: Perform multiple operations efficiently
- **Result Logging**: Track all operations with detailed logs

## Running the Demonstration

```bash
python3 filesystem_mcp_demo.py
```

## Code Structure

### Main Class: `FilesystemMCPDemo`

The demonstration is organized as a class with methods corresponding to MCP filesystem operations:

```python
demo = FilesystemMCPDemo(workspace_dir="/path/to/workspace")
demo.setup_workspace()
demo.write_text_file("example.txt", "Hello, MCP!")
content = demo.read_text_file("example.txt")
```

### Error Handling

All operations include comprehensive error handling:

```python
try:
    filepath.write_text(content)
    log_operation("write_file", "SUCCESS", details)
except Exception as e:
    log_operation("write_file", "ERROR", str(e))
```

### Operation Logging

Every operation is logged with:
- Timestamp
- Operation name
- Status (SUCCESS, ERROR, WARNING)
- Detailed description
- Optional data payload

## MCP Tool Equivalents

Each method documents its equivalent MCP filesystem tool call:

| Demo Method | MCP Tool Equivalent |
|-------------|---------------------|
| `write_text_file()` | `filesystem.write_file(path, content)` |
| `read_text_file()` | `filesystem.read_file(path)` |
| `create_directory()` | `filesystem.create_directory(path)` |
| `list_directory()` | `filesystem.list_directory(path)` |
| `file_exists()` | `filesystem.file_exists(path)` |
| `get_file_info()` | `filesystem.get_file_info(path)` |
| `copy_file()` | `filesystem.copy_file(src, dst)` |
| `delete_file()` | `filesystem.delete_file(path)` |

## Example Usage Scenarios

### Scenario 1: Configuration Management

```python
# Write configuration
config = {
    "api_key": "xxx",
    "timeout": 30,
    "retry_count": 3
}
demo.write_json_file("config.json", config)

# Read configuration
config = demo.read_json_file("config.json")
```

### Scenario 2: Log File Analysis

```python
# Create log file
demo.write_text_file("logs/app.log", log_content)

# Search for errors
errors = demo.search_in_file("logs/app.log", "ERROR")
print(f"Found {len(errors)} errors")
```

### Scenario 3: Batch File Processing

```python
# Create multiple files
for i in range(10):
    demo.write_text_file(f"data/file_{i}.txt", f"Data {i}")

# List all files
files = demo.list_directory("data")
print(f"Created {len(files)} files")
```

## Output

The demonstration produces:

1. **Console Output**: Real-time operation logging with status indicators
2. **Operation Summary**: Statistics on success/error rates
3. **Results File**: JSON export of all operations (`operation_results.json`)

### Sample Console Output

```
[SUCCESS] setup_workspace: Created workspace directory: /path/to/workspace
[SUCCESS] write_text_file: Wrote 45 bytes to hello.txt
[SUCCESS] read_text_file: Read 45 bytes from hello.txt
[SUCCESS] create_directory: Created directory: logs
[ERROR] read_text_file: File not found: nonexistent.txt
```

### Sample Results File

```json
{
  "summary": {
    "total_operations": 25,
    "successful": 23,
    "errors": 2,
    "warnings": 0,
    "success_rate": "92.0%"
  },
  "operations": [
    {
      "timestamp": "2024-01-15T10:30:00",
      "operation": "write_text_file",
      "status": "SUCCESS",
      "details": "Wrote 45 bytes to hello.txt",
      "data": {
        "filepath": "/path/to/hello.txt",
        "size": 45
      }
    }
  ]
}
```

## Best Practices Demonstrated

1. **Always validate inputs** before filesystem operations
2. **Check file existence** before reading or deleting
3. **Use try-except blocks** for all I/O operations
4. **Log operations** for debugging and auditing
5. **Handle different error types** (FileNotFoundError, PermissionError, etc.)
6. **Use Path objects** for cross-platform compatibility
7. **Encode text files** explicitly (UTF-8)
8. **Clean up resources** after operations

## Security Considerations

The demonstration includes security best practices:

- **Path validation**: Ensures operations stay within workspace
- **Error disclosure**: Doesn't expose sensitive system information
- **Permission handling**: Gracefully handles permission errors
- **Input validation**: Validates all user-provided paths and content

## Extending the Demonstration

To add custom operations:

```python
def custom_operation(self, filename: str) -> bool:
    """
    Your custom filesystem operation.
    
    MCP Tool Equivalent: filesystem.custom_method()
    """
    try:
        # Your operation logic here
        self.log_operation("custom_operation", "SUCCESS", "Details")
        return True
    except Exception as e:
        self.log_operation("custom_operation", "ERROR", str(e))
        return False
```

## Workspace Structure

After running the demonstration, the workspace will contain:

```
mcp_demo_workspace/
├── hello.txt
├── notes.txt
├── config.json
├── logs/
│   └── app.log
├── data/
│   └── input/
└── operation_results.json
```

## Troubleshooting

### Permission Errors
Ensure the workspace directory is writable:
```bash
chmod 755 /projects/sandbox/awstest/mcp_demo_workspace
```

### Import Errors
Ensure Python 3.6+ is installed:
```bash
python3 --version
```

### Workspace Already Exists
The demonstration safely handles existing workspaces and won't overwrite files unless explicitly programmed to do so.

## License

This demonstration is provided as-is for educational purposes.
