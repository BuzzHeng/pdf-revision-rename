import os
import re
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox


# Function to extract the 8-digit number and date from the filename
def extract_info(filename):
    match = re.search(r'(\d{8}) (\d{8})', filename)
    if match:
        return match.group(1), match.group(2)
    return None, None


# Function to sort filenames by the 8-digit number and date
def sort_filenames(filenames):
    extracted_info = []
    for filename in filenames:
        number, date = extract_info(filename)
        if number and date:
            try:
                date_obj = datetime.strptime(date, '%Y%m%d')
                extracted_info.append((filename, number, date_obj))
            except ValueError as e:
                print(f"Error parsing date from filename '{filename}': {e}")

    # Sort by the 8-digit number and date
    sorted_info = sorted(extracted_info, key=lambda x: (x[1], x[2]))
    return sorted_info


# Function to add revision number postfix
def add_revision_numbers(sorted_info):
    revisions = {}
    revised_filenames = []

    for filename, number, date in sorted_info:
        if number not in revisions:
            revisions[number] = 0
        else:
            revisions[number] += 1

        revision = revisions[number]
        revised_filename = f"{filename[:-4]} R{revision}.pdf"
        revised_filenames.append(revised_filename)

    return revised_filenames


# Function to select directory using tkinter
def select_directory():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    directory = filedialog.askdirectory(title="Select Directory with PDF Files")
    return directory


# Main function
def main():
    directory = select_directory()
    if not directory:
        print("No directory selected. Exiting...")
        return

    # List all PDF files in the directory
    filenames = [f for f in os.listdir(directory) if f.endswith('.pdf')]

    # Sort filenames
    sorted_info = sort_filenames(filenames)

    # Add revision numbers
    revised_filenames = add_revision_numbers(sorted_info)

    # Rename files with revised filenames
    for original, revised in zip(sorted_info, revised_filenames):
        original_path = os.path.join(directory, original[0])
        revised_path = os.path.join(directory, revised)
        os.rename(original_path, revised_path)
        print(f"Renamed: {original_path} -> {revised_path}")

    # Show completion message
    messagebox.showinfo("Complete", "PDF Revision renaming completed.")


if __name__ == "__main__":
    main()
