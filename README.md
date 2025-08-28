## Overview
This Python script reads the contents of a specified text file (e.g., `file_1.txt`) and prints each line, stripping trailing whitespace. It includes error handling for cases like a missing file or other exceptions, making it robust for basic file operations.

## Requirements
- Python 3.x (tested on Python 3.8+)
- No external dependencies required.

## How to Run
1. Save the script as `display_file.py` (or similar).
2. Ensure `file_1.txt` exists in the same directory as sample content.
3. Run the script from the command line:
   ```
   python display_file.py
   ```
   - If the file exists, it will print its contents line by line.
   - If not, it will output "File not found".

## Example Output
- If `file_1.txt` contains "Hello\nWorld":
  ```
  This is a sample text file.
  It contains multiple lines
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
