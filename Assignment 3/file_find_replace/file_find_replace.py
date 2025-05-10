# This program finds and replaces a specific word in a text file with another word.

def find_and_replace(filename, old_word, new_word):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            
        # Replace the word
        updated_content = content.replace(old_word, new_word)
        with open(filename, 'w') as file:
            file.write(updated_content)
            
        print(f"All occurrences of '{old_word}' replaced with '{new_word}' in '{filename}'.")
        
    except FileNotFoundError:
        print("File not found. please check the filename.")

# Input from user
file_name = input("Enter the file name (e.g., notes.txt): ")
word_to_replace = input("Enter the word to replace: ")
replacement_word = input("Enter the new word: ")

find_and_replace(file_name, word_to_replace, replacement_word)