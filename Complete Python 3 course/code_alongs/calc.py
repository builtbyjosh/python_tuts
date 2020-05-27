# math functions
# def add(x,y):
#     return x + y

# def sub(x,y):
#     return x - y

# def mult(x,y):
#     return x * y

# def div(x,y):
#     return x / y

# print("Select operation")
# print("1. Add, 2. Subtract, 3. Multiply, 4. Divide")
# choice = int(input("Select 1,2,3, or 4: "))

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# if choice == 1:
#     print(f'{num1} + {num2} = {add(num1,num2)}')
# elif choice == 2:
#     print(f'{num1} - {num2} = {sub(num1,num2)}')
# elif choice == 3:
#     print(f'{num1} * {num2} = {mult(num1,num2)}')
# elif choice == 4:
#     print(f'{num1} / {num2} = {div(num1,num2)}')
# else:
#     print("Wrong input")

import re

print("Our Magical Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))


    if equation == "quit":
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previouse = eval(str(previous) + equation) 
            
previous = 0
run = True

while run:
    performMath()