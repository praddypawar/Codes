import re
import os

def read_changes(output_file):
    """Reads the changes from the output.txt file and organizes them by file."""
    file_changes = {}
    current_file = None
    
    with open(output_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Parse each line in the output file
    for line in lines:
        if line.startswith("File:"):
            # Extract the file path from the line
            current_file = line.strip().replace("File: ", "")
            file_changes[current_file] = []
        elif line.startswith("  Line"):
            # Match lines like: '  Line 77: print("called predict api..")'
            match = re.match(r"  Line (\d+): (.+)", line.strip())
            if match:
                line_number = int(match.group(1))  # Extract line number
                content = match.group(2)  # Extract content of the line
                # Add to the corresponding file's changes list
                file_changes[current_file].append((line_number, content))

    return file_changes

def apply_changes(file_path, changes):
    """Applies changes from the changes list to the given file."""
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return
    
    try:
        with open(file_path, 'r+', encoding='utf-8') as file:
            lines = file.readlines()
            
            # Apply changes to lines based on the changes list
            for line_num, new_content in changes:
                print(line_num, new_content)
                if line_num <= len(lines):
                    print(f"Before change at line {line_num}: {lines[line_num - 1].strip()}")
                    
                    # If 'DELETE' is specified, remove the line
                    if new_content == 'DELETE':
                        print(f"Deleting line {line_num}: {lines[line_num - 1].strip()}")
                        lines.pop(line_num - 1)
                    else:
                        # Otherwise, update the line with the new content
                        lines[line_num - 1] = new_content + "\n"
                        print(f"After change at line {line_num}: {lines[line_num - 1].strip()}")
            
            # Write the modified lines back to the file
            file.seek(0)
            file.writelines(lines)
            print(f"Changes applied successfully to {file_path}!")
    except Exception as e:
        print(f"Error applying changes to {file_path}: {e}")

def main():
    output_file = 'output.txt'  # Path to your output.txt
    
    # Step 1: Read changes from the output.txt file
    file_changes = read_changes(output_file)

    # Step 2: Apply the changes to each file listed in output.txt
    for file_path, changes in file_changes.items():
        print(f"\nApplying changes to file: {file_path}")
        apply_changes(file_path, changes)

if __name__ == "__main__":
    main()
