# Arithmetic operation functions

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "❌ Error: Division by zero"
    return x / y

# Function that uses the operations
def calculate(x, y, operation):
    if operation == '+':
        return add(x, y)
    elif operation == '-':
        return subtract(x, y)
    elif operation == '*':
        return multiply(x, y)
    elif operation == '/':
        return divide(x, y)
    else:
        return "❌ Error: Invalid operation"

# Main function
def main():
    print("🧮 Simple CLI Calculator (basic version)")
    while True:
        try:
            x = float(input("Enter the first number: "))
            operation = input("Enter operation (+, -, *, /): ")
            y = float(input("Enter the second number: "))
            result = calculate(x, y, operation)
            print(f"Result: {result}")
        except ValueError:
            print("❌ Error: Invalid number input")
        
        # Ask the user if they want to continue
        again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if again not in ('yes', 'y'):
            print("Goodbye! 👋")
            break

if __name__ == "__main__":
    main()