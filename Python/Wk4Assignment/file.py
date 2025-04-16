def process_file(filename):
    """This function reads a file and writes a modified version 
        to a new file.
    """
    try:
        with open(filename, "r") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"File not found, please check the filename and try again.")
        return None

    with open("modified.txt", "w") as file:
            file.write(content.upper())
            
    print("File written successfully.")

process_file(input("Enter the filename: "))