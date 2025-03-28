import math

def get_input():
    """Function to take input from the user."""
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b

def add(a, b):
    return a+b

def subtract(a, b):
    pass  # To be implemented by a team member

def multiply(a, b):
    pass  # To be implemented by a team member

def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Invalid input type. Please provide numbers."


def modulus(a, b):
    return int(a % b)

def power(a, b):
    pass  # To be implemented by a team member

def square_root(a):
    pass  # To be implemented by a team member

def factorial(a):
    fact=1
    for i in range(int(a),1,-1):
        fact*=i
    return fact

def sine(a):
    pass  # To be implemented by a team member

def cosine(a):
    pass  # To be implemented by a team member

def tangent(a):
    pass  # To be implemented by a team member

def logarithm(a, b):
    pass  # To be implemented by a team member

def exponent(a):
    pass  # To be implemented by a team member

def absolute(a):
    return abs(a)

def calculator():
    print("\nWelcome to the Team Calculator!")
    a, b = get_input()  # Taking input for `a` and `b`
    #1st function
    print(f"Addition of {a} and {b} is{add(a,b)}")
    print(f"Values received: a = {a}, b = {b}")
    #4th function
    print(f"Division of {a} and {b} is {divide(a,b)}")
    #5th function
    print(f"{a} % {b} is {modulus(a,b)}")
    #8th function
    print(f"Factorial value of {a} is {factorial(a)}")
    #14th function
    print(f"Absolute value of {a} is {absolute(a)}")
    

if __name__ == "__main__":
    calculator()
