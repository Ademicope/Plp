# Program accepts user input to create a list of integers
# and then pcompute and print the sum of the list.

user_list = []
user_input = input("Enter a number: ")
for i in range(int(user_input)):
    user_list.append(i)
    user_list.append(i)
print(sum(user_list))