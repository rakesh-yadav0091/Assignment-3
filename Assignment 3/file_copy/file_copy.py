# This program copies the contents of one text file and writes them into another text file.

def copy_file(source, destination):
    try:
        with open(source, 'r') as src_file:
            content = src_file.read()

        with open(destination, 'w') as dest_file:
            dest_file.write(content)

        print(f"Contents copied sucessfully from '{source}' to '{destination}'.")

    except FileNotFoundError:
        print("Source file not found. Please check the file name.")

# Get file names from user
source_file = input("Enter the source file name (e.g., source.txt): ")
destination_file = input("Enter the destination file name (e.g., copy.txt): ")

copy_file(source_file, destination_file)