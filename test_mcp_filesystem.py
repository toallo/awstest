#!/usr/bin/env python3
"""
Test script for Filesystem MCP Tool Demonstration

This script tests various edge cases and error handling scenarios
to demonstrate robust filesystem MCP tool usage.
"""

import sys
from filesystem_mcp_demo import FilesystemMCPDemo


def test_error_handling():
    """Test error handling capabilities of filesystem MCP operations."""
    print("\n" + "="*60)
    print("TESTING ERROR HANDLING")
    print("="*60 + "\n")
    
    demo = FilesystemMCPDemo("/projects/sandbox/awstest/test_workspace")
    demo.setup_workspace()
    
    print("\n--- Test 1: Reading Non-existent File ---")
    content = demo.read_text_file("does_not_exist.txt")
    assert content is None, "Should return None for non-existent file"
    print("✓ Correctly handled non-existent file")
    
    print("\n--- Test 2: Reading Invalid JSON ---")
    demo.write_text_file("invalid.json", "{this is not valid json}")
    data = demo.read_json_file("invalid.json")
    assert data is None, "Should return None for invalid JSON"
    print("✓ Correctly handled invalid JSON")
    
    print("\n--- Test 3: Copying Non-existent File ---")
    success = demo.copy_file("missing.txt", "copy.txt")
    assert not success, "Should fail when source doesn't exist"
    print("✓ Correctly handled copy from non-existent source")
    
    print("\n--- Test 4: Listing Non-existent Directory ---")
    items = demo.list_directory("nonexistent_dir")
    assert items is None, "Should return None for non-existent directory"
    print("✓ Correctly handled non-existent directory")
    
    print("\n--- Test 5: Getting Info for Non-existent File ---")
    info = demo.get_file_info("phantom.txt")
    assert info is None, "Should return None for non-existent file"
    print("✓ Correctly handled file info request for non-existent file")
    
    print("\n--- Test 6: Deleting Non-existent File ---")
    success = demo.delete_file("already_gone.txt")
    assert success, "Should return True (idempotent delete)"
    print("✓ Correctly handled delete of non-existent file")
    
    # Export results
    demo.export_results("error_test_results.json")
    
    summary = demo.get_operation_summary()
    print("\n" + "="*60)
    print(f"Error Handling Tests Complete")
    print(f"Total Operations: {summary['total_operations']}")
    print(f"Errors Handled: {summary['errors']}")
    print("="*60 + "\n")
    
    return True


def test_edge_cases():
    """Test edge cases in filesystem operations."""
    print("\n" + "="*60)
    print("TESTING EDGE CASES")
    print("="*60 + "\n")
    
    demo = FilesystemMCPDemo("/projects/sandbox/awstest/edge_case_workspace")
    demo.setup_workspace()
    
    print("\n--- Test 1: Empty File Operations ---")
    demo.write_text_file("empty.txt", "")
    content = demo.read_text_file("empty.txt")
    assert content == "", "Should read empty string"
    print("✓ Correctly handled empty file")
    
    print("\n--- Test 2: Large Content ---")
    large_content = "x" * 10000
    demo.write_text_file("large.txt", large_content)
    read_content = demo.read_text_file("large.txt")
    assert len(read_content) == 10000, "Should handle large files"
    print(f"✓ Correctly handled file with {len(large_content)} characters")
    
    print("\n--- Test 3: Special Characters in Content ---")
    special_content = "Hello™ 你好 🚀 Special chars: @#$%^&*()"
    demo.write_text_file("special.txt", special_content)
    read_special = demo.read_text_file("special.txt")
    assert special_content == read_special, f"Should preserve special characters. Expected: {repr(special_content)}, Got: {repr(read_special)}"
    print("✓ Correctly handled special characters")
    
    print("\n--- Test 4: Nested Directory Creation ---")
    demo.create_directory("level1/level2/level3")
    items = demo.list_directory("level1/level2")
    assert items is not None, "Should create nested directories"
    print("✓ Correctly created nested directories")
    
    print("\n--- Test 5: File Operations in Subdirectory ---")
    demo.write_text_file("level1/nested_file.txt", "Nested content")
    nested_content = demo.read_text_file("level1/nested_file.txt")
    assert nested_content == "Nested content", "Should work with nested paths"
    print("✓ Correctly handled file operations in subdirectory")
    
    print("\n--- Test 6: Multiple Appends ---")
    demo.write_text_file("append_test.txt", "Line 1\n")
    demo.append_to_file("append_test.txt", "Line 2\n")
    demo.append_to_file("append_test.txt", "Line 3\n")
    final_content = demo.read_text_file("append_test.txt")
    assert final_content.count("\n") == 3, "Should append correctly"
    print("✓ Correctly handled multiple appends")
    
    print("\n--- Test 7: Search with No Matches ---")
    demo.write_text_file("search_test.txt", "foo bar baz")
    matches = demo.search_in_file("search_test.txt", "xyz")
    assert len(matches) == 0, "Should return empty list for no matches"
    print("✓ Correctly handled search with no matches")
    
    print("\n--- Test 8: Search with Multiple Matches ---")
    demo.write_text_file("multi_match.txt", "error here\nsome text\nerror there\nerror everywhere")
    matches = demo.search_in_file("multi_match.txt", "error")
    assert len(matches) == 3, "Should find all matches"
    print(f"✓ Correctly found {len(matches)} matches")
    
    # Export results
    demo.export_results("edge_case_results.json")
    
    summary = demo.get_operation_summary()
    print("\n" + "="*60)
    print(f"Edge Case Tests Complete")
    print(f"Success Rate: {summary['success_rate']}")
    print("="*60 + "\n")
    
    return True


