# Quick Start Guide

## Run the Demo
```bash
python3 server.py
```

## Try Examples
```bash
# Basic usage
python3 example_usage.py

# Error handling
python3 test_error_handling.py

# Advanced patterns
python3 advanced_example.py
```

## Use in Your Code
```python
from server import FilesystemToolTask

# Create instance
task = FilesystemToolTask("./my_workspace")

# Create directories
task.create_directory("data/input")

# Write files
task.write_file("data/config.json", '{"key": "value"}')

# Read files
content = task.read_file("data/config.json")

# List directory
files = task.list_directory("data")

# Search files
txt_files = task.search_files("*.txt")

# Copy files
task.copy_file("data/config.json", "backups/config.json")

# Get file info
info = task.get_file_info("data/config.json")
```

## Documentation
- `README.md` - Overview and features
- `USAGE_GUIDE.md` - Detailed documentation

## Requirements
- Python 3.6+
- No external dependencies
