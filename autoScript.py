# import os
# import re

# def find_matches_in_file(file_path, search_pattern):
#     """
#     Find lines containing the search pattern in a file, including continuation lines.

#     Args:
#         file_path (str): Path to the file.
#         search_pattern (str): Text or regex pattern to search for.

#     Returns:
#         list: List of matches with line numbers and content.
#     """
#     matches = []
#     try:
#         with open(file_path, 'r', encoding='utf-8') as f:
#             lines = f.readlines()

#         i = 0
#         while i < len(lines):
#             line = lines[i]
#             if re.search(search_pattern, line):
#                 block = [(i + 1, line.strip())]  # Line number starts from 1
#                 # Check continuation lines
#                 j = i + 1
#                 while j < len(lines):
#                     next_line = lines[j].strip()
#                     if next_line.startswith(("(", "[", "{", ".", "\\")) or next_line == "" or next_line.startswith(" "):
#                         block.append((j + 1, next_line))
#                         j += 1
#                     else:
#                         break
#                 matches.append(block)
#                 i = j - 1  # Skip to the last line of the block
#             i += 1
#     except Exception as e:
#         matches.append([(-1, f"Error reading file {file_path}: {e}")])
#     return matches


# def search_directory(directory, search_pattern, file_extension=None, output_file="output.txt"):
#     """
#     Search for a text pattern in all files of a directory and write results to a file.

#     Args:
#         directory (str): Root directory to search.
#         search_pattern (str): Text or regex pattern to search for.
#         file_extension (str): File extension filter, or None for all files.
#         output_file (str): File to save the results.
#     """
#     results = []
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             if file_extension and not file.endswith(file_extension):
#                 continue

#             file_path = os.path.join(root, file)
#             matches = find_matches_in_file(file_path, search_pattern)
#             if matches:
#                 results.append((file_path, matches))

#     # Write results to a file in proper format
#     with open(output_file, 'w', encoding='utf-8') as out:
#         for file_path, matches in results:
#             out.write(f"\nFile: {file_path}\n")
#             out.write("=" * 80 + "\n")
#             for block in matches:
#                 for line_number, content in block:
#                     if line_number == -1:
#                         out.write(f"  {content}\n")
#                     else:
#                         out.write(f"  Line {line_number}: {content}\n")
#             out.write("\n")


# # Example usage
# if __name__ == "__main__":
#     # Configure your paths and search term
#     project_dir = "/path/to/your/project"  # Replace with your project directory
#     search_term = r"old_text"  # Replace with your search text or regex
#     file_ext = ".txt"  # Specify file extension, or set to None for all files
#     output_path = "output.txt"  # File where results will be saved

#     print(f"Searching for '{search_term}' in '{project_dir}'...")
#     search_directory(project_dir, search_term, file_extension=file_ext, output_file=output_path)
#     print(f"Results saved to '{output_path}'.")


import os
import re

def find_matches_in_file(file_path, search_pattern):
    """
    Find lines containing the search pattern in a file, including continuation lines.

    Args:
        file_path (str): Path to the file.
        search_pattern (str): Text or regex pattern to search for.

    Returns:
        list: List of matches with line numbers and content.
    """
    matches = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        i = 0
        while i < len(lines):
            line = lines[i]
            if re.search(search_pattern, line):  # Matches regex or escaped literal
                block = [(i + 1, line.strip())]  # Line number starts from 1
                # Check continuation lines
                j = i + 1
                while j < len(lines):
                    next_line = lines[j].strip()
                    if next_line.startswith(("(", "[", "{", ".", "\\")) or next_line == "" or next_line.startswith(" "):
                        block.append((j + 1, next_line))
                        j += 1
                    else:
                        break
                matches.append(block)
                i = j - 1  # Skip to the last line of the block
            i += 1
    except Exception as e:
        matches.append([(-1, f"Error reading file {file_path}: {e}")])
    return matches


def search_directory(directory, search_pattern, file_extension=None, output_file="output.txt"):
    """
    Search for a text pattern in all files of a directory and write results to a file.

    Args:
        directory (str): Root directory to search.
        search_pattern (str): Text or regex pattern to search for.
        file_extension (str): File extension filter, or None for all files.
        output_file (str): File to save the results.
    """
    results = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file_extension and not file.endswith(file_extension):
                continue

            file_path = os.path.join(root, file)
            matches = find_matches_in_file(file_path, search_pattern)
            if matches:
                results.append((file_path, matches))

    # Write results to a file in proper format
    with open(output_file, 'w', encoding='utf-8') as out:
        for file_path, matches in results:
            out.write(f"\nFile: {file_path}\n")
            out.write("=" * 80 + "\n")
            for block in matches:
                for line_number, content in block:
                    if line_number == -1:
                        out.write(f"  {content}\n")
                    else:
                        out.write(f"  Line {line_number}: {content}\n")
            out.write("\n")


# Example usage
if __name__ == "__main__":
    # Configure your paths and search term
    project_dir = "/path/to/your/project"  # Replace with your project directory
    search_term = re.escape("cell_name[1:8]")  # Escapes special regex characters
    file_ext = ".txt"  # Specify file extension, or set to None for all files
    output_path = "output.txt"  # File where results will be saved

    print(f"Searching for '{search_term}' in '{project_dir}'...")
    search_directory(project_dir, search_term, file_extension=file_ext, output_file=output_path)
    print(f"Results saved to '{output_path}'.")
