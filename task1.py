# Task 1: Read a File and Handle Errors

filename = "sample.txt"

try:
    # 1. Opens and reads a text file named sample.txt
    with open(filename, "r") as file:
        print("Reading file content:")

        # 2. Prints its content line by line
        for line_num, line in enumerate(file, 1):
            print(f"Line {line_num}: {line.strip()}")

# 3. Handles errors gracefully if the file does not exist
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")