The provided README.md file is tailored for your Python script that reads and displays the content of a file (e.g., `file_1.txt`) while handling errors like file not found[1][2]. It follows standard best practices for Python project documentation, including sections for overview, usage, and testing[4][7].

```markdown
# File Content Display Script

## Overview
This Python script reads the contents of a specified text file (e.g., `file_1.txt`) and prints each line, stripping trailing whitespace. It includes error handling for cases like a missing file or other exceptions, making it robust for basic file operations.

## Requirements
- Python 3.x (tested on Python 3.8+)
- No external dependencies required.

## How to Run
1. Save the script as `display_file.py` (or similar).
2. Ensure `file_1.txt` exists in the same directory with sample content.
3. Run the script from the command line:
   ```
   python display_file.py
   ```
   - If the file exists, it will print its contents line by line.
   - If not, it will output "File not found".

## Example Output
- If `file_1.txt` contains "Hello\nWorld":
  ```
  Hello
  World
  ```
- If the file is missing:
  ```
  File not found
  ```

## Error Handling
- Catches `FileNotFoundError` specifically and prints a user-friendly message.
- Falls back to a general exception handler for unexpected issues.

## Testing
- Create or delete `file_1.txt` to test success and error paths.
- Modify the filename in the `display_file_content` call for different files.
