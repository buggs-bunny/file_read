## Overview
This Python script reads the contents of a specified text file (e.g., `file_1.txt`) and prints each line, stripping trailing whitespace. It includes error handling for cases like a missing file or other exceptions, making it robust for basic file operations.

## Requirements
- Python 3.x (tested on Python 3.8+)
- No external dependencies required.

## How to Run
1. Save the script as `open_file.py` (or similar).
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

- ```markdown
# Write and Append to File Script

## Overview of task 2
This Python script collects user input, writes it to a specified file (e.g., `output.txt`), appends additional input, and then displays the final contents of the file line by line. It includes basic error handling for robustness during file operations.
   ```
   python open_file2.py
   ```
3. Follow the prompts:
   - Enter initial data to write.
   - Enter additional data to append.
4. The script will create/overwrite `output.txt`, append to it, and print the final content.

## Example Output
Assuming user inputs "Hello" and then "World":

```
Enter data to write to the file: Hello
Enter additional data to append: World

Final content of the file:
Hello
World
```

## Error Handling
- Wraps all operations in a try-except block to catch and print any exceptions (e.g., permission issues or file errors).

## Testing
- Run with valid inputs to verify writing, appending, and reading.
- Test error cases by restricting file permissions or using an invalid filename.
- Check the generated `output.txt` file manually for accuracy.
