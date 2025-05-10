# This program counts the occurrence of each word in a text file and displays the frequency of each word.

from collections import Counter

def count_word_occurrences(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read().lower()  # Convert to lowercase to count words case-insensitively
            words = text.split()  # Split text into words
            word_count = Counter(words)  # Count each word

            print("\n--- Word Frequency ---")
            for word, count in word_count.items():
                print(f"{word}: {count}")

    except FileNotFoundError:
        print("File not found. Please check the filename.")

# Get file name from user
file_name = input("Enter the file name (e.g., article.txt): ")
count_word_occurrences(file_name)