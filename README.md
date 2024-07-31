# PDF Revision Renaming Tool

This tool sorts and renames PDF files in a selected directory by adding a revision number postfix. It uses an 8-digit number and date embedded in the filenames to determine the order.

## Features

- Extracts an 8-digit number and date from filenames.
- Sorts filenames by the extracted number and date.
- Adds revision number postfix to each filename.
- Renames PDF files in the selected directory.

## Requirements

- Python 3.x
- `tkinter` library

## How to Use

1. **Clone the Repository**

   ```sh
   git clone <repository-url>
   cd <repository-directory>

2. **Install Dependencies**

This script requires the tkinter library, which is included with most Python installations. If not, you can install it via your package manager.

3. **Run the Script**

    ```sh
    python pdf_revision_renamer.py

4. **Select Directory**

- A dialog box will appear prompting you to select the directory containing your PDF files.
- Select the directory and click "OK".

5. **Process Files**

The script will process the files, add revision numbers, and rename them.
A message box will display the completion status.

## Code Explanation

### Functions
- extract_info(filename): Extracts the 8-digit number and date from the filename using regex.
- sort_filenames(filenames): Sorts filenames by the extracted number and date.
- add_revision_numbers(sorted_info): Adds a revision number postfix to each filename.
- select_directory(): Opens a dialog to select a directory using tkinter.
- main(): The main function that coordinates the entire process.

### Main Flow
1. Select Directory: Opens a directory selection dialog.
2. List PDF Files: Lists all PDF files in the selected directory.
3. Sort Filenames: Sorts the filenames based on the extracted information.
4. Add Revision Numbers: Adds revision numbers to the sorted filenames.
5. Rename Files: Renames the original files with the revised filenames.
6. Completion Message: Displays a completion message box.


## Example:
Before Running the Script

    12345678 20230101.pdf
    12345678 20230102.pdf
    23456789 20230201.pdf
    23456789 20230202.pdf

After Running the Script

    12345678 20230101 R0.pdf
    12345678 20230102 R1.pdf
    23456789 20230201 R0.pdf
    23456789 20230202 R1.pdf

## License
This project is licensed under the MIT License. See the LICENSE file for details.

##  Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## Contact
For any questions or feedback, please open an issue in this repository.