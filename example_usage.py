#!/usr/bin/env python3
"""
Example Usage: Filesystem MCP Tool Demo

This script shows practical examples of how to use the filesystem MCP tool
demonstration in your own projects.
"""

from filesystem_mcp_demo import FilesystemMCPDemo
import json


def example_1_simple_file_operations():
    """Example 1: Basic file read/write operations."""
    print("\n=== Example 1: Simple File Operations ===\n")
    
    demo = FilesystemMCPDemo("/projects/sandbox/awstest/example1_workspace")
    demo.setup_workspace()
    
    # Write a simple text file
    demo.write_text_file("greeting.txt", "Hello from MCP filesystem tool!")
    
    # Read it back
    content = demo.read_text_file("greeting.txt")
    print(f"File content: {content}")
    
    # Get file information
    info = demo.get_file_info("greeting.txt")
    print(f"File size: {info['size']} bytes")
    print(f"Created: {info['created']}")


def example_2_json_configuration():
    """Example 2: Managing JSON configuration files."""
    print("\n=== Example 2: JSON Configuration Management ===\n")
    
    demo = FilesystemMCPDemo("/projects/sandbox/awstest/example2_workspace")
    demo.setup_workspace()
    
    # Create initial configuration
    config = {
        "app_name": "MyApplication",
        "version": "1.0.0",
        "database": {
            "host": "localhost",
            "port": 5432,
            "name": "mydb"
        },
        "features": {
            "auth": True,
            "logging": True,
            "caching": False
        }
    }
    
    demo.write_json_file("config.json", config)
    print("✓ Configuration saved")
    
    # Read and modify configuration
    loaded_config = demo.read_json_file("config.json")
    loaded_config["features"]["caching"] = True
    loaded_config["version"] = "1.1.0"
    
    demo.write_json_file("config.json", loaded_config)
    print("✓ Configuration updated")
    
    # Verify changes
    final_config = demo.read_json_file("config.json")
    print(f"Caching enabled: {final_config['features']['caching']}")
    print(f"New version: {final_config['version']}")


def example_3_log_file_analysis():
    """Example 3: Analyzing log files."""
    print("\n=== Example 3: Log File Analysis ===\n")
    
    demo = FilesystemMCPDemo("/projects/sandbox/awstest/example3_workspace")
    demo.setup_workspace()
    
    # Create a sample log file
    log_entries = [
        "2024-01-15 10:00:00 INFO Application started",
        "2024-01-15 10:00:05 DEBUG Loading configuration",
        "2024-01-15 10:00:10 INFO Configuration loaded successfully",
        "2024-01-15 10:00:15 ERROR Database connection failed",
        "2024-01-15 10:00:20 WARN Retrying database connection",
        "2024-01-15 10:00:25 INFO Database connection established",
        "2024-01-15 10:00:30 ERROR Invalid user credentials",
        "2024-01-15 10:00:35 INFO User login successful",
    ]
    
    demo.write_text_file("app.log", "\n".join(log_entries))
    print("✓ Log file created")
    
    # Search for errors
    errors = demo.search_in_file("app.log", "ERROR")
    print(f"\nFound {len(errors)} errors:")
    for error in errors:
        print(f"  Line {error['line_number']}: {error['content']}")
    
    # Search for warnings
    warnings = demo.search_in_file("app.log", "WARN")
    print(f"\nFound {len(warnings)} warnings:")
    for warning in warnings:
        print(f"  Line {warning['line_number']}: {warning['content']}")


def example_4_data_backup():
    """Example 4: Creating file backups."""
    print("\n=== Example 4: Data Backup System ===\n")
    
    demo = FilesystemMCPDemo("/projects/sandbox/awstest/example4_workspace")
    demo.setup_workspace()
    
    # Create important data files
    demo.write_text_file("important_data.txt", "Critical business data")
    demo.write_json_file("user_data.json", {
        "users": [
            {"id": 1, "name": "Alice", "email": "alice@example.com"},
            {"id": 2, "name": "Bob", "email": "bob@example.com"}
        ]
    })
    
    print("✓ Created data files")
    
    # Create backup directory
    demo.create_directory("backups")
    
    # Backup files
    files_to_backup = ["important_data.txt", "user_data.json"]
    for filename in files_to_backup:
        if demo.file_exists(filename):
            backup_name = f"backup_{filename}"
            demo.copy_file(filename, f"backups/{backup_name}")
            print(f"✓ Backed up: {filename}")
    
    # List backups
    backups = demo.list_directory("backups")
    print(f"\nTotal backups created: {len(backups)}")
    for backup in backups:
        print(f"  - {backup}")


def example_5_directory_structure():
    """Example 5: Creating complex directory structures."""
    print("\n=== Example 5: Directory Structure Creation ===\n")
    
    demo = FilesystemMCPDemo("/projects/sandbox/awstest/example5_workspace")
    demo.setup_workspace()
    
    # Create a typical application directory structure
    directories = [
        "src/components",
        "src/utils",
        "src/models",
        "tests/unit",
        "tests/integration",
        "docs/api",
        "docs/guides",
        "config/dev",
        "config/prod",
        "logs",
    ]
    
    for directory in directories:
        demo.create_directory(directory)
    
    print("✓ Created directory structure")
    
    # Add sample files to the structure
    demo.write_text_file("src/components/Header.js", "// Header component")
    demo.write_text_file("src/utils/helpers.js", "// Helper functions")
    demo.write_text_file("tests/unit/test_helpers.js", "// Unit tests")
    demo.write_json_file("config/dev/settings.json", {"env": "development"})
    demo.write_json_file("config/prod/settings.json", {"env": "production"})
    
    print("✓ Added sample files")
    
    # List top-level directories
    top_level = demo.list_directory()
    print(f"\nTop-level directories: {', '.join(top_level)}")


