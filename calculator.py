import sys

# Python program for simple calculator
 
# Function to add two numbers
def add(num1, num2):
    output = num1 + num2
    return output
 
# Function to subtract two numbers
def subtract(num1, num2):
    output = num1 - num2
    return output
 
# Function to multiply two numbers
def multiply(num1, num2):
    output = num1 * num2
    return output
 
# Function to divide two numbers
def divide(num1, num2):
    output = num1 / num2
    return output
    

print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")

# Take Opration option from the user
select = int(sys.argv[1])

print("Operation selected by user : {}".format(select))
 

# Take input from the user

number_1 = int(sys.argv[2])

print("First input from user Number 1 : {}".format(number_1))

number_2 = int(sys.argv[3])

print("Second input from user Number 2 : {}".format(number_2))

 
if select == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))
 
elif select == 2:
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))
 
elif select == 3:
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))
 
elif select == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
else:
    print("Invalid input")
