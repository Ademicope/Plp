with open("input.txt", "w") as file:
    file.write("follow who know road\n")
    file.write("eni to mo way lo mo'we\n")
    file.write("a townhall different from balablu\n")
    file.write("blublu, bulaba\n")

with open("input.txt", "r") as file:
    content = file.read()

words = len(content.split())

upper_case = content.upper()

with open("output.txt", "w") as file:
    file.write(upper_case + "\n")
    file.write(f"Number of words: {words}\n")

print("File written successfully.")