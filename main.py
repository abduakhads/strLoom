from text_class import Text

def read_text(path: str) -> str:
    with open(path, 'r') as file:
        input_str = file.read()
    return input_str

def write_text(output_str: str, path: str) -> None:
    with open(path, 'w') as file:
        file.write(output_str)

def file_name_split(file_name: str) -> list:
    name, ext = file_name.split(".", 1)
    return [name, ext]



input_file = input("Enter the file name: ")
output_file = None

try:
    input_str = Text(read_text(input_file))
except FileNotFoundError:
    input_str = None
    print("\nError: File not found\n")
except:
    input_str = None
    print("Error")
else:
    f_name, f_ext = file_name_split(input_file)
    print("File was read successfully\n")

while input_str:
    while True:
        choice = input("\nWhat would you like to do?\n[1] Replace\n[2] Remove\n[3] Filter\n\n[s] Save changes\n[q] Quit\n>> ")
        if choice in ["1", "2", "3", "q", "s"]:
            break

    if choice == "q":
        if output_file:
            print(f"Changes saved to {output_file}")
        break

    if choice == "s":
        try:
            output_file = f"{f_name}_edited.{f_ext}"
            write_text(input_str.getText(), output_file)
        except:
            print("Error occurred")
            break
        else:
            print("Changes saved successfully")
            print(f"File: {output_file}")

    if choice == "1":
        try:
            input_str.replace(input("\nOriginal: "), input("Replacement: "))
        except:
            print("Error occurred")
            break
        else:
            print("Replaced successfully")

    if choice == "2":
        try:
            input_str.remove(input("To remove: "))
        except:
            print("Error occurred")
            break
        else:
            print("Removed successfully")

    if choice == "3":
        while True:
            try:
                n_len = int(input("\nEnter an integer number to filter by length (0 to go back)\n - negative integer to remove words which are smaller than given number\n - positive integer to remove words which are greater than given number\n>> "))
                if n_len == 0:
                    break
                input_str.filtLen(n_len, input("With what to separate filtered words: "))
            except ValueError:
                print("Must be an integer!")
            except:
                print("Error occurred")
                break
            else:
                print("Filtered successfully")
                break