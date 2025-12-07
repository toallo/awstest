#!/usr/bin/env python3
"""
Filesystem MCP Tool Demonstration

This module demonstrates practical use of the filesystem MCP (Model Context Protocol) tool
for various file operations including reading, writing, and manipulating files.

The MCP filesystem tool provides a standardized way to interact with the file system
in a controlled and secure manner, with built-in error handling and validation.
"""

import os
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Union
from datetime import datetime


class FilesystemMCPDemo:
    """
    Demonstrates filesystem MCP tool operations with practical examples.
    
    This class showcases various filesystem operations that would typically be
    performed through an MCP filesystem tool, including:
    - Reading files (text and binary)
    - Writing files (creating and updating)
    - Directory operations (listing, creating, navigating)
    - File manipulation (copying, moving, deleting)
    - Metadata operations (checking existence, getting file info)
    """
    
    def __init__(self, workspace_dir: str = "/projects/sandbox/awstest/mcp_demo_workspace"):
        """
        Initialize the filesystem MCP demo.
        
        Args:
            workspace_dir: Base directory for demonstration operations
        """
        self.workspace_dir = Path(workspace_dir)
        self.results: List[Dict] = []
        
    def log_operation(self, operation: str, status: str, details: str, data: Optional[any] = None):
        """
        Log the result of a filesystem operation.
        
        Args:
            operation: Name of the operation performed
            status: Status of the operation (SUCCESS, ERROR, WARNING)
            details: Detailed description of the operation result
            data: Optional data associated with the operation
        """
        result = {
            "timestamp": datetime.now().isoformat(),
            "operation": operation,
            "status": status,
            "details": details,
        }
        if data is not None:
            result["data"] = data
        self.results.append(result)
        print(f"[{status}] {operation}: {details}")
        
    def setup_workspace(self) -> bool:
        """
        Create the demonstration workspace directory.
        
        MCP Tool Equivalent: filesystem.create_directory()
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.workspace_dir.mkdir(parents=True, exist_ok=True)
            self.log_operation(
                "setup_workspace",
                "SUCCESS",
                f"Created workspace directory: {self.workspace_dir}"
            )
            return True
        except Exception as e:
            self.log_operation(
                "setup_workspace",
                "ERROR",
                f"Failed to create workspace: {str(e)}"
            )
            return False
            
    def write_text_file(self, filename: str, content: str) -> bool:
        """
        Write text content to a file.
        
        MCP Tool Equivalent: filesystem.write_file(path, content, encoding='utf-8')
        
        Args:
            filename: Name of the file to write
            content: Text content to write
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            filepath = self.workspace_dir / filename
            filepath.write_text(content, encoding='utf-8')
            self.log_operation(
                "write_text_file",
                "SUCCESS",
                f"Wrote {len(content)} bytes to {filename}",
                {"filepath": str(filepath), "size": len(content)}
            )
            return True
        except Exception as e:
            self.log_operation(
                "write_text_file",
                "ERROR",
                f"Failed to write {filename}: {str(e)}"
            )
            return False
            
    def read_text_file(self, filename: str) -> Optional[str]:
        """
        Read text content from a file.
        
        MCP Tool Equivalent: filesystem.read_file(path, encoding='utf-8')
        
        Args:
            filename: Name of the file to read
            
        Returns:
            str: File content if successful, None otherwise
        """
        try:
            filepath = self.workspace_dir / filename
            content = filepath.read_text(encoding='utf-8')
            self.log_operation(
                "read_text_file",
                "SUCCESS",
                f"Read {len(content)} bytes from {filename}",
                {"filepath": str(filepath), "size": len(content)}
            )
            return content
        except FileNotFoundError:
            self.log_operation(
                "read_text_file",
                "ERROR",
                f"File not found: {filename}"
            )
            return None
        except Exception as e:
            self.log_operation(
                "read_text_file",
                "ERROR",
                f"Failed to read {filename}: {str(e)}"
            )
            return None
            
    def write_json_file(self, filename: str, data: Dict) -> bool:
        """
        Write JSON data to a file.
        
        MCP Tool Equivalent: filesystem.write_file(path, json.dumps(data), encoding='utf-8')
        
        Args:
            filename: Name of the JSON file to write
            data: Dictionary data to serialize as JSON
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            filepath = self.workspace_dir / filename
            json_content = json.dumps(data, indent=2)
            filepath.write_text(json_content, encoding='utf-8')
            self.log_operation(
                "write_json_file",
                "SUCCESS",
                f"Wrote JSON data to {filename}",
                {"filepath": str(filepath), "keys": list(data.keys())}
            )
            return True
        except Exception as e:
            self.log_operation(
                "write_json_file",
                "ERROR",
                f"Failed to write JSON to {filename}: {str(e)}"
            )
            return False
            
    def read_json_file(self, filename: str) -> Optional[Dict]:
        """
        Read JSON data from a file.
        
        MCP Tool Equivalent: filesystem.read_file(path, encoding='utf-8') + json.loads()
        
        Args:
            filename: Name of the JSON file to read
            
        Returns:
            dict: Parsed JSON data if successful, None otherwise
        """
        try:
            filepath = self.workspace_dir / filename
            content = filepath.read_text(encoding='utf-8')
            data = json.loads(content)
            self.log_operation(
                "read_json_file",
                "SUCCESS",
                f"Read JSON data from {filename}",
                {"filepath": str(filepath), "keys": list(data.keys()) if isinstance(data, dict) else None}
            )
            return data
        except FileNotFoundError:
            self.log_operation(
                "read_json_file",
                "ERROR",
                f"File not found: {filename}"
            )
            return None
        except json.JSONDecodeError as e:
            self.log_operation(
                "read_json_file",
                "ERROR",
                f"Invalid JSON in {filename}: {str(e)}"
            )
            return None
        except Exception as e:
            self.log_operation(
                "read_json_file",
                "ERROR",
                f"Failed to read JSON from {filename}: {str(e)}"
            )
            return None
            
    def list_directory(self, subdir: str = "") -> Optional[List[str]]:
        """
        List files and directories in a path.
        
        MCP Tool Equivalent: filesystem.list_directory(path)
        
        Args:
            subdir: Subdirectory to list (relative to workspace)
            
        Returns:
            list: List of file/directory names if successful, None otherwise
        """
        try:
            dirpath = self.workspace_dir / subdir if subdir else self.workspace_dir
            items = [item.name for item in dirpath.iterdir()]
            self.log_operation(
                "list_directory",
                "SUCCESS",
                f"Listed {len(items)} items in {subdir or 'workspace root'}",
                {"path": str(dirpath), "items": items}
            )
            return items
        except FileNotFoundError:
            self.log_operation(
                "list_directory",
                "ERROR",
                f"Directory not found: {subdir}"
            )
            return None
        except Exception as e:
            self.log_operation(
                "list_directory",
                "ERROR",
                f"Failed to list directory {subdir}: {str(e)}"
            )
            return None
            
    def create_directory(self, dirname: str) -> bool:
        """
        Create a new directory.
        
        MCP Tool Equivalent: filesystem.create_directory(path)
        
        Args:
            dirname: Name of the directory to create
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            dirpath = self.workspace_dir / dirname
            dirpath.mkdir(parents=True, exist_ok=True)
            self.log_operation(
                "create_directory",
                "SUCCESS",
                f"Created directory: {dirname}",
                {"path": str(dirpath)}
            )
            return True
        except Exception as e:
            self.log_operation(
                "create_directory",
                "ERROR",
                f"Failed to create directory {dirname}: {str(e)}"
            )
            return False
            
    def file_exists(self, filename: str) -> bool:
        """
        Check if a file exists.
        
        MCP Tool Equivalent: filesystem.file_exists(path)
        
        Args:
            filename: Name of the file to check
            
        Returns:
            bool: True if file exists, False otherwise
        """
        filepath = self.workspace_dir / filename
        exists = filepath.exists()
        self.log_operation(
            "file_exists",
            "SUCCESS",
            f"File {'exists' if exists else 'does not exist'}: {filename}",
            {"filepath": str(filepath), "exists": exists}
        )
        return exists
        
    def get_file_info(self, filename: str) -> Optional[Dict]:
        """
        Get metadata information about a file.
        
        MCP Tool Equivalent: filesystem.get_file_info(path)
        
        Args:
            filename: Name of the file to inspect
            
        Returns:
            dict: File metadata if successful, None otherwise
        """
        try:
            filepath = self.workspace_dir / filename
            if not filepath.exists():
                self.log_operation(
                    "get_file_info",
                    "ERROR",
                    f"File not found: {filename}"
                )
                return None
                
            stat = filepath.stat()
            info = {
                "name": filepath.name,
                "path": str(filepath),
                "size": stat.st_size,
                "is_file": filepath.is_file(),
                "is_directory": filepath.is_dir(),
                "created": datetime.fromtimestamp(stat.st_ctime).isoformat(),
                "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                "accessed": datetime.fromtimestamp(stat.st_atime).isoformat(),
            }
            self.log_operation(
                "get_file_info",
                "SUCCESS",
                f"Retrieved info for {filename}",
                info
            )
            return info
        except Exception as e:
            self.log_operation(
                "get_file_info",
                "ERROR",
                f"Failed to get info for {filename}: {str(e)}"
            )
            return None
            
    def copy_file(self, source: str, destination: str) -> bool:
        """
        Copy a file from source to destination.
        
        MCP Tool Equivalent: filesystem.copy_file(source_path, dest_path)
        
        Args:
            source: Source filename
            destination: Destination filename
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            src_path = self.workspace_dir / source
            dst_path = self.workspace_dir / destination
            
            if not src_path.exists():
                self.log_operation(
                    "copy_file",
                    "ERROR",
                    f"Source file not found: {source}"
                )
                return False
                
            content = src_path.read_bytes()
            dst_path.write_bytes(content)
            
            self.log_operation(
                "copy_file",
                "SUCCESS",
                f"Copied {source} to {destination}",
                {"source": str(src_path), "destination": str(dst_path), "size": len(content)}
            )
            return True
        except Exception as e:
            self.log_operation(
                "copy_file",
                "ERROR",
                f"Failed to copy {source} to {destination}: {str(e)}"
            )
            return False
            
    def delete_file(self, filename: str) -> bool:
        """
        Delete a file.
        
        MCP Tool Equivalent: filesystem.delete_file(path)
        
        Args:
            filename: Name of the file to delete
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            filepath = self.workspace_dir / filename
            
            if not filepath.exists():
                self.log_operation(
                    "delete_file",
                    "WARNING",
                    f"File does not exist (already deleted?): {filename}"
                )
                return True
                
            filepath.unlink()
            self.log_operation(
                "delete_file",
                "SUCCESS",
                f"Deleted file: {filename}",
                {"filepath": str(filepath)}
            )
            return True
        except Exception as e:
            self.log_operation(
                "delete_file",
                "ERROR",
                f"Failed to delete {filename}: {str(e)}"
            )
            return False
            
    def append_to_file(self, filename: str, content: str) -> bool:
        """
        Append content to an existing file.
        
        MCP Tool Equivalent: filesystem.read_file() + filesystem.write_file()
        
        Args:
            filename: Name of the file to append to
            content: Content to append
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            filepath = self.workspace_dir / filename
            
            # Read existing content if file exists
            existing_content = ""
            if filepath.exists():
                existing_content = filepath.read_text(encoding='utf-8')
            
            # Append new content
            new_content = existing_content + content
            filepath.write_text(new_content, encoding='utf-8')
            
            self.log_operation(
                "append_to_file",
                "SUCCESS",
                f"Appended {len(content)} bytes to {filename}",
                {"filepath": str(filepath), "appended_size": len(content), "total_size": len(new_content)}
            )
            return True
        except Exception as e:
            self.log_operation(
                "append_to_file",
                "ERROR",
                f"Failed to append to {filename}: {str(e)}"
            )
            return False
            
    def search_in_file(self, filename: str, search_term: str) -> Optional[List[Dict]]:
        """
        Search for a term in a file and return matching lines.
        
        MCP Tool Equivalent: filesystem.read_file() + custom search logic
        
        Args:
            filename: Name of the file to search
            search_term: Term to search for
            
        Returns:
            list: List of matching lines with line numbers, None if error
        """
        try:
            filepath = self.workspace_dir / filename
            
            if not filepath.exists():
                self.log_operation(
                    "search_in_file",
                    "ERROR",
                    f"File not found: {filename}"
                )
                return None
                
            content = filepath.read_text(encoding='utf-8')
            lines = content.split('\n')
            
            matches = []
            for line_num, line in enumerate(lines, 1):
                if search_term in line:
                    matches.append({
                        "line_number": line_num,
                        "content": line.strip(),
                        "position": line.index(search_term)
                    })
            
            self.log_operation(
                "search_in_file",
                "SUCCESS",
                f"Found {len(matches)} matches for '{search_term}' in {filename}",
                {"filepath": str(filepath), "matches": matches}
            )
            return matches
        except Exception as e:
            self.log_operation(
                "search_in_file",
                "ERROR",
                f"Failed to search in {filename}: {str(e)}"
            )
            return None
            
    def get_operation_summary(self) -> Dict:
        """
        Get a summary of all operations performed.
        
        Returns:
            dict: Summary statistics of operations
        """
        total = len(self.results)
        success = sum(1 for r in self.results if r["status"] == "SUCCESS")
        errors = sum(1 for r in self.results if r["status"] == "ERROR")
        warnings = sum(1 for r in self.results if r["status"] == "WARNING")
        
        summary = {
            "total_operations": total,
            "successful": success,
            "errors": errors,
            "warnings": warnings,
            "success_rate": f"{(success/total*100):.1f}%" if total > 0 else "0%"
        }
        
        return summary
        
    def export_results(self, filename: str = "operation_results.json") -> bool:
        """
        Export all operation results to a JSON file.
        
        Args:
            filename: Name of the file to export to
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            summary = self.get_operation_summary()
            export_data = {
                "summary": summary,
                "operations": self.results
            }
            
            filepath = self.workspace_dir / filename
            json_content = json.dumps(export_data, indent=2)
            filepath.write_text(json_content, encoding='utf-8')
            
            print(f"\n{'='*60}")
            print(f"Operation Summary:")
            print(f"{'='*60}")
            for key, value in summary.items():
                print(f"  {key.replace('_', ' ').title()}: {value}")
            print(f"{'='*60}")
            print(f"Full results exported to: {filepath}")
            
            return True
        except Exception as e:
            print(f"Failed to export results: {str(e)}")
            return False


