# Andrew-at
# 2023
# basic python console calculator

"""
This is a side project using some
beginner Python fundamentals (loops, error checking, ect.)
to build a calculator that uses a terminal window.
The ultimate goal is to recreate some math functions from the Python
math library without using anything from the library itself.
"""

from pathlib import Path
from square_root import *

# displays a calculator ascii graphic
txt_path1 = Path('calc_display.txt')
calc_display = txt_path1.read_text()

# displays operations in console via .txt file
txt_path2 = Path("operation_display.txt")
operation_display = txt_path2.read_text()


# operation select
def input_select():

    operation_select = int
    active = True
    while active:

        try:
            print(operation_display)
            operation_select = int(input(">: "))
        except ValueError:
            print("Error, unknown value")

        if operation_select == 1:
            addition()
        elif operation_select == 2:
            subtract()
        elif operation_select == 3:
            multiply()
        elif operation_select == 4:
            divide()
        elif operation_select == 5:
            square_root()
        elif operation_select == 0:
            active = False


# 1:
# Addition of multiple integers
def addition():

    num_list = []
    sum_total = 0

    while True:

        try:
            num_range = int(input("How many numbers do you want to add? "))
            break
        except ValueError:
            print("Error: unknown value")

    for i in range(num_range):
        while True:
            try:
                num = int(input("select a number: "))
                num_list.append(num)
                break
            except ValueError:
                print("Error: unknown value")

    for i in num_list:
        sum_total += i

    print(sum_total)


# 2:
# Subtraction
def subtract():

    while True:
        try:
            num1 = int(input("Enter a number: "))
            break
        except ValueError:
            print("Error: unknown value")

    while True:
        try:
            num2 = int(input("Enter a number to subtract by: "))
            break
        except ValueError:
            print("Error: unknown value")

    print(":", num1 - num2)


# 3: multiply
def multiply():

    while True:
        try:
            num1 = int(input("Enter a number: "))
            break
        except ValueError:
            print("Error: unknown value")

    while True:
        try:
            num2 = int(input("Enter number to multiply by: "))
            break
        except ValueError:
            print("Error: unknown value")

    print(":", num1 * num2)


# 4: divide
def divide():
    while True:
        try:
            num1 = int(input("Enter a number: "))
            break
        except ValueError:
            print("Error: unknown value")

    while True:
        try:
            num2 = int(input("Enter number to multiply by: "))
            break
        except ValueError:
            print("Error: unknown value.")

    if num2 == 0:
        print("Error: division by zero.")
    else:
        print(":", num1 / num2)

print(calc_display)
input_select()
