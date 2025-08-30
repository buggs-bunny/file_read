# task2_write_append_file.py

def write_and_append_to_file(filename):
    try:
        user_input = input("Enter data to write to the file: ")
        # Write initial user input
        with open(filename, 'w') as file:
            file.write(user_input + "\n")

        extra_input = input("Enter additional data to append: ")
        # Append extra input
        with open(filename, 'a') as file:
            file.write(extra_input + "\n")

        # Display final content
        print("\nFinal content of the file:")
        with open(filename, 'r') as file:
            for line in file:
                print(line.rstrip())

    except Exception as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    write_and_append_to_file("output.txt")