def run_demonstration():
    """
    Run a comprehensive demonstration of filesystem MCP tool operations.
    """
    print("\n" + "="*60)
    print("FILESYSTEM MCP TOOL DEMONSTRATION")
    print("="*60 + "\n")
    
    demo = FilesystemMCPDemo()
    
    # Setup workspace
    print("\n--- Phase 1: Workspace Setup ---")
    demo.setup_workspace()
    
    # Writing files
    print("\n--- Phase 2: Writing Files ---")
    demo.write_text_file("hello.txt", "Hello, MCP Filesystem Tool!\nThis is a demonstration.")
    demo.write_text_file("notes.txt", "Note 1: MCP tools provide standardized interfaces.\n")
    demo.write_json_file("config.json", {
        "application": "MCP Filesystem Demo",
        "version": "1.0.0",
        "features": ["read", "write", "list", "search"],
        "enabled": True
    })
    
    # Reading files
    print("\n--- Phase 3: Reading Files ---")
    content = demo.read_text_file("hello.txt")
    if content:
        print(f"  Content preview: {content[:50]}...")
    
    config = demo.read_json_file("config.json")
    if config:
        print(f"  Config application: {config.get('application')}")
    
    # Directory operations
    print("\n--- Phase 4: Directory Operations ---")
    demo.create_directory("logs")
    demo.create_directory("data/input")
    demo.list_directory()
    
    # File information
    print("\n--- Phase 5: File Metadata ---")
    demo.get_file_info("hello.txt")
    demo.file_exists("hello.txt")
    demo.file_exists("nonexistent.txt")
    
    # File manipulation
    print("\n--- Phase 6: File Manipulation ---")
    demo.copy_file("hello.txt", "hello_backup.txt")
    demo.append_to_file("notes.txt", "Note 2: Error handling is crucial for robust applications.\n")
    demo.append_to_file("notes.txt", "Note 3: Always validate file operations.\n")
    
    # Advanced operations
    print("\n--- Phase 7: Advanced Operations ---")
    demo.write_text_file("logs/app.log", 
        "2024-01-15 10:00:00 INFO Application started\n"
        "2024-01-15 10:00:05 DEBUG Initializing filesystem\n"
        "2024-01-15 10:00:10 INFO Filesystem ready\n"
        "2024-01-15 10:00:15 ERROR Connection timeout\n"
        "2024-01-15 10:00:20 INFO Retrying connection\n"
    )
    demo.search_in_file("logs/app.log", "ERROR")
    
    # Cleanup demonstration
    print("\n--- Phase 8: Cleanup Operations ---")
    demo.delete_file("hello_backup.txt")
    
    # Export results
    print("\n--- Phase 9: Export Results ---")
    demo.export_results()
    
    print("\n" + "="*60)
    print("DEMONSTRATION COMPLETE")
    print("="*60 + "\n")
    
    return demo


if __name__ == "__main__":
    try:
        demo = run_demonstration()
        sys.exit(0)
    except Exception as e:
        print(f"\n[FATAL ERROR] Demonstration failed: {str(e)}", file=sys.stderr)
        sys.exit(1)
