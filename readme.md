# Text Manipulation Tool (String Loom)

This is a simple Python command-line tool for performing various operations on text files, such as replacement, removal, and filtering based on word length.

## Features

- **Replace**: Replace occurrences of a specific string with another string.
- **Remove**: Remove occurrences of a specific string from the text.
- **Filter by Length**: Filter words based on their length, keeping only those that meet the specified criteria.

## Requirements

- Python 3.x

## Installation

1. Clone the repository to your local machine:

   ```sh
   git clone https://github.com/abduakhads/strLoom.git
   ```

2. Navigate to the project directory:

   ```sh
   cd strLoom
   ```

## Usage

1. Run the main script `main.py`:

   ```sh
   python main.py
   ```

2. You will be prompted to enter the name of the input file.

3. Choose from the available options to manipulate the text:

   - [1] Replace
   - [2] Remove
   - [3] Filter
   - [s] Save changes
   - [q] Quit

4. Follow the on-screen instructions to perform the desired operation.

5. If you choose to save changes (`s`), the modified text will be written to a new file with "_edited" appended to the original filename.

## Example

Suppose you have a file named `input.txt` with the following content:

```
Hello, world! This is a sample text.
```

You want to replace "world" with "universe" and filter out words longer than 4 characters.

1. Run the script and input `input.txt`.
2. Choose option [1] Replace and enter "world" as the original string and "universe" as the replacement.
3. Choose option [3] Filter and enter `4` as the maximum word length.
4. Save changes and exit the program.

The modified text will be saved to a file named `input_edited.txt`:

```
Hello, universe! This is a text.
```
