# This program reads a CSV file and displays its contents in a tabular format.

import csv

def display_csv(filename):
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            print("\n--- CSV File Content ---")
            for row in reader:
                print("\t".join(row)) # Tab-separated display for table format

    except FileNotFoundError:
        print("CSV file not found. please check the file name and try again.")

# Get filename from user
file_name = input("Enter the CSV file name (e.g., data.csv): ")
display_csv(file_name)