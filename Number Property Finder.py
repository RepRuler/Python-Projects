import math

class Numeral:
    def __init__(self):
        self.square = None
        self.cube = None
        self.root = None
        self.factorial = None

def start():
    while True:
        print("Welcome to Number Property Finder!")
        print("For this to work, the number has to be between 1 and 994.")
        try:
            x = float(input("Number ==> "))
            if 1 <= x <= 994:
                x_instance = Numeral()
                calculation(x, x_instance)
                print_results(x, x_instance)
            else:
                print("Number must be between 1 and 994. Please try again.")
        except ValueError:
            print("Error: You must enter a number. Please try again.")

        restart = input("Do you want to find properties for another number? (yes/no): ")
        if restart.lower() != 'yes':
            break

def calculation(x, numeral_instance):
    numeral_instance.square = x * x
    numeral_instance.cube = x * x * x
    numeral_instance.root = math.sqrt(x)
    numeral_instance.factorial = factorial(int(x))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def print_results(x, numeral_instance):
    print("\nThe Properties of", x, "are:")
    print("Square =", numeral_instance.square)
    print("Cube =", numeral_instance.cube)
    print("Square Root =", numeral_instance.root)
    print("Factorial =", numeral_instance.factorial)

start()