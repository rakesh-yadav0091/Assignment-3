# This program reads a text file and counts the number of lines, words, and characters in it.

def count_file_status(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            num_chars = sum(len(line) for line in lines)

            print(f"Total Lines: {num_lines}")
            print(f"Total Words: {num_words}")
            print(f"Total characters: {num_chars}")

    except FileNotFoundError:
        print("File not found. Please make sure the file exist.")

# Example usage
file_name = input("Enter the fie name (with .txt extension): ")
count_file_status(file_name)