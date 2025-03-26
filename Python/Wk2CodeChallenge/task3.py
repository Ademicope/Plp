# Program to store and display information about a person using a dictionary

# Create an empty dictionary to store the person's information
person_info = {}

# Get user input for the person's details
person_info['name'] = input("Enter the person's name: ")
person_info['age'] = input("Enter the person's age: ")
person_info['favorite_color'] = input("Enter the person's favorite color: ")

# Print the dictionary to the console
print("\nPerson's Information:")
print(person_info)