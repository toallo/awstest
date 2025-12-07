# Quick Start Guide: Filesystem MCP Tool Demo

This guide will help you quickly get started with the Filesystem MCP Tool demonstration.

## What You'll Find Here

This demonstration provides a comprehensive example of using the filesystem MCP (Model Context Protocol) tool for various file operations with proper error handling and best practices.

## Files in This Demo

- **`filesystem_mcp_demo.py`**: Main demonstration class with all filesystem operations
- **`test_mcp_filesystem.py`**: Comprehensive test suite with error handling and edge cases
- **`README_MCP_DEMO.md`**: Detailed documentation of all features
- **`QUICKSTART.md`**: This quick start guide

## Run the Demo (5 seconds)

```bash
cd /projects/sandbox/awstest
python3 filesystem_mcp_demo.py
```

Expected output: 18 successful operations demonstrating all filesystem MCP capabilities.

## Run the Test Suite (10 seconds)

```bash
cd /projects/sandbox/awstest
python3 test_mcp_filesystem.py
```

Expected output: All tests pass with comprehensive coverage of:
- Error handling scenarios
- Edge cases (empty files, large files, special characters)
- Practical real-world scenarios

## Key Features Demonstrated

### 1. Basic Operations
```python
from filesystem_mcp_demo import FilesystemMCPDemo

demo = FilesystemMCPDemo()
demo.setup_workspace()

# Write and read text files
demo.write_text_file("hello.txt", "Hello, World!")
content = demo.read_text_file("hello.txt")

# Write and read JSON files
demo.write_json_file("config.json", {"key": "value"})
config = demo.read_json_file("config.json")
```

### 2. Directory Operations
```python
# Create directories
demo.create_directory("logs")
demo.create_directory("data/input")  # Creates nested dirs

# List directory contents
items = demo.list_directory()
```

### 3. File Management
```python
# Copy files
demo.copy_file("source.txt", "backup.txt")

# Delete files
demo.delete_file("old_file.txt")

# Append to files
demo.append_to_file("log.txt", "New log entry\n")
```

### 4. File Metadata
```python
# Check if file exists
exists = demo.file_exists("config.json")

# Get detailed file information
info = demo.get_file_info("data.txt")
print(f"Size: {info['size']} bytes")
print(f"Modified: {info['modified']}")
```

### 5. Advanced Operations
```python
# Search within files
matches = demo.search_in_file("app.log", "ERROR")
print(f"Found {len(matches)} errors")

# Export operation results
demo.export_results("results.json")
```

## Output Files

After running the demo, you'll find:

```
mcp_demo_workspace/
├── hello.txt                    # Sample text file
├── notes.txt                    # File with appended content
├── config.json                  # Sample JSON configuration
├── logs/
│   └── app.log                  # Sample log file
├── data/
│   └── input/                   # Nested directory structure
└── operation_results.json       # Complete operation log
```

## Understanding MCP Tool Equivalents

Each method in the demo maps to an MCP filesystem tool operation:

| Demo Method | MCP Tool Call |
|-------------|---------------|
| `write_text_file()` | `filesystem.write_file(path, content)` |
| `read_text_file()` | `filesystem.read_file(path)` |
| `create_directory()` | `filesystem.create_directory(path)` |
| `list_directory()` | `filesystem.list_directory(path)` |
| `file_exists()` | `filesystem.file_exists(path)` |
| `get_file_info()` | `filesystem.get_file_info(path)` |
| `copy_file()` | `filesystem.copy_file(src, dst)` |
| `delete_file()` | `filesystem.delete_file(path)` |

## Error Handling Examples

The demo shows proper error handling for common scenarios:

```python
# Reading non-existent file
content = demo.read_text_file("missing.txt")
if content is None:
    print("File not found - handled gracefully")

# Invalid JSON
data = demo.read_json_file("corrupt.json")
if data is None:
    print("Invalid JSON - error logged")

# Copy from non-existent source
success = demo.copy_file("missing.txt", "dest.txt")
if not success:
    print("Copy failed - error handled")
```

## Real-World Use Cases

### Configuration Management
```python
# Load config, modify, save
config = demo.read_json_file("config.json")
config["debug"] = True
demo.write_json_file("config.json", config)
```

### Log Analysis
```python
# Find errors in logs
errors = demo.search_in_file("app.log", "ERROR")
for error in errors:
    print(f"Line {error['line_number']}: {error['content']}")
```

### Backup Operations
```python
# Create backup
demo.create_directory("backups")
demo.copy_file("important.txt", "backups/important_backup.txt")
```

### Data Pipeline
```python
# Process files from input to output
demo.create_directory("pipeline/input")
demo.create_directory("pipeline/output")

input_files = demo.list_directory("pipeline/input")
for filename in input_files:
    # Process each file
    content = demo.read_text_file(f"pipeline/input/{filename}")
    processed = content.upper()  # Example processing
    demo.write_text_file(f"pipeline/output/{filename}", processed)
```

## Next Steps

1. **Read the full documentation**: See `README_MCP_DEMO.md` for detailed API reference
2. **Explore the code**: Open `filesystem_mcp_demo.py` to see implementation details
3. **Run the tests**: Execute `test_mcp_filesystem.py` to see comprehensive testing
4. **Customize for your needs**: Extend the `FilesystemMCPDemo` class with your own methods

## Tips for Integration

When integrating MCP filesystem tools into your projects:

1. ✅ Always use try-except blocks for I/O operations
2. ✅ Check file existence before reading or deleting
3. ✅ Validate file paths to prevent security issues
4. ✅ Log all operations for debugging and auditing
5. ✅ Handle different error types specifically (FileNotFoundError, PermissionError, etc.)
6. ✅ Use Path objects for cross-platform compatibility
7. ✅ Always specify encoding for text files (UTF-8)
8. ✅ Test edge cases (empty files, large files, special characters)

## Troubleshooting

**Q: Permission denied errors?**
A: Ensure the workspace directory is writable. Check permissions with `ls -la`.

**Q: Module not found?**
A: Run from the `/projects/sandbox/awstest` directory.

**Q: Tests fail?**
A: Ensure Python 3.6+ is installed. Check with `python3 --version`.

## Support

For questions or issues with this demonstration, review:
- The inline code documentation in `filesystem_mcp_demo.py`
- The comprehensive README in `README_MCP_DEMO.md`
- The test examples in `test_mcp_filesystem.py`

## License

This demonstration is provided as-is for educational and development purposes.
