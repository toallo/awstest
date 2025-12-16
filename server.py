"""
Filesystem Tool Task Implementation

This module demonstrates practical filesystem tool capabilities including:
- Reading files from the filesystem
- Writing files to the filesystem
- Listing directory contents
- Creating directories
- Handling file paths appropriately
- Proper error handling for filesystem operations

Usage:
    python server.py

The script will execute a series of filesystem operations demonstrating
various capabilities.
"""

import os
import json
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional


class FilesystemToolTask:
    """
    A comprehensive filesystem tool task that demonstrates various filesystem operations.
    """

    def __init__(self, workspace_dir: str = "./filesystem_workspace"):
        """
        Initialize the FilesystemToolTask.

        Args:
            workspace_dir: Base directory for filesystem operations
        """
        self.workspace_dir = Path(workspace_dir)
        self.results = []

    def log_result(self, operation: str, status: str, details: str):
        """Log operation results."""
        result = {
            "timestamp": datetime.now().isoformat(),
            "operation": operation,
            "status": status,
            "details": details
        }
        self.results.append(result)
        print(f"[{status}] {operation}: {details}")

    def create_directory(self, dir_path: str) -> bool:
        """
        Create a directory if it doesn't exist.

        Args:
            dir_path: Path to the directory to create

        Returns:
            True if successful, False otherwise
        """
        try:
            full_path = self.workspace_dir / dir_path
            full_path.mkdir(parents=True, exist_ok=True)
            self.log_result(
                "CREATE_DIRECTORY",
                "SUCCESS",
                f"Created directory: {full_path}"
            )
            return True
        except Exception as e:
            self.log_result(
                "CREATE_DIRECTORY",
                "ERROR",
                f"Failed to create directory {dir_path}: {str(e)}"
            )
            return False

    def write_file(self, file_path: str, content: str, mode: str = 'w') -> bool:
        """
        Write content to a file.

        Args:
            file_path: Path to the file to write
            content: Content to write to the file
            mode: Write mode ('w' for text, 'wb' for binary)

        Returns:
            True if successful, False otherwise
        """
        try:
            full_path = self.workspace_dir / file_path
            # Ensure parent directory exists
            full_path.parent.mkdir(parents=True, exist_ok=True)

            with open(full_path, mode) as f:
                f.write(content)

            self.log_result(
                "WRITE_FILE",
                "SUCCESS",
                f"Wrote {len(content)} characters to {full_path}"
            )
            return True
        except Exception as e:
            self.log_result(
                "WRITE_FILE",
                "ERROR",
                f"Failed to write to {file_path}: {str(e)}"
            )
            return False

    def read_file(self, file_path: str, mode: str = 'r') -> Optional[str]:
        """
        Read content from a file.

        Args:
            file_path: Path to the file to read
            mode: Read mode ('r' for text, 'rb' for binary)

        Returns:
            File content if successful, None otherwise
        """
        try:
            full_path = self.workspace_dir / file_path

            if not full_path.exists():
                self.log_result(
                    "READ_FILE",
                    "ERROR",
                    f"File not found: {full_path}"
                )
                return None

            with open(full_path, mode) as f:
                content = f.read()

            self.log_result(
                "READ_FILE",
                "SUCCESS",
                f"Read {len(content)} characters from {full_path}"
            )
            return content
        except Exception as e:
            self.log_result(
                "READ_FILE",
                "ERROR",
                f"Failed to read {file_path}: {str(e)}"
            )
            return None

    def list_directory(self, dir_path: str = ".") -> Optional[List[Dict]]:
        """
        List contents of a directory.

        Args:
            dir_path: Path to the directory to list

        Returns:
            List of directory contents with metadata, None if error
        """
        try:
            full_path = self.workspace_dir / dir_path

            if not full_path.exists():
                self.log_result(
                    "LIST_DIRECTORY",
                    "ERROR",
                    f"Directory not found: {full_path}"
                )
                return None

            contents = []
            for item in full_path.iterdir():
                item_info = {
                    "name": item.name,
                    "type": "directory" if item.is_dir() else "file",
                    "size": item.stat().st_size if item.is_file() else None,
                    "modified": datetime.fromtimestamp(item.stat().st_mtime).isoformat()
                }
                contents.append(item_info)

            self.log_result(
                "LIST_DIRECTORY",
                "SUCCESS",
                f"Listed {len(contents)} items in {full_path}"
            )
            return contents
        except Exception as e:
            self.log_result(
                "LIST_DIRECTORY",
                "ERROR",
                f"Failed to list directory {dir_path}: {str(e)}"
            )
            return None

    def copy_file(self, src_path: str, dest_path: str) -> bool:
        """
        Copy a file from source to destination.

        Args:
            src_path: Source file path
            dest_path: Destination file path

        Returns:
            True if successful, False otherwise
        """
        try:
            src_full = self.workspace_dir / src_path
            dest_full = self.workspace_dir / dest_path

            if not src_full.exists():
                self.log_result(
                    "COPY_FILE",
                    "ERROR",
                    f"Source file not found: {src_full}"
                )
                return False

            # Ensure destination directory exists
            dest_full.parent.mkdir(parents=True, exist_ok=True)

            shutil.copy2(src_full, dest_full)
            self.log_result(
                "COPY_FILE",
                "SUCCESS",
                f"Copied {src_full} to {dest_full}"
            )
            return True
        except Exception as e:
            self.log_result(
                "COPY_FILE",
                "ERROR",
                f"Failed to copy {src_path} to {dest_path}: {str(e)}"
            )
            return False

    def delete_file(self, file_path: str) -> bool:
        """
        Delete a file.

        Args:
            file_path: Path to the file to delete

        Returns:
            True if successful, False otherwise
        """
        try:
            full_path = self.workspace_dir / file_path

            if not full_path.exists():
                self.log_result(
                    "DELETE_FILE",
                    "WARNING",
                    f"File not found (already deleted?): {full_path}"
                )
                return True

            full_path.unlink()
            self.log_result(
                "DELETE_FILE",
                "SUCCESS",
                f"Deleted file: {full_path}"
            )
            return True
        except Exception as e:
            self.log_result(
                "DELETE_FILE",
                "ERROR",
                f"Failed to delete {file_path}: {str(e)}"
            )
            return False

    def get_file_info(self, file_path: str) -> Optional[Dict]:
        """
        Get detailed information about a file.

        Args:
            file_path: Path to the file

        Returns:
            Dictionary with file information, None if error
        """
        try:
            full_path = self.workspace_dir / file_path

            if not full_path.exists():
                self.log_result(
                    "GET_FILE_INFO",
                    "ERROR",
                    f"File not found: {full_path}"
                )
                return None

            stat = full_path.stat()
            info = {
                "name": full_path.name,
                "path": str(full_path),
                "size": stat.st_size,
                "created": datetime.fromtimestamp(stat.st_ctime).isoformat(),
                "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                "is_file": full_path.is_file(),
                "is_directory": full_path.is_dir(),
                "extension": full_path.suffix
            }

            self.log_result(
                "GET_FILE_INFO",
                "SUCCESS",
                f"Retrieved info for {full_path}"
            )
            return info
        except Exception as e:
            self.log_result(
                "GET_FILE_INFO",
                "ERROR",
                f"Failed to get info for {file_path}: {str(e)}"
            )
            return None

    def search_files(self, pattern: str, search_dir: str = ".") -> Optional[List[str]]:
        """
        Search for files matching a pattern.

        Args:
            pattern: File pattern to search for (e.g., "*.txt")
            search_dir: Directory to search in

        Returns:
            List of matching file paths, None if error
        """
        try:
            full_path = self.workspace_dir / search_dir
            matches = list(full_path.glob(f"**/{pattern}"))
            relative_matches = [str(m.relative_to(self.workspace_dir)) for m in matches]

            self.log_result(
                "SEARCH_FILES",
                "SUCCESS",
                f"Found {len(relative_matches)} files matching '{pattern}'"
            )
            return relative_matches
        except Exception as e:
            self.log_result(
                "SEARCH_FILES",
                "ERROR",
                f"Failed to search for '{pattern}': {str(e)}"
            )
            return None

    def run_demonstration(self):
        """
        Run a comprehensive demonstration of filesystem tool capabilities.
        """
        print("=" * 70)
        print("FILESYSTEM TOOL TASK DEMONSTRATION")
        print("=" * 70)
        print()

        # 1. Create workspace directory structure
        print("Step 1: Creating directory structure...")
        self.create_directory("data")
        self.create_directory("logs")
        self.create_directory("config")
        self.create_directory("backups")
        print()

        # 2. Write various types of files
        print("Step 2: Writing files...")
        self.write_file(
            "data/sample.txt",
            "This is a sample text file.\nIt demonstrates writing text data.\n"
        )
        self.write_file(
            "config/settings.json",
            json.dumps({
                "app_name": "Filesystem Tool Demo",
                "version": "1.0.0",
                "debug": True,
                "max_file_size": 1048576
            }, indent=2)
        )
        self.write_file(
            "logs/app.log",
            f"[{datetime.now().isoformat()}] Application started\n"
            f"[{datetime.now().isoformat()}] Filesystem operations initialized\n"
        )
        self.write_file(
            "data/notes.md",
            "# Notes\n\n## Filesystem Operations\n\n- Read\n- Write\n- List\n- Delete\n"
        )
        print()

        # 3. Read files
        print("Step 3: Reading files...")
        content = self.read_file("data/sample.txt")
        if content:
            print(f"   Content preview: {content[:50]}...")

        config = self.read_file("config/settings.json")
        if config:
            print(f"   Config loaded: {len(config)} bytes")
        print()

        # 4. List directory contents
        print("Step 4: Listing directory contents...")
        for dir_name in ["data", "config", "logs"]:
            contents = self.list_directory(dir_name)
            if contents:
                print(f"   {dir_name}/:")
                for item in contents:
                    print(f"      - {item['name']} ({item['type']}, {item.get('size', 'N/A')} bytes)")
        print()

        # 5. Get file information
        print("Step 5: Getting file information...")
        info = self.get_file_info("config/settings.json")
        if info:
            print(f"   File: {info['name']}")
            print(f"   Size: {info['size']} bytes")
            print(f"   Modified: {info['modified']}")
        print()

        # 6. Copy files
        print("Step 6: Copying files...")
        self.copy_file("data/sample.txt", "backups/sample_backup.txt")
        self.copy_file("config/settings.json", "backups/settings_backup.json")
        print()

        # 7. Search for files
        print("Step 7: Searching for files...")
        txt_files = self.search_files("*.txt")
        print(f"   Text files found: {txt_files}")
        json_files = self.search_files("*.json")
        print(f"   JSON files found: {json_files}")
        print()

        # 8. Write summary report
        print("Step 8: Writing summary report...")
        summary = {
            "execution_time": datetime.now().isoformat(),
            "total_operations": len(self.results),
            "successful_operations": len([r for r in self.results if r["status"] == "SUCCESS"]),
            "failed_operations": len([r for r in self.results if r["status"] == "ERROR"]),
            "operations": self.results
        }
        self.write_file("logs/execution_summary.json", json.dumps(summary, indent=2))
        print()

        # 9. Display final statistics
        print("=" * 70)
        print("EXECUTION SUMMARY")
        print("=" * 70)
        print(f"Total operations: {summary['total_operations']}")
        print(f"Successful: {summary['successful_operations']}")
        print(f"Failed: {summary['failed_operations']}")
        print(f"Workspace: {self.workspace_dir.absolute()}")
        print()

        # List all files created
        all_files = self.search_files("*")
        if all_files:
            print(f"Files created ({len(all_files)}):")
            for file in sorted(all_files):
                print(f"   - {file}")
        print()
        print("=" * 70)


def main():
    """Main entry point for the filesystem tool task."""
    try:
        # Create and run the filesystem tool task
        task = FilesystemToolTask()
        task.run_demonstration()

        print("\nFilesystem tool task completed successfully!")
        print(f"Check the '{task.workspace_dir}' directory to see all created files.")

    except KeyboardInterrupt:
        print("\n\nTask interrupted by user.")
    except Exception as e:
        print(f"\n\nUnexpected error: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
