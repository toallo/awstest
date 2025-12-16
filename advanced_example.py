#!/usr/bin/env python3
"""
Advanced usage examples for FilesystemToolTask.

This script demonstrates more advanced patterns and use cases.
"""

import json
from datetime import datetime
from server import FilesystemToolTask


def backup_and_version_files(task):
    """Example: Create versioned backups of files."""
    print("Advanced Example 1: Versioned File Backups")
    print("-" * 70)
    
    # Create original files
    task.write_file("data/document.txt", "Version 1 of the document")
    task.write_file("data/config.json", json.dumps({"version": 1}, indent=2))
    
    # Create versioned backups with timestamps
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    task.copy_file("data/document.txt", f"backups/document_{timestamp}.txt")
    task.copy_file("data/config.json", f"backups/config_{timestamp}.json")
    
    # Update original files
    task.write_file("data/document.txt", "Version 2 of the document")
    task.write_file("data/config.json", json.dumps({"version": 2}, indent=2))
    
    print(f"Created versioned backups with timestamp: {timestamp}")
    print()


def organize_files_by_extension(task):
    """Example: Organize files into directories by extension."""
    print("Advanced Example 2: Organize Files by Extension")
    print("-" * 70)
    
    # Create various files
    files = {
        "report.pdf": b"PDF content",
        "image.png": b"PNG content",
        "data.csv": "name,age\nJohn,30\nJane,25",
        "script.py": "print('Hello')",
        "notes.txt": "Some notes here",
        "config.yaml": "key: value"
    }
    
    for filename, content in files.items():
        mode = 'w' if isinstance(content, str) else 'wb'
        task.write_file(f"unsorted/{filename}", content, mode=mode)
    
    # Organize by extension
    all_files = task.search_files("*", "unsorted")
    if all_files:
        for file in all_files:
            if '.' in file:
                ext = file.split('.')[-1]
                new_path = f"organized/{ext}/{file.split('/')[-1]}"
                task.copy_file(file, new_path)
    
    print("Files organized by extension")
    print()


def create_project_snapshot(task):
    """Example: Create a project snapshot with metadata."""
    print("Advanced Example 3: Project Snapshot with Metadata")
    print("-" * 70)
    
    # Create some project files
    task.write_file("project/src/main.py", "def main():\n    pass")
    task.write_file("project/src/utils.py", "def helper():\n    pass")
    task.write_file("project/tests/test_main.py", "def test_main():\n    pass")
    
    # Create snapshot metadata
    all_files = task.search_files("*", "project")
    file_metadata = []
    
    for file in all_files:
        info = task.get_file_info(file)
        if info and info['is_file']:
            file_metadata.append({
                "path": file,
                "size": info['size'],
                "modified": info['modified']
            })
    
    snapshot = {
        "created_at": datetime.now().isoformat(),
        "files": file_metadata,
        "total_files": len(file_metadata),
        "total_size": sum(f['size'] for f in file_metadata)
    }
    
    task.write_file(
        "snapshots/snapshot.json",
        json.dumps(snapshot, indent=2)
    )
    
    print(f"Created snapshot with {len(file_metadata)} files")
    print(f"Total size: {snapshot['total_size']} bytes")
    print()


def generate_directory_report(task):
    """Example: Generate a detailed directory report."""
    print("Advanced Example 4: Directory Structure Report")
    print("-" * 70)
    
    def scan_directory(dir_path, level=0):
        """Recursively scan directory and build report."""
        items = task.list_directory(dir_path)
        if not items:
            return []
        
        report_lines = []
        for item in sorted(items, key=lambda x: (x['type'] != 'directory', x['name'])):
            indent = "  " * level
            if item['type'] == 'directory':
                report_lines.append(f"{indent}📁 {item['name']}/")
                # Recursively scan subdirectories
                subdir_path = f"{dir_path}/{item['name']}" if dir_path != "." else item['name']
                report_lines.extend(scan_directory(subdir_path, level + 1))
            else:
                size = item.get('size', 0)
                size_str = f"{size:,} bytes" if size is not None else "N/A"
                report_lines.append(f"{indent}📄 {item['name']} ({size_str})")
        
        return report_lines
    
    # Generate report
    report_lines = ["# Directory Structure Report", ""]
    report_lines.append(f"Generated at: {datetime.now().isoformat()}")
    report_lines.append("")
    report_lines.extend(scan_directory("."))
    
    report_content = "\n".join(report_lines)
    task.write_file("reports/directory_report.txt", report_content)
    
    print("Generated directory structure report")
    print()


def demonstrate_batch_operations(task):
    """Example: Batch file operations."""
    print("Advanced Example 5: Batch Operations")
    print("-" * 70)
    
    # Create multiple files in batch
    file_data = [
        ("batch/file1.txt", "Content 1"),
        ("batch/file2.txt", "Content 2"),
        ("batch/file3.txt", "Content 3"),
        ("batch/subdir/file4.txt", "Content 4"),
        ("batch/subdir/file5.txt", "Content 5"),
    ]
    
    print("Creating batch files...")
    for path, content in file_data:
        task.write_file(path, content)
    
    # Batch read and process
    print("\nReading and processing batch files...")
    all_txt_files = task.search_files("*.txt", "batch")
    total_chars = 0
    for file in all_txt_files:
        content = task.read_file(file)
        if content:
            total_chars += len(content)
    
    print(f"Processed {len(all_txt_files)} files")
    print(f"Total characters: {total_chars}")
    
    # Batch backup
    print("\nCreating batch backup...")
    for file in all_txt_files:
        backup_path = file.replace("batch/", "batch_backup/")
        task.copy_file(file, backup_path)
    
    print()


def main():
    """Run all advanced examples."""
    print("=" * 70)
    print("ADVANCED FILESYSTEM TOOL EXAMPLES")
    print("=" * 70)
    print()
    
    task = FilesystemToolTask(workspace_dir="./advanced_workspace")
    
    # Run all examples
    backup_and_version_files(task)
    organize_files_by_extension(task)
    create_project_snapshot(task)
    demonstrate_batch_operations(task)
    generate_directory_report(task)
    
    # Final summary
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    all_files = task.search_files("*")
    file_count = len([f for f in all_files if not task.workspace_dir.joinpath(f).is_dir()])
    
    print(f"Total files created: {file_count}")
    print(f"Total operations: {len(task.results)}")
    print(f"Successful: {len([r for r in task.results if r['status'] == 'SUCCESS'])}")
    print(f"Workspace: {task.workspace_dir.absolute()}")
    print("=" * 70)


if __name__ == "__main__":
    main()
