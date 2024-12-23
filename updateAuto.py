# import difflib

# def compare_files(original_file, modified_file):
#     """
#     Compare two files (original and modified) and track changes.
    
#     Args:
#         original_file (str): Path to the original file.
#         modified_file (str): Path to the modified file.
#     """
#     # Read both files
#     with open(original_file, 'r', encoding='utf-8') as f:
#         original_lines = f.readlines()

#     with open(modified_file, 'r', encoding='utf-8') as f:
#         modified_lines = f.readlines()

#     # Compare the files line by line using difflib
#     diff = difflib.unified_diff(original_lines, modified_lines, fromfile='original.txt', tofile='modified.txt')

#     # Process the diff and track changes
#     changes = []
#     for line in diff:
#         if line.startswith("+ ") or line.startswith("- "):
#             changes.append(line)
    
#     # Print the changes
#     for change in changes:
#         print(change)

#     return changes

# def update_file_with_changes(file_path, changes):
#     """
#     Update the file with the tracked changes.
    
#     Args:
#         file_path (str): Path to the file to be updated.
#         changes (list): List of changes to be applied.
#     """
#     with open(file_path, 'r', encoding='utf-8') as f:
#         lines = f.readlines()

#     for change in changes:
#         # Here you can apply changes based on your logic
#         # This example is simply printing the changes, but you can update them
#         print(f"Applying change: {change}")

#     # Optionally, write back changes to the file if needed
#     with open(file_path, 'w', encoding='utf-8') as f:
#         f.writelines(lines)
#     print(f"File '{file_path}' has been successfully updated.")

# # Example usage
# if __name__ == "__main__":
#     original_file = "output.txt"  # Path to the original file
#     modified_file = "modified_output.txt"  # Path to the modified file (with manual changes)
    
#     # Compare files and get changes
#     changes = compare_files(original_file, modified_file)
    
#     # Update the file with tracked changes
#     update_file_with_changes(original_file, changes)


# import re
# import os

# def parse_output_file(output_file):
#     """
#     Parse the output.txt file and extract file updates.
    
#     :param output_file: Path to the output.txt file.
#     :return: A dictionary where keys are file paths and values are lists of (line_number, content).
#     """
#     file_updates = {}
#     current_file = None

#     with open(output_file, 'r') as file:
#         for line in file:
#             # Check for file path
#             file_match = re.match(r'^File: (.+)$', line.strip())
#             if file_match:
#                 current_file = file_match.group(1)
#                 file_updates[current_file] = []
#                 continue

#             # Check for line updates
#             line_match = re.match(r'^\s*Line (\d+): (.+)$', line.strip())
#             if line_match and current_file:
#                 line_number = int(line_match.group(1))
#                 content = line_match.group(2)
#                 file_updates[current_file].append((line_number, content))
    
#     return file_updates


# def update_file_content_with_indentation(file_updates):
#     """
#     Update specific lines in given files while preserving indentation.
    
#     :param file_updates: Dictionary with file paths as keys and a list of tuples (line number, content) as values.
#     """
#     for file_path, updates in file_updates.items():
#         if not os.path.exists(file_path):
#             print(f"File not found: {file_path}")
#             continue
        
#         # Read the file content
#         with open(file_path, 'r') as file:
#             lines = file.readlines()
        
#         # Update specific lines
#         for line_num, new_content in updates:
#             if 0 < line_num <= len(lines):  # Ensure line number is valid
#                 # Preserve existing indentation
#                 original_line = lines[line_num - 1]
#                 indentation = re.match(r'^(\s*)', original_line).group(1)
#                 lines[line_num - 1] = f"{indentation}{new_content}\n"
#             else:
#                 print(f"Invalid line number {line_num} in file {file_path}")
        
#         # Write updated content back to the file
#         with open(file_path, 'w') as file:
#             file.writelines(lines)
#         print(f"Updated file: {file_path}")


# # Example usage
# output_file_path = "output.txt"  # Path to your output.txt file
# file_updates = parse_output_file(output_file_path)
# update_file_content_with_indentation(file_updates)



import re
import os

def parse_output_file(output_file):
    """
    Parse the output.txt file and extract file updates.

    :param output_file: Path to the output.txt file.
    :return: A dictionary where keys are file paths and values are lists of (line_number, content).
    """
    file_updates = {}
    current_file = None

    with open(output_file, 'r') as file:
        for line in file:
            # Check for file path
            file_match = re.match(r'^File: (.+)$', line.strip())
            if file_match:
                current_file = file_match.group(1)
                file_updates[current_file] = []
                continue

            # Check for line updates
            line_match = re.match(r'^\s*Line (\d+): (.*)$', line.strip())
            # print(line,"=========>",line_match)
            if line_match:
                if line_match and current_file:
                    line_number = int(line_match.group(1))
                    content = line_match.group(2)  # Keep content as-is (can be empty)
                    file_updates[current_file].append((line_number, content))
            else:
                match_number = re.search(r'\d+', line)
                if match_number:
                    number = int(match_number.group())
                    print(number,"------")
                    file_updates[current_file].append((number, ""))
               
    
    return file_updates


def update_file_content(file_updates):
    """
    Update specific lines in given files while preserving indentation and handling empty lines.

    :param file_updates: Dictionary with file paths as keys and a list of tuples (line number, content) as values.
    """
    for file_path, updates in file_updates.items():
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue

        # Read the file content
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Update specific lines
        for line_num, new_content in updates:
            if 0 < line_num <= len(lines):  # Ensure line number is valid
                original_line = lines[line_num - 1]
                indentation_match = re.match(r'^(\s*)', original_line)
                indentation = indentation_match.group(1) if indentation_match else ''
                
                # Replace with new content or clear the line
                if new_content.strip() == "":
                    lines[line_num - 1] = f"{indentation}\n"
                    print(f"Cleared Line {line_num} in {file_path}")
                else:
                    lines[line_num - 1] = f"{indentation}{new_content}\n"
                    print(f"Updated Line {line_num} in {file_path}: {lines[line_num - 1].strip()}")
            else:
                print(f"Invalid line number {line_num} in file {file_path}")
        
        # Write updated content back to the file
        with open(file_path, 'w') as file:
            file.writelines(lines)
        print(f"File successfully updated: {file_path}")


# Example usage
output_file_path = "output.txt"  # Path to your output.txt file
file_updates = parse_output_file(output_file_path)
# print(file_updates)
update_file_content(file_updates)