def example_6_data_processing_pipeline():
    """Example 6: Building a data processing pipeline."""
    print("\n=== Example 6: Data Processing Pipeline ===\n")
    
    demo = FilesystemMCPDemo("/projects/sandbox/awstest/example6_workspace")
    demo.setup_workspace()
    
    # Setup pipeline directories
    demo.create_directory("pipeline/raw")
    demo.create_directory("pipeline/processed")
    demo.create_directory("pipeline/reports")
    
    # Generate sample raw data
    sample_data = [
        {"id": 1, "name": "Product A", "price": 100, "quantity": 5},
        {"id": 2, "name": "Product B", "price": 200, "quantity": 3},
        {"id": 3, "name": "Product C", "price": 150, "quantity": 8},
    ]
    
    for i, item in enumerate(sample_data, 1):
        demo.write_json_file(f"pipeline/raw/data_{i}.json", item)
    
    print(f"✓ Created {len(sample_data)} raw data files")
    
    # Process data files
    raw_files = demo.list_directory("pipeline/raw")
    processed_items = []
    
    for filename in raw_files:
        data = demo.read_json_file(f"pipeline/raw/{filename}")
        if data:
            # Process: calculate total value
            data["total_value"] = data["price"] * data["quantity"]
            demo.write_json_file(f"pipeline/processed/{filename}", data)
            processed_items.append(data)
    
    print(f"✓ Processed {len(processed_items)} files")
    
    # Generate summary report
    total_revenue = sum(item["total_value"] for item in processed_items)
    report = {
        "total_items": len(processed_items),
        "total_revenue": total_revenue,
        "items": processed_items
    }
    
    demo.write_json_file("pipeline/reports/summary.json", report)
    print(f"✓ Generated report: Total revenue = ${total_revenue}")


def example_7_error_handling():
    """Example 7: Demonstrating error handling."""
    print("\n=== Example 7: Error Handling ===\n")
    
    demo = FilesystemMCPDemo("/projects/sandbox/awstest/example7_workspace")
    demo.setup_workspace()
    
    # Attempt to read non-existent file
    print("1. Attempting to read non-existent file...")
    content = demo.read_text_file("missing.txt")
    if content is None:
        print("   → Handled gracefully: File not found")
    
    # Attempt to read invalid JSON
    print("\n2. Creating and reading invalid JSON...")
    demo.write_text_file("bad.json", "{ invalid json }")
    data = demo.read_json_file("bad.json")
    if data is None:
        print("   → Handled gracefully: Invalid JSON format")
    
    # Attempt to copy non-existent file
    print("\n3. Attempting to copy non-existent file...")
    success = demo.copy_file("phantom.txt", "copy.txt")
    if not success:
        print("   → Handled gracefully: Source file not found")
    
    # Attempt to delete non-existent file (should succeed - idempotent)
    print("\n4. Attempting to delete non-existent file...")
    success = demo.delete_file("never_existed.txt")
    if success:
        print("   → Handled gracefully: Idempotent delete operation")
    
    print("\n✓ All error scenarios handled properly")


def example_8_file_monitoring():
    """Example 8: File monitoring and metadata tracking."""
    print("\n=== Example 8: File Monitoring ===\n")
    
    demo = FilesystemMCPDemo("/projects/sandbox/awstest/example8_workspace")
    demo.setup_workspace()
    
    # Create a file
    demo.write_text_file("monitored.txt", "Initial content")
    
    # Get initial metadata
    info1 = demo.get_file_info("monitored.txt")
    print(f"Initial state:")
    print(f"  Size: {info1['size']} bytes")
    print(f"  Modified: {info1['modified']}")
    
    # Modify the file
    demo.append_to_file("monitored.txt", "\nAdditional line 1")
    demo.append_to_file("monitored.txt", "\nAdditional line 2")
    
    # Get updated metadata
    info2 = demo.get_file_info("monitored.txt")
    print(f"\nAfter modifications:")
    print(f"  Size: {info2['size']} bytes (grew by {info2['size'] - info1['size']} bytes)")
    print(f"  Modified: {info2['modified']}")
    
    # Show content
    content = demo.read_text_file("monitored.txt")
    lines = content.split('\n')
    print(f"  Lines: {len(lines)}")


def main():
    """Run all examples."""
    print("\n" + "="*70)
    print(" "*15 + "FILESYSTEM MCP TOOL - USAGE EXAMPLES")
    print("="*70)
    
    examples = [
        example_1_simple_file_operations,
        example_2_json_configuration,
        example_3_log_file_analysis,
        example_4_data_backup,
        example_5_directory_structure,
        example_6_data_processing_pipeline,
        example_7_error_handling,
        example_8_file_monitoring,
    ]
    
    for example in examples:
        try:
            example()
        except Exception as e:
            print(f"\n[ERROR] Example failed: {str(e)}")
    
    print("\n" + "="*70)
    print(" "*20 + "ALL EXAMPLES COMPLETE")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
