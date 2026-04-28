#!/usr/bin/env python3
# JamesABPlay Calculator - Scientific Calculator with Command-Line Interface

import math
import sys

class JamesABPlayCalculator:
    def __init__(self):
        self.last_result = 0
        self.pi = math.pi
        self.e = math.e
        
    # Basic Operations
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y == 0:
            raise ValueError("Error: Cannot divide by zero")
        return x / y
    
    def power(self, x, y):
        return x ** y
    
    def modulo(self, x, y):
        if y == 0:
            raise ValueError("Error: Cannot calculate modulo by zero")
        return x % y
    
    # Scientific Functions
    def sqrt(self, x):
        if x < 0:
            raise ValueError("Error: Cannot calculate square root of negative number")
        return math.sqrt(x)
    
    def factorial(self, x):
        if x < 0 or x != int(x):
            raise ValueError("Error: Factorial requires non-negative integer")
        return math.factorial(int(x))
    
    def log10(self, x):
        if x <= 0:
            raise ValueError("Error: Logarithm requires positive number")
        return math.log10(x)
    
    def log_natural(self, x):
        if x <= 0:
            raise ValueError("Error: Natural logarithm requires positive number")
        return math.log(x)
    
    def log(self, x, base=10):
        if x <= 0 or base <= 0:
            raise ValueError("Error: Logarithm requires positive numbers")
        return math.log(x, base)
    
    def abs_value(self, x):
        return abs(x)
    
    # Trigonometry (in degrees)
    def sin(self, angle_degrees):
        return math.sin(math.radians(angle_degrees))
    
    def cos(self, angle_degrees):
        return math.cos(math.radians(angle_degrees))
    
    def tan(self, angle_degrees):
        return math.tan(math.radians(angle_degrees))
    
    def asin(self, x):
        if x < -1 or x > 1:
            raise ValueError("Error: asin requires value between -1 and 1")
        return math.degrees(math.asin(x))
    
    def acos(self, x):
        if x < -1 or x > 1:
            raise ValueError("Error: acos requires value between -1 and 1")
        return math.degrees(math.acos(x))
    
    def atan(self, x):
        return math.degrees(math.atan(x))
    
    def percentage(self, value, percent):
        return (value * percent) / 100


def print_welcome():
    print("\n" + "="*50)
    print("   Welcome to JamesABPlay Calculator")
    print("   Scientific Calculator with Trigonometry")
    print("="*50 + "\n")


def print_help():
    help_text = '''
BASIC OPERATIONS:
  add <x> <y>              - Add two numbers
  sub <x> <y>              - Subtract two numbers
  mul <x> <y>              - Multiply two numbers
  div <x> <y>              - Divide two numbers
  pow <x> <y>              - Power (x^y)
  mod <x> <y>              - Modulo (remainder)

SCIENTIFIC FUNCTIONS:
  sqrt <x>                 - Square root
  fact <x>                 - Factorial
  log <x>                  - Logarithm base 10
  ln <x>                   - Natural logarithm
  abs <x>                  - Absolute value
  percent <value> <%>      - Calculate percentage

TRIGONOMETRY (angles in degrees):
  sin <angle>              - Sine
  cos <angle>              - Cosine
  tan <angle>              - Tangent
  asin <x>                 - Arc sine
  acos <x>                 - Arc cosine
  atan <x>                 - Arc tangent

CONSTANTS:
  pi                       - Value of π (3.14159...)
  e                        - Value of e (2.71828...)

OTHER COMMANDS:
  last                     - Show last result
  help                     - Show this help message
  exit / quit              - Exit calculator
    '''
    print(help_text)


def interactive_mode():
    calc = JamesABPlayCalculator()
    print_welcome()
    print("Type 'help' for available commands\n")
    
    while True:
        try:
            user_input = input(">>> ").strip()
            
            if not user_input:
                continue
            
            parts = user_input.split()
            command = parts[0].lower()
            
            # Exit commands
            if command in ['exit', 'quit']:
                print("Thank you for using JamesABPlay Calculator!")
                break
            
            # Help command
            elif command == 'help':
                print_help()
            
            # Constants
            elif command == 'pi':
                result = calc.pi
                print(f"π = {result}")
                calc.last_result = result
            
            elif command == 'e':
                result = calc.e
                print(f"e = {result}")
                calc.last_result = result
            
            # Last result
            elif command == 'last':
                print(f"Last result: {calc.last_result}")
            
            # Basic operations
            elif command == 'add' and len(parts) == 3:
                result = calc.add(float(parts[1]), float(parts[2]))
                print(f"Result: {result}")
                calc.last_result = result
            
            elif command == 'sub' and len(parts) == 3:
                result = calc.subtract(float(parts[1]), float(parts[2]))
                print(f"Result: {result}")
                calc.last_result = result
            
            elif command == 'mul' and len(parts) == 3:
                result = calc.multiply(float(parts[1]), float(parts[2]))
                print(f"Result: {result}")
                calc.last_result = result
            
            elif command == 'div' and len(parts) == 3:
                result = calc.divide(float(parts[1]), float(parts[2]))
                print(f"Result: {result}")
                calc.last_result = result
            
            elif command == 'pow' and len(parts) == 3:
                result = calc.power(float(parts[1]), float(parts[2]))
                print(f"Result: {result}")
                calc.last_result = result
            
            elif command == 'mod' and len(parts) == 3:
                result = calc.modulo(float(parts[1]), float(parts[2]))
                print(f"Result: {result}")
                calc.last_result = result
            
            # Scientific functions
            elif command == 'sqrt' and len(parts) == 2:
                result = calc.sqrt(float(parts[1]))
                print(f"Result: {result}")
                calc.last_result = result
            
            elif command == 'fact' and len(parts) == 2:
                result = calc.factorial(float(parts[1]))
                print(f"Result: {result}")
                calc.last_result = result
            
            elif command == 'log' and len(parts) == 2:
                result = calc.log10(float(parts[1]))
                print(f"Result: {result}")
                calc.last_result = result
            
            elif command == 'ln' and len(parts) == 2:
                result = calc.log_natural(float(parts[1]))
                print(f"Result: {result}")
                calc.last_result = result
            
            elif command == 'abs' and len(parts) == 2:
                result = calc.abs_value(float(parts[1]))
                print(f"Result: {result}")
                calc.last_result = result
            
            elif command == 'percent' and len(parts) == 3:
                result = calc.percentage(float(parts[1]), float(parts[2]))
                print(f"Result: {result}")
                calc.last_result = result
            
            # Trigonometry
            elif command == 'sin' and len(parts) == 2:
                result = calc.sin(float(parts[1]))
                print(f"Result: {result}")
                calc.last_result = result
            
            elif command == 'cos' and len(parts) == 2:
                result = calc.cos(float(parts[1]))
                print(f"Result: {result}")
                calc.last_result = result
            
            elif command == 'tan' and len(parts) == 2:
                result = calc.tan(float(parts[1]))
                print(f"Result: {result}")
                calc.last_result = result
            
            elif command == 'asin' and len(parts) == 2:
                result = calc.asin(float(parts[1]))
                print(f"Result: {result}°")
                calc.last_result = result
            
            elif command == 'acos' and len(parts) == 2:
                result = calc.acos(float(parts[1]))
                print(f"Result: {result}°")
                calc.last_result = result
            
            elif command == 'atan' and len(parts) == 2:
                result = calc.atan(float(parts[1]))
                print(f"Result: {result}°")
                calc.last_result = result
            
            else:
                print("Invalid command or incorrect number of arguments. Type 'help' for assistance.")
        
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == '__main__':
    interactive_mode()