def test_practical_scenarios():
    """Test practical real-world scenarios."""
    print("\n" + "="*60)
    print("TESTING PRACTICAL SCENARIOS")
    print("="*60 + "\n")
    
    demo = FilesystemMCPDemo("/projects/sandbox/awstest/practical_workspace")
    demo.setup_workspace()
    
    print("\n--- Scenario 1: Configuration File Workflow ---")
    # Create initial config
    config_v1 = {
        "version": "1.0",
        "database": {"host": "localhost", "port": 5432},
        "cache_enabled": False
    }
    demo.write_json_file("app_config.json", config_v1)
    
    # Read and update config
    config = demo.read_json_file("app_config.json")
    config["cache_enabled"] = True
    config["version"] = "1.1"
    demo.write_json_file("app_config.json", config)
    
    # Verify update
    updated_config = demo.read_json_file("app_config.json")
    assert updated_config["cache_enabled"] is True, "Config should be updated"
    print("✓ Configuration workflow successful")
    
    print("\n--- Scenario 2: Log File Management ---")
    # Create log directory structure
    demo.create_directory("logs/application")
    demo.create_directory("logs/system")
    
    # Write various logs
    demo.write_text_file("logs/application/app.log", 
        "2024-01-01 INFO Started\n2024-01-01 ERROR Failed\n")
    demo.write_text_file("logs/system/sys.log",
        "2024-01-01 DEBUG System check\n")
    
    # Search for errors across logs
    errors = demo.search_in_file("logs/application/app.log", "ERROR")
    assert len(errors) > 0, "Should find error logs"
    print(f"✓ Log management successful, found {len(errors)} error(s)")
    
    print("\n--- Scenario 3: Data Backup Workflow ---")
    # Create important data
    demo.write_text_file("important_data.txt", "Critical information")
    
    # Create backup directory
    demo.create_directory("backups")
    
    # Backup the file
    demo.copy_file("important_data.txt", "backups/important_data_backup.txt")
    
    # Verify backup
    backup_exists = demo.file_exists("backups/important_data_backup.txt")
    assert backup_exists, "Backup should exist"
    print("✓ Backup workflow successful")
    
    print("\n--- Scenario 4: Data Processing Pipeline ---")
    # Create input data
    demo.create_directory("pipeline/input")
    demo.create_directory("pipeline/output")
    
    for i in range(3):
        demo.write_text_file(f"pipeline/input/data_{i}.txt", f"Data record {i}")
    
    # Process files (simulated by copying to output)
    input_files = demo.list_directory("pipeline/input")
    for filename in input_files:
        demo.copy_file(f"pipeline/input/{filename}", 
                      f"pipeline/output/processed_{filename}")
    
    # Verify output
    output_files = demo.list_directory("pipeline/output")
    assert len(output_files) == 3, "Should process all input files"
    print(f"✓ Pipeline processed {len(output_files)} files")
    
    print("\n--- Scenario 5: File Metadata Tracking ---")
    # Create a file and track its metadata
    demo.write_text_file("tracked_file.txt", "Initial content")
    info1 = demo.get_file_info("tracked_file.txt")
    
    # Modify the file
    demo.append_to_file("tracked_file.txt", "\nAdditional content")
    info2 = demo.get_file_info("tracked_file.txt")
    
    # Verify size changed
    assert info2["size"] > info1["size"], "File size should increase"
    print("✓ Metadata tracking successful")
    
    # Export results
    demo.export_results("practical_results.json")
    
    summary = demo.get_operation_summary()
    print("\n" + "="*60)
    print(f"Practical Scenario Tests Complete")
    print(f"Success Rate: {summary['success_rate']}")
    print("="*60 + "\n")
    
    return True


def main():
    """Run all tests."""
    print("\n" + "="*70)
    print(" "*15 + "FILESYSTEM MCP TOOL TEST SUITE")
    print("="*70)
    
    try:
        # Run all test suites
        test_error_handling()
        test_edge_cases()
        test_practical_scenarios()
        
        print("\n" + "="*70)
        print(" "*20 + "ALL TESTS PASSED ✓")
        print("="*70 + "\n")
        
        return 0
    except AssertionError as e:
        print(f"\n[TEST FAILED] {str(e)}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"\n[ERROR] Unexpected error: {str(e)}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
