print("Hello :), what would you like to calculate today?")
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
operator = input("Enter operator: +, -, *, /")
answer = 0

if operator == '+':
    answer = num1 + num2
elif operator == '-':
    answer = num1 - num2
elif operator == '/':
    answer = num1 / num2
elif operator == '*':
    answer = num1 * num2
else:
    print("Invalid operator :(")

print(f"{num1} {operator} {num2} = {answer}")
