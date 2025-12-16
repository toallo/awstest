#!/usr/bin/env python3
"""
Example usage of the FilesystemToolTask class.

This script demonstrates how to use the filesystem tool task
programmatically for your own projects.
"""

from server import FilesystemToolTask


def main():
    """Example usage scenarios."""

    # Initialize the task with a custom workspace
    print("Creating FilesystemToolTask instance...\n")
    task = FilesystemToolTask(workspace_dir="./example_workspace")

    # Example 1: Create a project structure
    print("Example 1: Creating a project structure")
    print("-" * 50)
    task.create_directory("src")
    task.create_directory("tests")
    task.create_directory("docs")
    task.create_directory("build")
    print()

    # Example 2: Write configuration files
    print("Example 2: Writing configuration files")
    print("-" * 50)
    import json
    config = {
        "project": "My Application",
        "version": "0.1.0",
        "author": "Developer"
    }
    task.write_file("config.json", json.dumps(config, indent=2))

    task.write_file("src/main.py", "#!/usr/bin/env python3\n\ndef main():\n    print('Hello, World!')\n\nif __name__ == '__main__':\n    main()\n")
    
    task.write_file("README.md", "# My Application\n\nThis is a sample project.\n")
    print()

    # Example 3: Read and display files
    print("Example 3: Reading files")
    print("-" * 50)
    config_content = task.read_file("config.json")
    if config_content:
        print("Config file contents:")
        print(config_content)
    print()

    # Example 4: List directory contents
    print("Example 4: Listing directory contents")
    print("-" * 50)
    root_contents = task.list_directory(".")
    if root_contents:
        print("Root directory contents:")
        for item in root_contents:
            item_type = "📁" if item["type"] == "directory" else "📄"
            size_info = f"{item['size']} bytes" if item['size'] is not None else "N/A"
            print(f"  {item_type} {item['name']} ({size_info})")
    print()

    # Example 5: Get file information
    print("Example 5: Getting file information")
    print("-" * 50)
    info = task.get_file_info("config.json")
    if info:
        print(f"File: {info['name']}")
        print(f"Size: {info['size']} bytes")
        print(f"Extension: {info['extension']}")
        print(f"Modified: {info['modified']}")
    print()

    # Example 6: Copy files
    print("Example 6: Copying files")
    print("-" * 50)
    task.copy_file("config.json", "build/config.json")
    task.copy_file("README.md", "docs/README.md")
    print()

    # Example 7: Search for files
    print("Example 7: Searching for files")
    print("-" * 50)
    json_files = task.search_files("*.json")
    print(f"JSON files: {json_files}")

    py_files = task.search_files("*.py")
    print(f"Python files: {py_files}")

    md_files = task.search_files("*.md")
    print(f"Markdown files: {md_files}")
    print()

    # Example 8: Create a log file
    print("Example 8: Writing log entries")
    print("-" * 50)
    from datetime import datetime
    log_entries = [
        f"[{datetime.now().isoformat()}] Application started",
        f"[{datetime.now().isoformat()}] Configuration loaded",
        f"[{datetime.now().isoformat()}] Ready to process requests"
    ]
    task.write_file("application.log", "\n".join(log_entries) + "\n")
    print()

    # Display final summary
    print("=" * 50)
    print("SUMMARY")
    print("=" * 50)
    all_files = task.search_files("*")
    print(f"Total files created: {len([f for f in all_files if not task.workspace_dir.joinpath(f).is_dir()])}")
    print(f"Total operations: {len(task.results)}")
    print(f"Successful operations: {len([r for r in task.results if r['status'] == 'SUCCESS'])}")
    print(f"Failed operations: {len([r for r in task.results if r['status'] == 'ERROR'])}")
    print(f"\nWorkspace location: {task.workspace_dir.absolute()}")


if __name__ == "__main__":
    main()
