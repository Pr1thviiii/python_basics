def add(num1, num2):
    add = num1 + num2
    return add

def subtract(num1, num2):
    sub = num1 - num2
    return sub

def multiply(num1, num2):
    mul = num1 * num2
    return mul

def divide(num1, num2):
    divide = num1 / num2
    return divide

def remainder_finder(num1, num2):
    remainder_finder = num1 % num2
    return remainder_finder

def int_divison(num1, num2):
    int_divison = num1 // num2
    return int_divison

print("""___Its Prithvi's Calculator for only 2 no.'s calculation___
___________________________________________________________________________

      what you want to do

      please select the Number for your diserable operation

      1 for addition
      2 for subtraction
      3 for multiplication
      4 for division
      5 for finding remainder
      6 for integer divison """)

a = int(input("What you want to do , enter your number:"))

if a < 1 or a > 6:
    print("Invalid Input\nPlease select the number from 1 to 6 only")
    exit()


num1 = float(input("Enter first_no for operation:"))
num2 = float(input("Enter second_no for operation:"))

if a in (4, 5, 6) and num2 == 0:
    print("Error! , you cant divide by zero")
    exit()


if a == 1:
    x = add(num1, num2)
    print(x)
    
elif a == 2:
    x = subtract(num1, num2)
    print(x)

elif a == 3:
    x = multiply(num1, num2)
    print(x) 

elif a == 4:    
    x = divide(num1, num2)
    print(x)
    
elif a == 5:
    x = remainder_finder(num1, num2)
    print(x)

elif a == 6:    
    x = int_divison(num1, num2)
    print(x)












