# Task 2: Write and Append Data to a File

filename = "output.txt"

# 1. Takes user input and writes it to output.txt
user_text = input("Enter text to write to the file: ")
with open(filename, "w") as file:
    file.write(user_text + "\n")
print(f"Data successfully written to {filename}.")

# 2. Appends additional data to the same file
append_text = input("Enter additional text to append: ")
with open(filename, "a") as file:
    file.write(append_text + "\n")
print("Data successfully appended.")

# 3. Reads and displays the final content of the file
print(f"\nFinal content of {filename}:")
try:
    with open(filename, "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: Could not read the file.")