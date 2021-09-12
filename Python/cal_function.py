# Python program to calculate for scientific calculator using python console :)

import math

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def exponent(num1, num2):
    return num1 ** num2

#def reaminder(num1, num2):
#    return num1 % num2

def remainder(num1, num2):
    return math.remainder(num1, num2)

def tangent(num):
    return math.tan(num)

def sine(num):
    return math.sin(num)

def cosine(num):
    return math.cos(num)

def factorial(num):
    return math.factorial(num)

def logarithm(num):
    return math.log(num)

def squareroot(num):
    return math.sqrt(num)

def power(num1, num2):
    return math.pow(num1, num2)

def radians(num):
    return math.radians(num)

def degrees(num):
    return math.degrees(num)

print("""
Please select operation - 
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exponent
6. Remainder
7. Tangent
8. Sine
9. Cosine
10. Factorial
11. Logarithm
12. Square root
13. Power
14. Radians
15. Degrees
""")

while True:
    select = input("Select operations from 1 - 15 : ")

    if select in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', 'c'):
        if select == 'c':
            print("Thanks for using our calculator")
            break
        elif select == '1':
            number_1 = int(input("Enter first number: "))
            number_2 = int(input("Enter second number: "))
            print(number_1, "+", number_2, "=",
                    add(number_1 , number_2))

        elif select == '2':
            number_1 = int(input("Enter first number: "))
            number_2 = int(input("Enter second number: "))
            print(number_1, "-", number_2, "=",
                    subtract(number_1 , number_2))

        elif select == '3':
            number_1 = int(input("Enter first number: "))
            number_2 = int(input("Enter second number: "))
            print(number_1, "*", number_2, "=",
                    multiply(number_1 , number_2))

        elif select == '4':
            number_1 = int(input("Enter first number: "))
            number_2 = int(input("Enter second number: "))
            print(number_1, "/", number_2, "=",
                    divide(number_1 , number_2))

        elif select == '5':
            number_1 = int(input("Enter first number: "))
            number_2 = int(input("Enter second number: "))
            print(number_1, "**", number_2, "=",
                    exponent(number_1 , number_2))

            #elif select == 6:
            #    number_1 = int(input("Enter first number: "))
            #    number_2 = int(input("Enter second number: "))
            #    print(number_1, "%", number_2, "=",
            #          remainder(number_1 , number_2))

        elif select == '6':
            number_1 = int(input("Enter first number: "))
            number_2 = int(input("Enter second number: "))
            print(remainder(number_1, number_2))

        elif select == '7':
            number = float(input("Enter number: "))
            print(tangent(number))

        elif select == '8':
            number = float(input("Enter number: "))
            print(sine(number))

        elif select == '9':
            number = float(input("Enter number: "))
            print(cosine(number))

        elif select == '10':
            number = float(input("Enter number: "))
            print(factorial(number))

        elif select == '11':
           number = float(input("Enter number: "))
           print(logarithm(number))

        elif select == '12':
            number = float(input("Enter number: "))
            print(squareroot(number))

        elif select == '13':
            number_1 = int(input("Enter first number: "))
            number_2 = int(input("Enter second number: "))
            print(power(number_1, number_2))

        elif select == '14':
            number = float(input("Enter number: "))
            print(radians(number))
                
        elif select == '15':
            number = float(input("Enter number: "))
            print(degrees(number))
            continue
        else:
            print("Invalid input")
            break
