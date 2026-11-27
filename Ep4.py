# Conditional Statements
# NOTE Indentation is very important in python

marks = int(input("Enter MArks of the Student: "))

if marks >=80:
    print('A')
elif marks < 80 and marks >= 60:
    print('B')
else: 
    print('C')











# Test
# Building a calculator 

a = float(input("Enter a value: "));
b = float(input("Enter b value: "));
operator = input("Enter the operator for operation between a and b :")

if operator == "+":
    print("Sum of a + b is :", a+b)
elif operator == "-":
    print("Subtraction a - b is :", a-b)
elif operator == "*":
    print("Multiplication of a * b is :", a*b)
elif operator == "/":
    print("Division of a / b is :", a/b)
elif operator == "**":
    print("Power of a **b is: ", a**b)
else :
    print("Invalid operator")
