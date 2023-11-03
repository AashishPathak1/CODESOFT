# Function to add two numbers
def add(num1, num2):
	return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
	return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
	return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
	return num1 / num2

print("Please select an operation -\n" 
		"1. Add\n" 
		"2. Subtract\n" 
		"3. Multiply\n" 
		"4. Divide\n")


# Take input from the user
selection = int(input("selection operations using 1, 2, 3, 4 :"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if selection == 1:
	print("Result of Addition is :",number_1, "+", number_2, "=",add(number_1, number_2))
					

elif selection == 2:
	print("Result of Subtraction is :",number_1, "-", number_2, "=",subtract(number_1, number_2))
					

elif selection == 3:
	print("Result of Multiplication is :",number_1, "*", number_2, "=",multiply(number_1, number_2))
					

elif selection == 4:
	print("Result of Divison is :",number_1, "/", number_2, "=",divide(number_1, number_2))
					
else:
	print("Invalid input")
