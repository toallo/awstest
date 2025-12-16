#!/usr/bin/env python3
"""
Test script to demonstrate error handling capabilities of FilesystemToolTask.

This script intentionally triggers various error conditions to show
how the tool handles them gracefully.
"""

from server import FilesystemToolTask


def main():
    """Test error handling scenarios."""
    
    print("=" * 70)
    print("FILESYSTEM TOOL ERROR HANDLING TESTS")
    print("=" * 70)
    print()

    task = FilesystemToolTask(workspace_dir="./test_workspace")

    # Test 1: Read non-existent file
    print("Test 1: Reading non-existent file")
    print("-" * 50)
    content = task.read_file("non_existent_file.txt")
    print(f"Result: {content}")
    print()

    # Test 2: List non-existent directory
    print("Test 2: Listing non-existent directory")
    print("-" * 50)
    contents = task.list_directory("non_existent_dir")
    print(f"Result: {contents}")
    print()

    # Test 3: Get info for non-existent file
    print("Test 3: Getting info for non-existent file")
    print("-" * 50)
    info = task.get_file_info("missing.txt")
    print(f"Result: {info}")
    print()

    # Test 4: Copy non-existent file
    print("Test 4: Copying non-existent file")
    print("-" * 50)
    success = task.copy_file("source.txt", "destination.txt")
    print(f"Result: {success}")
    print()

    # Test 5: Delete non-existent file (should not error)
    print("Test 5: Deleting non-existent file")
    print("-" * 50)
    success = task.delete_file("non_existent.txt")
    print(f"Result: {success}")
    print()

    # Test 6: Successfully create a file, then demonstrate successful operations
    print("Test 6: Valid operations after handling errors")
    print("-" * 50)
    task.write_file("test_file.txt", "This is a test.")
    content = task.read_file("test_file.txt")
    print(f"Successfully read: '{content}'")
    print()

    # Test 7: Nested directory creation (should succeed)
    print("Test 7: Creating deeply nested directories")
    print("-" * 50)
    task.create_directory("level1/level2/level3/level4")
    task.write_file("level1/level2/level3/level4/deep_file.txt", "Deep in the hierarchy")
    print()

    # Summary
    print("=" * 70)
    print("ERROR HANDLING TEST SUMMARY")
    print("=" * 70)
    print(f"Total operations attempted: {len(task.results)}")
    successful = len([r for r in task.results if r["status"] == "SUCCESS"])
    errors = len([r for r in task.results if r["status"] == "ERROR"])
    warnings = len([r for r in task.results if r["status"] == "WARNING"])
    print(f"Successful: {successful}")
    print(f"Errors (handled gracefully): {errors}")
    print(f"Warnings: {warnings}")
    print()
    print("All errors were handled gracefully without crashes!")
    print("=" * 70)


if __name__ == "__main__":
    main()
