# Function to add two numbers
def add(x, y):
   return x + y

# Function to subtract two numbers
def subtract(x, y):
   return x - y

# Function to multiply two numbers
def multiply(x, y):
   return x * y

# Function to divide two numbers
def divide(x, y):
   return x / y

# Prompt the user to enter the first number
num1 = float(input("Enter first number: "))

# Prompt the user to enter the second number
num2 = float(input("Enter second number: "))

# Print the available operations
print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Prompt the user to enter their choice of operation
choice = input("Enter choice (1/2/3/4): ")

# Perform the selected operation
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")