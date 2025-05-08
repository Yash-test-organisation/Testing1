import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def power(x, y):
    return math.pow(x, y)

def sqrt(x):
    return math.sqrt(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def log(x, base=10):
    return math.log(x, base)

def ln(x):
    return math.log(x)

def factorial(x):
    return math.factorial(int(x))

def scientific_calculator():
    print("=== Scientific Calculator ===")
    print("Available operations: add, subtract, multiply, divide, power, sqrt, sin, cos, tan, log, ln, factorial")
    
    while True:
        operation = input("\nEnter operation (or 'exit' to quit): ").lower()

        if operation == "exit":
            print("Exiting calculator.")
            break

        try:
            if operation in ["add", "subtract", "multiply", "divide", "power"]:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                if operation == "add":
                    print("Result:", add(x, y))
                elif operation == "subtract":
                    print("Result:", subtract(x, y))
                elif operation == "multiply":
                    print("Result:", multiply(x, y))
                elif operation == "divide":
                    print("Result:", divide(x, y))
                elif operation == "power":
                    print("Result:", power(x, y))

            elif operation in ["sqrt", "sin", "cos", "tan", "log", "ln", "factorial"]:
                x = float(input("Enter number: "))
                if operation == "sqrt":
                    print("Result:", sqrt(x))
                elif operation == "sin":
                    print("Result:", sin(x))
                elif operation == "cos":
                    print("Result:", cos(x))
                elif operation == "tan":
                    print("Result:", tan(x))
                elif operation == "log":
                    base = input("Enter base (or press enter for base 10): ")
                    base = float(base) if base else 10
                    print("Result:", log(x, base))
                elif operation == "ln":
                    print("Result:", ln(x))
                elif operation == "factorial":
                    if x < 0 or not x.is_integer():
                        print("Error! Factorial only defined for non-negative integers.")
                    else:
                        print("Result:", factorial(x))
            else:
                print("Invalid operation.")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    scientific_calculator()
