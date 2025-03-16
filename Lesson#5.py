#----------LESSON#5 (Introduction to Control Flow)-----------------------------
#Control flow refers to the order in which statements are executed in a program. In Python, decision-making is achieved using if, elif, and else statements, along with comparison and logical operators.

#2. Comparison Operators

# Comparison operators are used to compare values and return True or False. Here are the most common ones:

# == (equal to)
# !=  (not equal to)
# >   (greater than)
# <   (less than)
# >= (greater than or equal to)
# <= (less than or equal to)

#================= Comparison Operators====================
x = 10
y = 20
print("x == y =", x == y)  # False
print("x != y =", x != y)  # True
print("x > y  =", x > y)   # False
print("x < y  =", x < y)   # True
print("x >= y =", x >= y)  # False
print("x <= y =", x <= y)  # True

# ==============Logical Operators========================
age = 25
is_student = True
if age > 18 and is_student:
    print("You are eligible for a student discount.")
if age < 12 or age > 60:
    print("You qualify for a special discount.")
if not is_student:
    print("You are not a student.")

# ---------if Statement-----------------
num = 10
if num > 0:
    print("The number is positive.")

# -----------------else Statement---------------
num = -5
if num > 0:
    print("The number is positive.")
else:
    print("The number is not positive.")

# ----------elif Statement------------------
num = 0
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# -----------Nested if Statements---------------
num = 10
if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is negative.")

# ----------Simple Calculator------------------
operation = input("Enter operation (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/' and num2 != 0:
    result = num1 / num2
else:
    result = "Invalid operation or division by zero."
print("Result:", result)

# --------Grading System----------------
def grading_system(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"
marks = float(input("Enter marks: "))
print("Grade:", grading_system(marks))

# ----------for Loop-------------------
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#---------------- for Loop with else---------------
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
else:
    print("Loop completed successfully!")

# -----------while Loop-----------------
count = 5
while count > 0:
    print("Count:", count)
    count -= 1
