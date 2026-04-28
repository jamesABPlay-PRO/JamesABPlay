# JamesABPlay Calculator

import math
import cmath

class Calculator:
    def __init__(self):
        print("Welcome to the JamesABPlay Calculator!")

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Error: Division by zero"
        return x / y

    def power(self, x, y):
        return x ** y

    def sqrt(self, x):
        return math.sqrt(x)

    def sin(self, angle):
        return math.sin(math.radians(angle))

    def cos(self, angle):
        return math.cos(math.radians(angle))

    def tan(self, angle):
        return math.tan(math.radians(angle))

    def log(self, x, base=10):
        return math.log(x, base)

    def complex_add(self, c1, c2):
        return c1 + c2

    def complex_subtract(self, c1, c2):
        return c1 - c2

    def complex_multiply(self, c1, c2):
        return c1 * c2

    def complex_divide(self, c1, c2):
        if c2 == 0:
            return "Error: Division by zero"
        return c1 / c2

if __name__ == '__main__':
    calc = Calculator()